import pytest
from streamlit.testing.v1 import AppTest

@pytest.fixture
def my_app(scope="session"):
    at = AppTest.from_file("src/app.py")
    at.run()
    return at
