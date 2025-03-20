from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime, timezone
from config import db

class Base(DeclarativeBase):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    @classmethod
    def save(cls, session: Session, **kwargs):
        new_record = cls(**kwargs)
        try:
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return new_record
        except Exception as e:
            session.rollback()
            raise e