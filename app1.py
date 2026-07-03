import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

if "chat_history" not  in st.session_state:
    st.session_state.chat_history = []

prompt = PromptTemplate.from_template(
    """you are help ai assistant.

    here is conversation history :

    {user_query}

    answer based on conversation."""
)

llm = ChatGoogleGenerativeAI(
    model ="gemini-2.5-flash"
)

parser = StrOutputParser()

get_res = prompt | llm | parser

st.title("Guhan's First & New Chatbot Project")

for msg in st.session_state.chat_history:
    st.write(msg)

User_question = st.chat_input("Type your message")

if User_question:
    st.session_state.chat_history.append("User" + User_question)

    title = get_res.invoke({
        "user_query":"\n".join(st.session_state.chat_history)
    })

    st.write("You:",User_question)
    st.write("Bot:",title)

    st.session_state.chat_history.append("AI:" + title)