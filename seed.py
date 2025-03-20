from config import db, app
from models import User, ZendeskTicket, Prompt, SuggestedSolution, PromptStatus
from datetime import datetime, timezone
from faker import Faker
import random

fake = Faker()

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
            school_name = f"{fake.first_name()} {fake.last_name()} {random.choice(school_types)} School"
            ticket_number = str(random.randint(96000, 99000))
            new_zd_ticket = ZendeskTicket.save(db.session, school_name=school_name, ticket_number=ticket_number)
            print(new_zd_ticket)
        
    def create_prompts(self):
        pass

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
        seeder.create_zendesk_tickets(1)
