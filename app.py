from config import app
from models import User, ZendeskTicket, Prompt, SuggestedSolution 

@app.route("/login", methods=["POST"])
def login():
    pass

@app.route("/logout", methods=["POST"])
def logout():
    pass

@app.get("/me")
def me():
    pass

@app.route("/query", methods=["POST"])
def query():
    pass

@app.route("/history", methods=["POST"])
def history():
    pass


    