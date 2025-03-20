from config import app
from flask import request, jsonify, session
import ipdb
from models import User, ZendeskTicket, Prompt, SuggestedSolution 

def valid_email(email):
    return email.endswith("@finalsite.com")

@app.route("/login", methods=["POST"])
def login():
    params = request.args
    email = params.get("email")
    if not valid_email(email):
        return jsonify({"error": "Not a valid email"}), 401

    user = User.find_or_create_by("email", email)
    session["user_id"] = user.id

    return jsonify({"message": "Login successful", "user": user.to_dict()})

@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out"}), 204
    
@app.get("/me")
def me():
    if "user_id" in session:
        user = User.find(session["user_id"])
        return jsonify({"user": user.to_dict()})
    
    return jsonify({"error": "Not logged in"}), 401
   

@app.route("/query", methods=["POST"])
def query():
    pass

@app.route("/history", methods=["POST"])
def history():
    pass


    