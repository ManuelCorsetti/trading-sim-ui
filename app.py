import yfinance as yf
import pandas as pd
import streamlit as st
import datetime as dt

st.title("Simple Trading Simulator")

# Load Tickers
tickers = pd.read_csv("./data/nasdaq-symbols.txt", sep='\t')

st.dataframe(tickers)

# search_term = st.text_input('Search', '')
# filtered_data = tickers[tickers['Security Name'].str.contains(search_term)]
# selected_data = filtered_data.iloc[selected_rows]
# selection = st.table(selected_data)


tickers_list = tickers['Symbol'].tolist()

# with st.container():
# Select Ticker
selected_ticker = st.selectbox("Select Ticker", tickers_list)

# Enter Stock Value
value = st.number_input("Enter Stock Value", min_value=1)

# with st.container():
# Select Trading Start and End Date
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Trading Start Date", value=dt.date.today() - dt.timedelta(days=365))

with col2:
    end_date = st.date_input("Trading End Date", value=dt.date.today())

# Get Stock Data and Calculate Profit
data = yf.download(selected_ticker, start=start_date, end=end_date)
start_price = data.iloc[0]['Close']
end_price = data.iloc[-1]['Close']

profit = (end_price - start_price) * value

# Visualize Profit
st.line_chart(data['Close'])
st.write(f"Overall profit: {profit}")

# Visualize File Profits
if st.button("Generate Profit File"):
    profit_df = pd.DataFrame([{"ticker": selected_ticker, "profit": profit}])
    profit_df.to_csv('profits.csv', index=False)
    st.success('Profit file has been generated!')
