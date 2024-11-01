import streamlit as st
from datetime import datetime
import pandas as pd
from expense_manager import ExpenseManager

# Create expense manager instance
expense_manager = ExpenseManager()

def generate_expense_column():
    st.header("Expense Column")

    if 'entries' not in st.session_state:
        st.session_state.entries = pd.DataFrame(columns=["Date", "Category", "Description", "Cost"])

    # User input for expense
    description = st.text_input("Enter Expense")

    # Create columns for category and cost
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        # Create initial date widget
        initial_date = st.date_input("Select a Date", value=datetime.today())
    with col2:
        # User selects category
        category_options = ["Rent", "Utilities", "Cable", "Internet", "Car", "Insurance"]
        category = st.selectbox("Select a Category", options=category_options)

    with col3:
        # User selects cost
        cost = st.number_input("Enter Cost", min_value=0.0, step=0.01)

    # Submit Button
    if st.button("Submit"):
        if description:
            st.session_state.expense_manager.add_entry(initial_date, category, description, cost)
            st.success(f"You have Entered: '{description}' in the Category: {category} with a cost of: ${cost} on: {initial_date}")
        else:
            st.warning("Please Enter a Description before Submitting")
    
    # Display the entries in a structured layout
    st.subheader("Entries Table")
    entries = st.session_state.expense_manager.get_entries()
    if not entries.empty:
        for index, entry in entries.iterrows():
            cols = st.columns([2, 2, 2, 2, 1])  # Create columns for description, cost, category, and delete button
            with cols[0]:
                st.write(entry["Date"])
            with cols[1]:
                st.write(entry["Description"])
            with cols[2]:
                st.write(f"${entry['Cost']:.2f}")
            with cols[3]:
                st.write(entry["Category"])
            with cols[4]:
                if st.button("❌", key=f"delete_{index}"):  # Delete button with a X symbol
                    st.session_state.expense_manager.delete_entry(index)
                    st.success(f"Deleted entry: '{entry['Description']}' with cost ${entry['Cost']} in category '{entry['Category']}' on:'{entry['Date']}'.")
                    st.rerun()
    else:
        st.write("No entries available.")
    
    #st.subheader("Expense Table")
    #st.dataframe(st.session_state.entries)