import streamlit as st
from auth import check_password
from utils.db import create_connection, creat_table


conn = create_connection("database.db")
creat_table(conn)

if check_password():
    st.write("You are authenticated")
    st.text("You can now access the stock analysis page")
    page = st.sidebar.selectbox("Select a page", ["Stock Analysis"])
    if page == "Stock Analysis":
        from pages.stock_analysis import stock_analysis
        stock_analysis()

    else:
        st.warning("Invalid username or password. Try again")
        st.stop()
