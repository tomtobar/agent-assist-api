from config import db, app
from models import User, ZendeskTicket, Prompt, SuggestedSolution, PromptStatus
from datetime import datetime, timezone
from faker import Faker
from sqlalchemy.sql.expression import func
from ems_question_provider import EmsQuestionProvider
import random

fake = Faker()
fake.add_provider(EmsQuestionProvider)

class Seeder():
    def create_users(self, quanity):
        for _ in range(quanity):
            fake_first_name = fake.first_name()
            fake_last_name = fake.last_name()
            email = f"{fake_first_name}.{fake_last_name}@finalsite.com"
            new_user = User.save(db.session, email=email)
            print(new_user)
            

    def create_zendesk_tickets(self, quantity):
        school_types = ["High", "Middle", "Intermediate", "Elementary"]
        for _ in range(quantity):
            school_name = f"{fake.first_name()} {fake.last_name()} {fake.random_element(school_types)} School"
            ticket_number = str(random.randint(96000, 99000))
            new_zd_ticket = ZendeskTicket.save(db.session, school_name=school_name, ticket_number=ticket_number)
            print(new_zd_ticket)
        
    def create_prompts(self, quantity):
        content = fake.ems_question()
        status = fake.random_element(elements=PromptStatus)
        user_id = db.session.query(User).order_by(func.random()).first().id
        zd_ticket_id = db.session.query(ZendeskTicket).order_by(func.random()).first().id
        
        new_prompt = Prompt.save(
            db.session,
            content=content,
            status=status,
            user_id=user_id,
            zd_ticket_id=zd_ticket_id
        )
        print(new_prompt)
        

    def create_suggested_solutions(self):
        pass

    def create_prompt_statues(self):
        pass

    def delete_all_instances_for(self, model):
        db.session.query(model).delete()
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seeder = Seeder()
        # seeder.create_users(1)
        # seeder.create_zendesk_tickets(1)
        seeder.create_prompts(1)
