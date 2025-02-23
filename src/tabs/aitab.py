"""Holds tab for AI chat functionality"""
import logging
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

logger = logging.getLogger(__name__)

def stringify_relevant_info():
    """
    Get and stringify the most recent 60 transactions.
    """
    df = st.session_state.expense_manager.get_entries()
    df = df.sort_values(by="Date").head(60)
    return df.to_string()


def generate_response(input_text):
    """
    Use Ollama to generate a text response
    """
    model = ChatOllama(temperature=0.3,
                       model="llama3.2:1b",
                       base_url="http://ollama-container:11434")
    info = stringify_relevant_info()

    system_template = """
        You are a helpful financial advisor.
        These are the last 60 transaction for your mentee: {financial_data}.
        Be cautious and use exact stats whenever possible to answer their questions.
    """

    template = ChatPromptTemplate([
        ("system", system_template),
        ("ai", "Hello, what can I help you with today?"),
        ("human", "{user_input}"),
    ])
    input_template = template.invoke({
        "financial_data": info,
        "user_input": input_text
    })
    return model.invoke(input_template)


def generate_example_ai_chat():
    """AI Chatbot placeholder"""

    st.markdown("###### Chat Box")

    with st.container():
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            response = generate_response(prompt)
            msg = response.content
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)