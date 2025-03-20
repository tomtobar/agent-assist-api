from config import db, app
from models import User, ZendeskTicket, Prompt, SuggestedSolution, PromptStatus
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
            User.save(db.session, email=email)
            
            

    def create_zendesk_tickets(self, quantity):
        school_types = ["High", "Middle", "Intermediate", "Elementary"]
        for _ in range(quantity):
            school_name = f"{fake.first_name()} {fake.last_name()} {fake.random_element(school_types)} School"
            ticket_number = str(random.randint(96000, 99000))
            ZendeskTicket.save(db.session, school_name=school_name, ticket_number=ticket_number)
        
    def create_prompts(self, quantity):
        for _ in range(quantity):
            content = fake.ems_question()
            status = fake.random_element(elements=PromptStatus)
            user_id = db.session.query(User).order_by(func.random()).first().id
            zd_ticket_id = db.session.query(ZendeskTicket).order_by(func.random()).first().id
            
            Prompt.save(
                db.session,
                content=content,
                status=status,
                user_id=user_id,
                zd_ticket_id=zd_ticket_id
            )

    def create_suggested_solutions(self, quantity):
        for _ in range(quantity):
            prompt_id = db.session.query(Prompt).order_by(func.random()).first().id
            response_generated = fake.random_element([True, False])
            content = fake.ai_response()
            supporting_docs = [{"links": ["https://schooladmin.zendesk.com/hc/en-us/articles/6219028030605-Billing-Setting-the-Financial-Split", "https://schooladmin.zendesk.com/hc/en-us/articles/6218999287309-Billing-Import-Billing-Transactions", "https://schooladmin.zendesk.com/hc/en-us/articles/6219051055373-Tuition-Assistance-Financial-Aid"]}]
            feedback_good = fake.random_element([True, False])
            ai_confidence_score = random.uniform(0, 1)
            tokens_used = random.randint(50, 150)
            processing_time = round(random.uniform(0.01, 2.5), 6)
            new = SuggestedSolution.save(
                db.session,
                prompt_id=prompt_id,
                response_generated=response_generated,
                content=content,
                supporting_docs=supporting_docs,
                feedback_good=feedback_good,
                ai_confidence_score=ai_confidence_score,
                tokens_used=tokens_used,
                processing_time=processing_time
            )
            print(new)

    def delete_all_instances_for(self, model):
        db.session.query(model).delete()
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seeder = Seeder()
        # seeder.create_users(1)
        # seeder.create_zendesk_tickets(1)
        # seeder.create_prompts(1)
        seeder.create_suggested_solutions(1)

