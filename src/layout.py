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
    """
    Base display for page
    """

    # Page Configuration
    st.set_page_config(
        page_title="Daily Expenses",
        layout="wide"
    )

    st.write("""
        <style>
            /* AI Tab Styles */
           #tabs-bui3-tabpanel-3 > div[data-testid="stVerticalBlockBorderWrapper"] > div.e1f1d6gn1 > div.stVerticalBlock > div:last-child {
                max-height: 500px;
                overflow-y: auto;
            }
        </style>
    """, unsafe_allow_html=True)

    # Instantiate the ExpenseManager
    if 'expense_manager' not in st.session_state:
        st.session_state.expense_manager = ExpenseManager()

    # Title of Application
    st.title("Expense Tracker")

    # Create Two Columns - left is 3 parts, right is 5 parts
    col1, col2 = st.columns([4, 4])

    # Column 1 - Left most column
    with col1:
        st.subheader("Transaction Records")
        generate_expense_column()

    # Column 2 - Right most column
    with col2:
        # st.header("Insights Dashboard")

        # Create Container for Tabs
        with st.container():
            st.subheader("Dashboard Sections")

            # Create Tabs
            tabs = st.tabs(["Daily Trends", "Spending Distribution", "Summary", "AI Insights"])

            # Tab Content

            with tabs[0]:
                # st.write("Content for Daily Expense Timelines")
                entries = st.session_state.expense_manager.get_entries()
                generate_time_plot(entries)

            with tabs[1]:
                # st.write("Expense Distribution")
                entries = st.session_state.expense_manager.get_entries()
                generate_example_pie_chart(entries)

            with tabs[2]:
                # st.write("Expenses over Time")
                entries = st.session_state.expense_manager.get_entries()
                generate_example_graph(entries)

            with tabs[3]:
                # st.write("Content for AI tab")
                generate_example_ai_chat()
