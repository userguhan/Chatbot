import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


load_dotenv()


# for key, value in os.environ.items():
#     print(f"{key} = {value}")




prompt = PromptTemplate.from_template(
    """You are a helpful AI assistant.

    Question:
    {user_query}"""
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()

get_res = prompt | llm | parser

chat_history = []

while True:
    User_question = input("User Msg: ")
    if User_question == "stop":
        break
    chat_history.append("User :" + User_question)

    title = get_res.invoke({
    "user_query" : "\n".join(chat_history)
    }) 
    print(title)

    chat_history.append("AI: " + title)