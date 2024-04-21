# app.py
import streamlit as st
from pages import landing, result

# st.set_page_config(page_title="POC: Visualize Strategy Performance", page_icon="📈")


PAGES = {
    "Landing": landing,
    "Results": result,
}

st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# page = PAGES[selection]
# page.app()

