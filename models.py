from config import db
from base import Base
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB, ENUM

import enum

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)

    prompts = db.relationship('Prompt', back_populates='user', lazy=True)

    def __repr__(self):
        return f"\n<User \n" + \
        f"\tid={self.id}\n" + \
        f"\temail={self.email}\n" + \
        f"\tcreated_at={self.created_at}\n" + \
        f"\tupdated_at={self.updated_at}\n" + \
        ">"
        


class ZendeskTicket(Base):
    __tablename__ = 'zendesk_tickets'

    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(), nullable=False)
    ticket_number = db.Column(db.String(), nullable=False)

    prompts = db.relationship('Prompt', back_populates='zendesk_ticket', lazy=True)

    def __repr__(self):
        return f"\n<ZendeskTicket \n" + \
        f"\tid={self.id}\n" + \
        f"\tschool_name={self.school_name}\n" + \
        f"\tticket_number={self.ticket_number}\n" + \
        f"\tcreated_at={self.created_at}\n" + \
        f"\tupdated_at={self.updated_at}\n" + \
        ">"


class PromptStatus(enum.Enum):
    PENDING = 'Pending'
    PROCESSED = 'Processed'
    ERROR = 'Error'

status_enum = ENUM(PromptStatus, name="promptstatus", create_type=False)

class Prompt(Base):
    __tablename__ = 'prompts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(PromptStatus), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    zd_ticket_id = db.Column(db.Integer, db.ForeignKey('zendesk_tickets.id'), nullable=True)

    user = db.relationship('User', back_populates='prompts')
    zendesk_ticket = db.relationship('ZendeskTicket', back_populates='prompts')
    
    suggested_solutions = db.relationship('SuggestedSolution', back_populates='prompt', lazy=True)

    def __repr__(self):
        return f"\n<Prompt \n" + \
        f"\tid={self.id}\n" + \
        f"\tcontent={self.content}\n" + \
        f"\tstatus={self.status}\n" + \
        f"\tuser_id={self.user_id}\n" + \
        f"\tzd_ticket_id={self.zd_ticket_id}\n" + \
        ">"
    
    
class SuggestedSolution(Base):
    __tablename__ = 'suggested_solutions'

    id = db.Column(db.Integer, primary_key=True)

    prompt_id = db.Column(db.Integer, db.ForeignKey('prompts.id'), nullable=False)
    prompt = db.relationship('Prompt', back_populates='suggested_solutions')

    response_generated = db.Column(db.Boolean, nullable=False, default=False)
    content = db.Column(db.Text)
    supporting_docs = db.Column(JSONB, nullable=False, server_default= '[]')
    feedback_good = db.Column(db.Boolean, nullable=True)
    ai_confidence_score = db.Column(db.Float, nullable=True)
    tokens_used = db.Column(db.Integer, nullable=True)
    processing_time = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"\n<SuggestedSolution \n" + \
        f"\tid={self.id}\n" + \
        f"\tcontent={self.content}\n" + \
        f"\tsupporting_docs={self.supporting_docs}\n" + \
        f"\tfeedback_good={self.feedback_good}\n" + \
        f"\tai_confidence_score={self.ai_confidence_score}\n" + \
        f"\ttokens_used={self.tokens_used}\n" + \
        f"\tprocessing_time={self.processing_time}\n" + \
        ">"