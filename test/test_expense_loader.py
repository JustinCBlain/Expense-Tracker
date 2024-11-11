"""Test expense loading"""

import os
from src.tabs.expensecolumn import process_file

def test_expense_loader():
    """Test that data will be loaded properly"""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(this_dir, os.pardir, 'sample_data/small_data.csv')

    df = process_file(filepath)
    assert df.shape[0] == 5
    assert set(df.columns.to_list()) == {"Date", "Time", "Category", "Vendor", "Amount"}
