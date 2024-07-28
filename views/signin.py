import streamlit as st
from auth import check_password
from streamlit_extras.switch_page_button import switch_page

def login(change_page):
    st.title("Sign In")

    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")
    
    col_one, col_two = st.columns(2)

    with col_one:
        if st.button("Sign In", use_container_width = True):
            if check_password():
                st.success("You are authenticated")
                st.session_state["authenticated"] = True
                change_page("authenticated")
                st.rerun()

            else:
                st.warning("Invalid username or password")
                st.experimental_rerun()
  
    with col_two:
        if st.button("Sign Up", use_container_width = True):
            change_page("Sign Up")
            st.rerun()
                

