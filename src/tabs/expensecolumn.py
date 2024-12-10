"""Core logic for generating the expense column, including data read/write"""

import streamlit as st
import pandas as pd
from src.expense_manager import ExpenseManager

from src.util.constants import AMOUNT_COL, CATEGORIES, CATEGORY_COL, DATE_COL, TIME_COL, VENDOR_COL

# Reference expense manager instance
if 'expense_manager' not in st.session_state:
    st.session_state.expense_manager = ExpenseManager()
expense_manager = st.session_state.expense_manager

def generate_expense_column():
    """Generates the expense column. This includes data manipulation and ingest.
    """
    # Display the entries in a structured layout
    # st.subheader("Entries Table")
    col_config = {
        DATE_COL: st.column_config.DateColumn(label=DATE_COL),
        TIME_COL: st.column_config.TimeColumn(label=TIME_COL),
        CATEGORY_COL: st.column_config.SelectboxColumn(label=CATEGORY_COL, options=CATEGORIES),
        VENDOR_COL: st.column_config.Column(label=VENDOR_COL),
        AMOUNT_COL: st.column_config.NumberColumn("Dollar amounts", format="$ %.2f")
    }

    entries = st.session_state.expense_manager.get_entries()
    editing = st.data_editor(
        entries,
        use_container_width=True,
        column_config=col_config,
        num_rows="dynamic"
    )

    uploaded_file = st.file_uploader("Save work and add from file")

    if uploaded_file is None:
        st.session_state["file_processed"] = False

    if uploaded_file is not None:
        if not st.session_state["file_processed"]:
            with st.spinner("Processing"):
                st.write(f"Processing {uploaded_file.name}...")
                st.session_state.expense_manager.set_entries(editing)
                df = process_file(uploaded_file)
                st.session_state.expense_manager.add_entries(df)
                st.success(f"You have uploaded the file {uploaded_file.name}")
        st.session_state["file_processed"] = True

    st.session_state.editing = editing

    user_data = f"{st.session_state.username}_data"
    st.session_state[user_data] = st.session_state.expense_manager.get_entries()


def process_file(file_input):
    """
    Logic for file processing. This assumes the columns: "Date", "Time", "Category",
    "Vendor", and "Amount". If values are missing initially, they can be safely added
    via the UI, but this does currently assume the columns are present and correctly named.

    Args:
        file_input (file): Can accept either a filepath or a buffer, for ease of testing

    Returns:
        dataframe representing the ingested data
    """
    df = pd.read_csv(file_input)
    df[DATE_COL] = pd.to_datetime(df[DATE_COL])
    df[TIME_COL] = df[DATE_COL].dt.time
    df[DATE_COL] = df[DATE_COL].dt.date
    return df
