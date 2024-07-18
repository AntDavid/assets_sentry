import streamlit as st
from utils.db import create_connection, verify_user

def check_password():
    def password_entered():
        username = st.session_state["username"]
        password = st.session_state["password"]

        conn = create_connection("data.db")
        user = verify_user(conn, username, password)

        if user:
            st.session_state["authenticated"] = True
            del st.session_state["password"]
        
        else:
            st.session_state["authenticated"] = False
            st.error("Invalid username or password")


        if st.session_state["authenticated"]:
            return True
        
        else:
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input("Password", on_change=password_entered, key="password", type="password")
            return False