from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime, timezone
from sqlalchemy.inspection import inspect
from config import db
import ipdb

class Base(DeclarativeBase):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    @classmethod
    def save(cls, session=None, **kwargs):
        new_record = cls(**kwargs)
        try:
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return new_record
        except Exception as e:
            session.rollback()
            raise e
    
    @classmethod
    def find_or_create_by(cls, attribute, value):
        new_instance = db.session.query(cls).filter(getattr(cls, attribute) == value).first()
        if new_instance is None:
            new_instance = cls.save(db.session, **{attribute: value})
        return new_instance
    
    @classmethod
    def find(cls, id):
        return db.session.query(cls).filter_by(id=id).first()

    def to_dict(self):
        return {column.key: getattr(self, column.key) for column in inspect(self).mapper.column_attrs}

