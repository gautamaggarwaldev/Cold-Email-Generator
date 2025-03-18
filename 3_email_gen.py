from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import pandas as pd
import chromadb
import uuid
load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

loader  = WebBaseLoader("https://careers.nike.com/software-engineer-i-itc/job/R-51569")

page_data = loader.load().pop().page_content

# print(page_data)

prompt_extract = PromptTemplate.from_template(
    """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing
        following keys: `role`, `experience`, `skills` and `description`.
        Only return valid JSON.
        ### VALID JSON (NO PREAMBLE): 
    """
)

chain = prompt_extract | llm
res = chain.invoke(input={'page_data':page_data})
# print(res.content) # string

json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)
# print(json_res)
# print(type(json_res))  <class 'dict'>

df = pd.read_csv("my_portfolio.csv")
# print(df)

client = chromadb.PersistentClient('vector_db_store')
collection = client.get_or_create_collection(name="portfolio")

if not collection.count():
    for _, row in df.iterrows():
        collection.add (
            documents = row['Techstack'],
            metadatas={"links": row["Links"]},
            ids=[str(uuid.uuid4())]
        )

job = json_res
# print(job['skills'])

links = collection.query(query_texts=job['skills'], n_results=2).get('metadatas', [])
# print(links)

prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Garima Govil, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Mohan, BDE at AtliQ. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

chain_email = prompt_email | llm
res = chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)
