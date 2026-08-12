from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import os

load_dotenv()

client = Groq(api_key= os.getenv("GROQ_API_KEY"))

#conversation = client.chat.completions.create(
 #   model="llama-3.3-70b-versatile",
 #   messages=[
 #       {"role": "system", "content": "You are a helpful assistant."},
 #       {"role": "user", "content": "What is the capital of france?"},
 #   ],
    
#)
#print(conversation.choices[0].message.content)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
text = "Your text string goes here"

embedding = embedding_model.encode(text)

print(embedding)
print("Embedding dimension:", len(embedding))