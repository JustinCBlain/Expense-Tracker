"""Tests for the expense manager class"""

from unittest.mock import MagicMock
import pandas as pd
from src.util.constants import DATE_COL, SQL_TABLE
from src.expense_manager import ExpenseManager


sample_one = [
    {
        "Date": "2024-11-10",
        "Category": "Grocery",
        "Amount": 20.5
    }
]

sample_two = [
    {
        "Date": "2024-11-10",
        "Category": "Grocery",
        "Amount": 20.5
    },
    {
        "Date": "2024-11-1",
        "Category": "Retail",
        "Amount": 15.5
    }

]

def test_set_entries():
    """Test setting entries"""
    # Simulate an existing database table with data
    mock_engine = MagicMock()

    # Initialize ExpenseManager
    manager = ExpenseManager()
    manager.engine = mock_engine

    # Simulate new entries DataFrame
    new_entries = pd.DataFrame(sample_one)
    new_entries[DATE_COL] = pd.to_datetime(new_entries[DATE_COL])

    mock_to_sql = MagicMock()
    new_entries.to_sql = mock_to_sql

    # Set new entries
    manager.set_entries(new_entries)

    # Assert that to_sql was called to save the new data
    mock_to_sql.assert_called_once_with(SQL_TABLE, mock_engine, if_exists="replace", index=False)
    assert manager.entries.shape[0] == 1
    assert manager.entries.iloc[0][DATE_COL].date() == pd.to_datetime("2024-11-10").date()


def test_delete_entry():
    """Test deleting an entry"""
    # Simulate some entries
    manager = ExpenseManager()
    manager.entries = pd.DataFrame(sample_two)
    manager.entries[DATE_COL] = pd.to_datetime(manager.entries[DATE_COL])

    # Delete the first entry
    manager.delete_entry(0)

    # Verify the deletion
    assert manager.entries.shape[0] == 1
    assert manager.entries.iloc[0][DATE_COL].date() == pd.to_datetime("2024-11-1").date()


def test_get_entries():
    """Test getting entries"""
    # Simulate ExpenseManager with some entries
    manager = ExpenseManager()
    manager.entries = pd.DataFrame(sample_one)
    manager.entries[DATE_COL] = pd.to_datetime(manager.entries[DATE_COL])

    # Get the entries
    entries = manager.get_entries()

    # Verify the entries
    assert entries.shape[0] == 1

    assert entries.iloc[0][DATE_COL].date() == pd.to_datetime("2024-11-10").date()


def test_add_entries():
    """Test adding entries"""
    manager = ExpenseManager()
    manager.entries = pd.DataFrame(sample_one)
    manager.entries[DATE_COL] = pd.to_datetime(manager.entries[DATE_COL])

    # Simulate new entries to add
    new_entries = pd.DataFrame(sample_two)
    new_entries[DATE_COL] = pd.to_datetime(new_entries[DATE_COL])

    # Add the new entries
    manager.add_entries(new_entries)

    # Check if the new entries are added
    assert manager.entries.shape[0] == 3
    assert manager.entries.iloc[2][DATE_COL].date() == pd.to_datetime("2024-11-1").date()
