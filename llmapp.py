import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

#Load environment varialbles

groq_api_key = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY']= os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "True"
os.environ['LANGCHAIN_PROJECT'] = 'Q&A Chatbot with Groq AI'

#Prompt Tenmplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are an intelligent AI answer the following questions asked"),
        ('user',"Question:{question}")
    ]

)

llm = ChatGroq(groq_api_key=groq_api_key,model = "llama-3.1-8b-instant")

def generate_response (question):
    parser = StrOutputParser()
    chain = prompt|llm|parser
    ans = chain.invoke({"question":question})
    return ans

st.title("Simple Q&A chatbot using GROQ AI")
st.write("Please enter your question")
user_input = st.text_input("here")
if user_input:
    res = generate_response(user_input)
    st.write(res)
else :
    st.write("Please enter question")

