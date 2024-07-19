import streamlit as st
from auth import check_password

def login():
    st.title("Sign In")

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Sign In"):
        if check_password():
            st.success("You are authenticated")
        else:
            st.warning("Invalid username or password")
