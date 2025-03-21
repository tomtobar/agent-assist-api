from config import pinecone_client
from openai_handler import OpenaiHandler
import json
import ipdb

oh = OpenaiHandler()

index_name = "ems-genie"
index = pinecone_client.Index(index_name)

class PineconeHandler():
    def retrieve_docs(self, query, top_k=3):
        query_vector = oh.embed_text(query)
        results = index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True,
            namespace="ems-articles"
        )
        
        return results["matches"]
