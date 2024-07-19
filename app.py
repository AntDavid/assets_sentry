import streamlit as st

st.write("Welcome to Stock Analysis App")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.sidebar.write("Please, select a page to continue")
    page = st.sidebar.selectbox("Select a page", ["Sign In", "Sign Up"])

    if page == "Sign In":
        from pages.signin import login
        login()
    elif page == "Sign Up":
        from pages.signup import signup
        signup()
else:
    st.write("You are authenticated")
    st.text("You can now access the stock analysis page")
    page = st.sidebar.selectbox("Select a page", ["Stock Analysis"])
    if page == "Stock Analysis":
        from pages.stock_analysis import stock_analysis
        stock_analysis()
