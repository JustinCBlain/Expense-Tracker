import pandas as pd

class ExpenseManager:
    def __init__(self):
        self.entries = pd.DataFrame(columns=["Date", "Category", "Description", "Cost"])

    def add_entry(self, date, category, description, cost):
        # Create a new entry DataFrame
        new_entry = pd.DataFrame({"Date": [date], "Category": [category], "Description": [description], "Cost": [cost]})

        # Only concatenate if new_entry is not empty and has valid data
        if not new_entry.empty and new_entry.notna().any(axis=None):
            self.entries = pd.concat([self.entries, new_entry], ignore_index=True)

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries = self.entries.drop(index).reset_index(drop=True)

    def get_entries(self):
        return self.entries
