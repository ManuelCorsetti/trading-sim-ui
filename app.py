import yfinance as yf
import pandas as pd
import streamlit as st
import datetime as dt
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Treat columns with < 10 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    _min,
                    _max,
                    (_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    return df

st.title("Simple Trading Simulator")
"Use the table below as reference to find the ticker names for your chosen stocks."

# Load Tickers
tickers = pd.read_csv("./data/ticker_names/nasdaq-symbols.txt", sep='\t')
tickers_list = tickers['Symbol'].tolist()

st.dataframe(filter_dataframe(tickers))

# with st.container():
selected_ticker = st.multiselect("Select Tickers", tickers_list)

# Display selected tickers with an input box beside them
"##### $ value that you would like to invest on each ticker:"
investment_amount = {}
for ticker in selected_ticker:
    investment_amount[ticker] = st.text_input(f"$ {ticker}", "")
    
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
st.write(profit)
profit_pct = profit / (start_price * value)
# Visualize Profit
st.line_chart(data['Close'])
st.write(f"Overall profit: {(profit):.2f}")
st.write(f"Overall profit (%): {profit_pct:.2%}")

# Visualize File Profits
if st.button("Generate Profit File"):
    profit_df = pd.DataFrame([{"ticker": selected_ticker, "profit": profit}])
    profit_df.to_csv('profits.csv', index=False)
    st.success('Profit file has been generated!')
