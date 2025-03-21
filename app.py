from config import app
from flask import request, jsonify, session
import ipdb
from models import User, ZendeskTicket, Prompt, PromptStatus, SuggestedSolution
from pinecone_handler import PineconeHandler
from openai_handler import OpenaiHandler

pc = PineconeHandler()
oh = OpenaiHandler()

def valid_email(email):
    return email.endswith("@finalsite.com")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    # ipdb.set_trace()
    if not valid_email(email):
        return jsonify({"error": "Not a valid email"}), 401

    user = User.find_or_create_by("email", email)
    session["user_id"] = user.id

    return jsonify({"message": "Login successful", "user": user.to_dict()})

@app.route("/logout", methods=["DELETE"])
def logout():
    session.pop("user_id", None)
    return jsonify({"message": "Logged out"})
    
@app.route("/me", methods=["GET"])
def me():
    if "user_id" in session:
        user = User.find(session["user_id"])
        return jsonify({"user": user.to_dict()})
    
    return jsonify({"error": "Not logged in"}), 401
   

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query = data.get("content")
    new_prompt = Prompt(
        content=query,
        status=PromptStatus.PENDING,
        user_id=session["user_id"],
    )
    docs = pc.retrieve_docs(query) # Could optimize with Pinecone asyc requests: https://docs.pinecone.io/reference/python-sdk#async-requests
    # Need to error handle docs

    ai_response = oh.get_ai_response(docs, query)
    return jsonify({"message": ai_response.choices[0].message.content})

@app.route("/history", methods=["POST"])
def history():
    pass


    