import streamlit as st
from auth import check_password
from streamlit_extras.switch_page_button import switch_page

def login():
    st.title("Sign In")

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Sign In"):
        if check_password():
            st.success("You are authenticated")
            switch_page("stock analysis")

            
        else:
            st.warning("Invalid username or password")
            st.rerun()
            
    if st.button("Sign Up"):
        switch_page("Sign Up")
