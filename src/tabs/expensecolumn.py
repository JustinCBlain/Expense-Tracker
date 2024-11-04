import streamlit as st
import pandas as pd
from expense_manager import ExpenseManager

from util.constants import AMOUNT_COL, CATEGORIES, CATEGORY_COL, DATE_COL, TIME_COL, VENDOR_COL

# Create expense manager instance
expense_manager = ExpenseManager()

def generate_expense_column():
    
    # Display the entries in a structured layout
    st.subheader("Entries Table")
    col_config = {
        DATE_COL: st.column_config.DateColumn(label=DATE_COL),
        TIME_COL: st.column_config.TimeColumn(label=TIME_COL),
        CATEGORY_COL: st.column_config.SelectboxColumn(label=CATEGORY_COL, options=CATEGORIES),
        VENDOR_COL: st.column_config.Column(label=VENDOR_COL),
        AMOUNT_COL: st.column_config.NumberColumn("Dollar amounts", format="$ %.2f")
    }

    entries = st.session_state.expense_manager.get_entries()
    editing = st.data_editor(entries, use_container_width=True, column_config=col_config, num_rows="dynamic")

    if st.button("Save"):
        st.session_state.expense_manager.set_entries(editing)
        st.success("You have saved your expenses to the database successfully")

    uploaded_file = st.file_uploader("Save work and add from file")

    if uploaded_file is None:
        st.session_state["file_processed"] = False

    if uploaded_file is not None:
        if not st.session_state["file_processed"]:
            with st.spinner("Processing"):
                st.write(f"Processing {uploaded_file.name}...")
                df = pd.read_csv(uploaded_file)
                df[DATE_COL] = pd.to_datetime(df[DATE_COL])
                df[TIME_COL] = df[DATE_COL].dt.time
                df[DATE_COL] = df[DATE_COL].dt.date
                st.session_state.expense_manager.set_entries(editing)
                st.session_state.expense_manager.add_entries(df)
                st.success(f"You have uploaded the file {uploaded_file.name}")
        st.session_state["file_processed"] = True
