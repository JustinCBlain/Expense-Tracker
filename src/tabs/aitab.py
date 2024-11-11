"""Holds tab for AI chat functionality"""
import streamlit as st

def generate_example_ai_chat():
    """AI Chatbot placeholder"""
    st.subheader("Fake AI Chat Box")
    # Create text area for user input
    user_input = st.text_area("Enter Information:", height=100)
    # Placeholder for AI Chat response
    if user_input:
        st.text_area("AI:", value="This is a fake response.", height=100)
