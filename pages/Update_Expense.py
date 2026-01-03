# importing modules and files
import streamlit as st
from utils.constants import CATEGORIES
from services.api_client import update_expense

# code for update expense page
st.set_page_config(page_title="Update Expense", layout="centered")
st.title("🛠️Update Expense")

st.subheader("Mandatory Field")

# fields for expense data
id = st.number_input(
    "ID [Unique identifier for each expense.]", min_value=1, value=None, placeholder="1"
)

st.divider()

st.subheader("Optional Fields")

amount = st.number_input(
    "Amount (in ₹) [The amount of money spent in a single transaction (in ₹).]",
    min_value=1,
    value=None,
    placeholder="1999",
)

category = st.selectbox(
    "Category [The category under the which the expense is classified, such as food, travel, or utilities.]",
    CATEGORIES,
)

description = st.text_input(
    "Description [An optional short note describing the purpose of the expense.]",
    placeholder="Lunch at canteen",
)

date = st.date_input("Date [The date on which the exepense was made.]")

if st.button("Update Expense", use_container_width=True, type="primary"):
    
    # checking if the field is filled or not
    if not id:
        st.error("Please fill the ID field in order to make changes to your Expense.")
    else:
        
        # preparing the data 
        data = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": str(date)
        }
        
        # filtering data based on emptiness
        new_data = {}
        for key, value in data.items():
            if value != None and value != "":
                new_data[key] = value
                
        try:
            status_code, data = update_expense(id, new_data) 
            if status_code == 202:
                st.success(data)
            else:
                st.error(data)
        
        except:
            st.error("Failed to establish a new connection. Please connect to the internet to update the Expense.")