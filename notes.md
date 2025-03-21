## Thoughts
- Fetch all schools (using SA api??) including subdomain to link from frontend

## Todo
- ✅ Think about routes
- ✅ create routes
- error handle Pinecone#retrieve_docs
- error handle OpenaiHandler#get_ai_response
- Add docstrings
- bad at giving instructions on navigating the site. need to add text instructions on how to find each part of the site.

## Routes
- POST, "/login":
    - find user my email
    - fake auth validation—check if email ends in @finalsite.com. `return {"error": "Unauthorized"}, 403` if not 
    - set session["user_id"] if authenticated
    - On successful login: `return {"message": "Login successful", "email": email}`

- POST, "/logout":
    - delete session["user_id"]
    - `return {"message": "Logout successful"}`

- GET, "/me"
    - Check if session exists `session["user_id"]`
        - if not, return `{"error": "Not logged in"}, 401`
    - Look up user and `return {"email": email}`

- POST, "/query": 
    - recieve a question
    - send to Pinecone and await response
        - Create Prompt instance
        - Establish relationship between current user and prompt
    - return 3 most relevant articles
    - send articles to OpenAI
        - limit tokens?
    - return: `{"response": ai_response, "articles": [aritcles]}`

- GET, "/history":
    - Check for logged in user `session["user_id"]`
        - return error if not
    - Get User.prompt_history 
    - `return {"history": history}`

## Questions
- How do I add a new charge to a ledger?
- How can I create a new field?
- How to create a new email template?
