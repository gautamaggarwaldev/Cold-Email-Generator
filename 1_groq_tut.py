from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

res = llm.invoke("The first person who climb mount everest?")

print(res.content)