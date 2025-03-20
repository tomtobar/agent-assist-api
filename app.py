from config import app
from models import User, ZendeskTicket, Prompt, SuggestedSolution 

@app.get("/")
def home():
    return "Hello, Agent Assist!"