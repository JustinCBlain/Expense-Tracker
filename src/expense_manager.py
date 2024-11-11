"""
Core data class for handling expenses
"""

import logging
import pandas as pd
from sqlalchemy import create_engine

from src.util.constants import DATE_COL, EXPENSE_COLUMNS, SQL_TABLE

class ExpenseManager:
    """Handles expense data, reads/writes from db
    """
    def __init__(self):
        """Initializes ExpenseManager
        """
        self.engine = create_engine('postgresql://postgres:postgres@postgres:5432/expenses')
        try:
            self.entries = pd.read_sql_table(SQL_TABLE, self.engine)
            self.entries[DATE_COL] = self.entries[DATE_COL].dt.date
        except Exception as exc:
            logging.warning("No table present, creating empty dataframe!")
            logging.debug(exc)
            self.entries = pd.DataFrame(columns=EXPENSE_COLUMNS)

    def delete_entry(self, index):
        """Removes an entry

        Args:
            index (int): index of entry to remove
        """
        if 0 <= index < len(self.entries):
            self.entries = self.entries.drop(index).reset_index(drop=True)

    def get_entries(self):
        """Retrieves entries

        Returns:
            dataframe: Pandas dataframe with all available entries
        """
        return self.entries

    def set_entries(self, entries):
        """Overwrites and saves entries
        For use with data editor

        Args:
            entries (dataframe): new Pandas dataframe to save and write to db
        """
        self.entries = entries
        self.entries.to_sql(SQL_TABLE, self.engine, if_exists="replace", index=False)

    def add_entries(self, new_entries):
        """Adds set of entries

        Args:
            new_entries (dataframe): dataframe to append to preexisting data
        """
        self.entries = pd.concat([self.entries, new_entries], ignore_index=True)
