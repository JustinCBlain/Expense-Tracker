"""
Tests main app - ensures it starts up correctly and is laid out
as expected.
"""

from unittest.mock import Mock
import pandas as pd


def test_layout(my_app):
    """Tests general layout and functionality"""

    assert not my_app.exception
    assert my_app.title[0].value == "Application Title"

    # Assert that the first column is "Expenses"
    expense_column = my_app.columns[0]
    assert expense_column.header[0].value == "Expenses"

    vis_column = my_app.columns[1]
    assert vis_column.header[0].value == "Visualizations"


def test_save(my_app):
    """Tests the save button"""

    expense_column = my_app.columns[0]
    # Assert that the "save" button works correctly
    my_loader = Mock()
    my_loader.return_value = pd.DataFrame(columns=[])
    my_app.session_state.expense_manager = Mock()
    my_app.session_state.expense_manager.get_entries = my_loader
    expense_column.button[0].click().run()
    my_loader.assert_called()
    assert my_app.success[0].value == "You have saved your expenses to the database successfully"
