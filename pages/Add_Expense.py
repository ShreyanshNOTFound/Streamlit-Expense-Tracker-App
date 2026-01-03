# importing modules and files
import streamlit as st
from utils.constants import CATEGORIES
from services.api_client import add_expense

# code for add expense page
st.set_page_config(page_title="Add Expense", layout="centered")
st.title("✍️Add Expense")

# fields for expense data
id = st.number_input(
    "ID [Unique identifier for each expense.]", min_value=1, value=None, placeholder="1"
)

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

if st.button("Add Expense", use_container_width=True, type="primary"):

    # checking if all fields are filled or not
    if not (id and amount and category and date):
        st.error("Please fill all the missing fields.")
    else:
        # preparing the data
        payload = {
            "id": id,
            "amount": amount,
            "category": category,
            "description": description,
            "date": str(date),
        }
        try:
            status_code, data = add_expense(payload)
            if status_code == 201:
                st.success(data)
            else:
                st.error(data)
                
        except Exception as e:
            st.error("Failed to establish a new connection. Please connect to the internet to add the Expense.")
