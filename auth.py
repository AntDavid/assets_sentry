import streamlit as st
from utils.db import create_connection, verify_user

def check_password():
    def password_entered():
        username = st.session_state["username"]
        password = st.session_state["password"]
        
        if not username or not password:
            st.error("Please enter your username and password")
            return

        conn = create_connection("database.db")
        user = verify_user(conn, username, password)

        if user:
            st.session_state["authenticated"] = True
            st.session_state["page"] = "analysis"
            del st.session_state["password"]
        else:
            st.session_state["authenticated"] = False
            st.error("Invalid username or password")

    if "authenticated" in st.session_state and st.session_state["authenticated"]:
        return True

    if "username" in st.session_state and "password" in st.session_state:
        password_entered()
        return st.session_state["authenticated"]

    return False
