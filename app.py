import streamlit as st

if "page" not in st.session_state:
    st.session_state["page"] = "Sign In"

def change_page(page):
    st.session_state["page"] = page

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state.page == "Sign In":
    from views.signin import login
    login(change_page)

elif st.session_state.page == "Sign Up":
    from views.signup import signup
    signup(change_page)    

elif st.session_state.page == "authenticated":
    st.write("You are authenticated")
    from views.stock_analysis import stock_analysis
    stock_analysis()


