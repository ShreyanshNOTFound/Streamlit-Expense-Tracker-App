# importing modules and files
import streamlit as st
from services.api_client import about_api

# code for homepage
st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("🔍Expense Tracker App")
st.write(
    """Expense Tracker App is a Streamlit-based frontend application that allows users to add, view, and manage their daily expenses through a FastAPI-powered backend. It provides a simple and interactive interface for tracking spending, categorizing expenses, and maintaining organized financial records."""
)

try:
    st.subheader("🚀About Expense Tracker API")
    about_api_data = about_api()
    st.write(about_api)
    
except Exception as e:
    st.error("Failed to establish a new connection. Please connect to the internet to know about the API.")


st.subheader("📒How To Use The App?")
st.write("Use the sidebar to navigate through the app and use our services.")