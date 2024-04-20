# app.py
import streamlit as st
from pages import landing, result

PAGES = {
    "Landing": landing,
    "Results": result,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()

