"""Main entrypoint to app"""
import streamlit as st

from src.expense_manager import ExpenseManager
from user_management import show_login
from layout import show_layout

# Page Configuration
st.set_page_config(
    page_title="Projekt Awesome",
    layout="wide"
)


def main():
    """
    Manages pages and session info
    """

    if st.session_state.logged_in:
        st.session_state.expense_manager = ExpenseManager()
        user_data = f"{st.session_state.username}_data"
        st.session_state.expense_manager.set_entries(st.session_state[user_data])
        show_layout()
    else:
        show_login()


# Run Application
if __name__ == "__main__":
    main()
