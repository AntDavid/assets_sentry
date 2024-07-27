import streamlit as st
import datetime as dt
from utils.finance import download_stock_data, calculate_metrics

def stock_analysis():
    st.title('Stock Market Analysis')
    
    end_date = dt.date.today()
    start_date = dt.datetime(end_date.year - 1, end_date.month, end_date.day)
    with st.container():
        st.header("Enter the requested information bellow:")
        col_one, col_two, col_three = st.columns(3)

        with col_one:
            selected_stock = st.selectbox("select stock:", options=['PETR4.SA', 'VALE3.SA', 'MGLU3.SA', 'BOVA11.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'WEGE3.SA', 'VVAR3.SA', 'B3SA3.SA', 'LREN3.SA', 'GNDI3.SA', 'NTCO3.SA', 'RENT3.SA', 'BBAS3.SA', 'PETR3.SA', 'CSNA3.SA', 'IRBR3.SA', 'CIEL3.SA', 'BRFS3.SA', 'USIM5.SA', 'GGBR4.SA', 'ELET3.SA', 'ELET6.SA', 'CMIG4.SA', 'CVCB3.SA', 'AZUL4.SA', 'BTOW3.SA', 'HAPV3.SA', 'CYRE3.SA', 'MRFG3.SA', 'BRML3.SA', 'BRPR3.SA', 'BRKM5.SA', 'BRAP4.SA', 'BRDT3.SA', 'BRFS3.SA', 'BRKM5.SA', 'BRML3.SA', 'BRPR3'])

        with col_two:
            selected_start_date = st.date_input("Start date:", start_date)

        with col_three:
            selected_end_date = st.date_input("End date:", end_date)

    dataframe = download_stock_data(selected_stock, selected_start_date, selected_end_date)

    if not dataframe.empty:
        last_update, last_quote, first_quote, min_quote, max_quote, change = calculate_metrics(dataframe)

        with col_one:
            st.metric(f"Last Update - {last_update}", "R$ {:,.2f}".format(last_quote), f"{change}%")

        with col_two:
            st.metric("Highest price of the period", "R$ {:,.2f}".format(max_quote))

        with col_three:
            st.metric("Lowest price of the period", "R$ {:,.2f}".format(min_quote))

        with st.container():
            st.area_chart(dataframe[["Adj Close"]])
            st.line_chart(dataframe[['Low', 'High', 'Adj Close']])
    
    
    else:
        st.warning("No data avaliable for the selected stock and date range")
