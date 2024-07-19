import streamlit as st
from auth import check_password

def login():
    st.title("Sign In")

    with st.form(key = 'login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type = 'password')
        submit_button = st.form_submit_button(label = 'Sign In')

        if submit_button:
            st.session_state["Username"] = username
            st.session_state["Password"] = password

            if check_password(username, password):
                st.sucess("You are authenticated")
            
            else:
                st.error("Invalid username or password")
                st.stop()