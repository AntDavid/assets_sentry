import streamlit as st
from utils.db import create_connection, add_user
from streamlit_extras.switch_page_button import switch_page


def signup():
    st.title("Sign Up")

    with st.form(key="signup_form"):
        name = st.text_input("Name")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_button = st.form_submit_button(label="Sign Up")
        login_button = st.form_submit_button(label="Sign In")

        if submit_button:
            if name and username and email and password and confirm_password:
                if password == confirm_password:
                    conn = create_connection("database.db")
                    user_id = add_user(conn, name, username, email, password)
                    st.success("Account created successfully")
                    switch_page("signin")

                else:
                    st.error("Passwords do not match")

            else:
                st.error("Please fill in all fields")

        if login_button:
            switch_page("signin")