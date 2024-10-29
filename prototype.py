"""
        Project Application - Expense Tracker
CMSC 495 7382 Capstone in Computer Science (2248)
                Blain, Justin
                Reynnells, Kayla
                Shultz, Mary
                Thakkar, Kirtan
                Truitt, Mark

One way to run the first time:
streamlit run prototype.py
press enter when email field comes up and the app will appear in the webpage

This is a prototype to visualize how to use streamlit and how the Expense Tracker will look

"""

# Imports
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Setting Page Title
st.set_page_config(page_title="Expense Tracker", layout="wide")

# Adding Main Title to app
st.title("Welcome to Capstone Project Group Awesome")

# Example line graph
def generate_example_graph():
    # Fake data for line graph
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Creating plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='Fake Data', color='blue')
    plt.title("Example Graph")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()
    plt.grid()

    # Show plot in Streamlit Widget
    st.pyplot(plt)

# Example pie chart
def generate_example_pie_chart():
    # Create fake date for pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen']

    # Create pie chart
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Example Pie Chart")

    # Show pie chart in Streamlit Widget
    st.pyplot(plt)

# Example Expense Entries
def expense_entry():
    st.subheader("Expense Entry")

    # Initialize session state for expenses if it doesn't exist
    if 'expenses' not in st.session_state:
        st.session_state.expenses = []

    # Input rows for expense entry
    num_rows = st.number_input("Number of expense entries", min_value=1, value=1)

    for i in range(num_rows):
        # Two columns for category and amount
        col_cat, col_exp = st.columns([2, 1])
        with col_cat:
            category = st.selectbox(f"Select Category for Entry {i+1}", ["Food", "Transport", "Utilities", "Rent"], key=f"category_{i}")
        with col_exp:
            amount = st.number_input(f"Amount for Entry {i+1}", min_value=0.0, format="%.2f", key=f"amount_{i}")

        # Append to session state expenses list with button
        if st.button("Add Expense"):
            if category and amount > 0:
                st.session_state.expenses.append({"Category": category, "Expense Amount": amount})

    # Display the expense data in a DataFrame
    if st.session_state.expenses:
        # Create a new DataFrame from the expense data
        expense_data = pd.DataFrame(st.session_state.expenses)

        # Add a 'Delete' column for buttons
        expense_data['Delete'] = ""
        # Display the DataFrame as a table
        for index, row in expense_data.iterrows():
            expense_data.at[index, 'Delete'] = f"Delete {index}"

        # Display the DataFrame in a table format
        exp_table = st.dataframe(expense_data, use_container_width=True)

        # Create delete buttons in the DataFrame
        for index in expense_data.index:
            if st.button(f"Delete {index}"):
                st.session_state.expenses.pop(index)
                # Exit the loop after deletion to refresh the display
                break

# Layout function to display everything in correct locations
def layout():
    # Container for chat box
    with st.container():
        # Two column layout for income and ai response
        col1, col2 = st.columns([2, 3])

        # Income Input
        with col1:
            income_input = st.text_input("Enter your Income:", placeholder="Type Some Money...")

            # Call expense entry function
            expense_entry()

        # AI Response
        with col2:
            st.subheader("Fake AI Chat Box")
            # Create text area for user input
            user_input = st.text_area("Enter Information:", height=100)
            # Placeholder for AI Chat response
            if user_input:
                st.text_area("AI:", value="This is a fake response.", height=100)


            # Graph Layout
            st.subheader("Graphs")
            graph_col1, graph_col2 = st.columns([1, 1])
            with graph_col1:
                generate_example_graph()
            with graph_col2:
                generate_example_pie_chart()

# Execute application
if __name__ == "__main__":
    layout()
