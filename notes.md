## Thoughts
- Fetch all schools (using SA api??) including subdomain to link from frontend

## Todo
- Think about routes
- create routes

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

