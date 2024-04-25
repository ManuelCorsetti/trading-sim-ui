"""
This module is the main entry point for the Streamlit web application.
It defines the necessary imports and configurations for the application,
sets up sidebar navigation for different pages and loads the selected 
page for user interaction.

Usage:
    Simply run this script with Streamlit to start the web application:
    
    $ streamlit run app.py
"""
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
