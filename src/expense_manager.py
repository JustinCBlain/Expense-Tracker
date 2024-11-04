import logging
import pandas as pd
from sqlalchemy import create_engine

from util.constants import DATE_COL, EXPENSE_COLUMNS, SQL_TABLE, TIME_COL

class ExpenseManager:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@postgres:5432/expenses')
        try:
            self.entries = pd.read_sql_table(SQL_TABLE, self.engine)
            self.entries[TIME_COL] = self.entries[TIME_COL].dt.time
            self.entries[DATE_COL] = self.entries[DATE_COL].dt.date
        except:
            logging.warning("No table present, creating empty dataframe!")
            self.entries = pd.DataFrame(columns=EXPENSE_COLUMNS)

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries = self.entries.drop(index).reset_index(drop=True)

    def get_entries(self):
        return self.entries

    def set_entries(self, entries):
        self.entries = entries
        self.entries.to_sql(SQL_TABLE, self.engine, if_exists="replace", index=False)

    def add_entries(self, new_entries):
        self.entries = pd.concat([self.entries, new_entries], ignore_index=True)