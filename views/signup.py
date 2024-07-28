import streamlit as st
from utils.db import create_connection, add_user
from streamlit_extras.switch_page_button import switch_page


def signup(change_page):
    st.title("Sign Up")
    page = None


    st.form(key="signup_form")
    name = st.text_input("Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    

    if st.button(label="Sign Up"):
        if name and username and email and password and confirm_password:
            if password == confirm_password:
                conn = create_connection("database.db")
                user_id = add_user(conn, name, username, email, password)
                st.success("Account created successfully")
                change_page("Sign In")
                st.experimental_rerun()
                
            else:
                st.error("Passwords do not match")

        else:
            st.error("Please fill in all fields")


    if st.button("Sign In"):
        change_page("Sign In")
        st.rerun()




       