# importing modules and files
import streamlit as st
from services.api_client import delete_expense

# code for delete expense page
st.set_page_config(page_title="Delete Expense", layout="centered")
st.title("⛔Delete Expense")

# field for expense data
id = st.number_input(
    "ID [Unique identifier for each expense.]", min_value=1, value=None, placeholder="1"
)
if st.button("Delete Expense", type="primary"):
    
    # checking if the field is filled or not
    if not id:
        st.error("Please fill the ID field in order to delete the expense.")
    else:
        try:
            status_code, data = delete_expense(id)
            if status_code == 204:
                st.success(data)
            else:
                st.error(data)
                
        except Exception as e:
            st.error("Failed to establish a new connection. Please connect to the internet to delete the Expense.")