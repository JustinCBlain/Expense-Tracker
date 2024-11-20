"""
Sets up basic layout
"""

import streamlit as st
from src.tabs.dailytab import generate_example_graph
from src.tabs.distributiontab import generate_example_pie_chart
from src.tabs.aitab import generate_example_ai_chat
from src.tabs.expensecolumn import generate_expense_column
from src.tabs.time_plot import generate_time_plot
from src.expense_manager import ExpenseManager


def show_layout():
    """Base display for page
    """
    # Page Configuration
    st.set_page_config(layout="wide")

    # Instantiate the ExpenseManager
    if 'expense_manager' not in st.session_state:
        st.session_state.expense_manager = ExpenseManager()

    # Title of Application
    st.title("Application Title")

    # Create Two Columns - left is 3 parts, right is 5 parts
    col1, col2 = st.columns([3, 5])

    # Column 1 - Left most column
    with col1:
        st.header("Expenses")
        generate_expense_column()

    # Column 2 - Right most column
    with col2:
        st.header("Visualizations")

        # Create Container for Tabs
        with st.container():
            st.subheader("Title in Container")

            # Create Tabs
            tabs = st.tabs(["Expense Distribution", "Expenses over Time", "Time plot", "AI"])

            # Tab Content
            with tabs[0]:
                st.write("Expense Distribution")
                entries = st.session_state.expense_manager.get_entries()
                generate_example_pie_chart(entries)

            with tabs[1]:
                st.write("Expenses over Time")
                entries = st.session_state.expense_manager.get_entries()
                generate_example_graph(entries)

            with tabs[2]:
                st.write("Content for Daily Expense Timelines")
                entries = st.session_state.expense_manager.get_entries()
                generate_time_plot(entries)

            with tabs[3]:
                st.write("Content for AI tab")
                generate_example_ai_chat()
