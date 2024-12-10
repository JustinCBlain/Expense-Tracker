import streamlit as st
import pandas as pd

from src.util.constants import EXPENSE_COLUMNS

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""


def show_login():
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title('Expense Tracker')
        st.subheader('Login')
        with st.form('Login'):
            user = st.text_input('Email')
            password = st.text_input('Password', type="password")
            submit = st.form_submit_button('Login!')

        if submit:
            if (user == "Mary" or "Justin") and password == "c4tes":
                st.session_state.logged_in = True
                st.session_state.username = user

                user_data = f"{st.session_state.username}_data"
                if user_data not in st.session_state:
                    st.session_state[user_data] = pd.DataFrame(
                        columns=EXPENSE_COLUMNS)
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

def navbar():
    with st.sidebar:
        st.subheader(st.session_state.username)

    # Save to user specific .csv
    if st.sidebar.button("Save"):
        with st.spinner("Processing"):
            user_data = f"{st.session_state.username}_data"
            editing = st.session_state.editing
            st.session_state[user_data] = editing
            st.success("You have saved your expenses to the database successfully")

    # Logout
    if st.sidebar.button("Logout"):
        logout()
        # TODO Clear entries

    # Delete local and server data
    if st.sidebar.button("Clear Data"):
        # TODO Clear entries
        # TODO delete csv
        pass

    # Delete all user data
    if st.sidebar.button("Delete Account"):
        # TODO Clear entries
        # TODO delete csv
        # TODO Delete user logon
        pass

# Resets user state
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""


    """import streamlit as st
from secrets import compare_digest

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

users = {
    "Lou": "Wilson",
    "Brennan": "LeeMulligan",
    "Abria": "Iyangar",
    "Erika": "Ishii"
}


def show_login():

    st.title("Login")

    with st.form('Login'):
        user = st.text_input('Email')
        password = st.text_input('Password', type="password")
        submit = st.form_submit_button('Engage!', icon="🛰️")

    if submit:
        if user in users.keys():
            if compare_digest(password, users[user]):
                st.success('Welcome back, ' + user, icon="👍")
                st.session_state.logged_in = True
                global session
                session = user
                st.switch_page(st.Page(layout.show_layout))
            else:
                st.error('You forgot again, ' + user, icon="👎")
        else:
            new_user(user, password)


def new_user(user, password):
    with st.form('New friend?'):
        pw_confirm = st.text_input('Confirm?', type="password")
        new_user = st.form_submit_button('Spawn!', icon="🤛")

    if new_user:
        if compare_digest(pw_confirm, password):
            st.success('Did we just become best friends?', icon="🤝")
            # add user
            # sign in
        else:
            st.error('That\'s not what you said before!', icon="👎")


# st.info(session)
if session != "":
    st.switch_page(st.Page(layout.show_layout))


st.sidebar
st.rerun - (loigout)
"""