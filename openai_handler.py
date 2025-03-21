from config import openai_client
import ipdb

class OpenaiHandler():
    def embed_text(self,text):
        response = openai_client.embeddings.create(input=text, model="text-embedding-ada-002")
        return response.data[0].embedding

    def get_ai_response(self, docs, query):
        docs_body = ", ".join([
            doc["metadata"]["content"] 
            for doc in docs 
            if "content" in doc["metadata"] and doc["metadata"]["content"]
        ])
        prompt = f"""
        Question: {query}

        Based on the provided documentation, extract and format the exact steps a user would need to follow. If the documentation does not provide a numbered list, convert clearly implied actions into a step-by-step format using only the language and intent found in the documentation.

        Use imperative language like “Go to”, “Click”, or “Toggle”, and always refer to the Finalsite Enrollment application as **"the site"** or **"your site"**— never say "your application"."

        Avoid paraphrasing or adding outside context. Do not guess functionality. Only translate what’s explicitly stated or clearly implied into clear instructions.

        Documentation:
        {docs_body}
        """

        message = [{"role": "user", "content": prompt}]
    
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=message,
        )

        return response
