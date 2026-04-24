import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

load_dotenv()

## langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked"),
    ("user", "Question: {question}")
])

## streamlit framework
st.title("Langchain Demo with Deepseek Model")
input_text=st.text_input("What question you have in your mind?")


## Ollama LLAMA2 or other model which i wanted to use
llm=ChatOllama(model="deepseek-r1:1.5b")

##output parser
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))