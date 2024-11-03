
import streamlit as st
from tabs.dailytab import generate_example_graph
from tabs.distributiontab import generate_example_pie_chart
from tabs.aitab import generate_example_ai_chat
from tabs.expensecolumn import generate_expense_column
from expense_manager import ExpenseManager


def show_layout():
    # Page Configuration
    st.set_page_config(layout="wide")

    # Instantiate the ExpenseManager
    if 'expense_manager' not in st.session_state:
        st.session_state.expense_manager = ExpenseManager()

    # Title of Application    
    st.title("Application Title")

    # Create Two Columns - left is one part, right is 3 parts
    col1, col2 = st.columns([3, 5])

    # Column 1 - Left most column
    with col1:
        st.header("Column 1")
        st.write("This is the left column")
        generate_expense_column()
    
    # Column 2 - Right most column
    with col2:
        st.header("Column 2")

        # Create Container for Tabs
        with st.container():
            st.subheader("Title in Container")

            # Create Tabs
            tabs = st.tabs(["Daily", "Distribution", "Overall", "AI"])

            # Tab Content
            with tabs[0]:
                st.write("Content for Daily Tab")
                entries = st.session_state.expense_manager.get_entries()
                generate_example_pie_chart(entries)

            with tabs[1]:
                st.write("Content for Distribution Tab")
                generate_example_graph()
            
            with tabs[2]:
                st.write("Content for Overall Tab")
            
            with tabs[3]:
                st.write("Content for AI tab")
                generate_example_ai_chat()