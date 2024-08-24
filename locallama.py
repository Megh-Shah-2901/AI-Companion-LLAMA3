from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os

os.environ['LANGCHAIN_TRACING_V2']= 'true'
os.environ['LANGCHAIN_API_KEY'] = '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'

st.title("Langchain Chatbot With Llama 3")
input_text = st.text_area("Search the topic you want...")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user's queries."),
        ("user","Question:{question}")
    ]
)

llm = Ollama(model='llama3')
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))