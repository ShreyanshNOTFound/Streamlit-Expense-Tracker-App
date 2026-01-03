# importing modules and files
import streamlit as st
from utils.constants import CATEGORIES
from services.api_client import get_expenses, get_expense_by_id, get_expenses_by_category, get_expenses_by_date

# code for track expenses page
st.set_page_config(page_title="Track Expenses", layout="centered")
st.title("📊Track Expenses")

# show all expenses
try:
    status_code, data = get_expenses()
    if status_code == 200:
        st.dataframe(data)
    else:
        st.error(data)
        
except Exception as e:
    st.error("Failed to establish a new connection. Please connect to the internet to see the Expenses.")

st.divider()

st.subheader("🪪Track Expense By ID")

# show expense of a given id
id = st.number_input(
    "ID [Unique identifier for each expense.]", min_value=1, value=None, placeholder="1", 
)
if st.button("Find Expense", type="primary", key="1"):
    
    # checking if the field is filled or not
    if not id:
        st.error("Please fill the ID field in order to track the information of the Expense.")
    else:
        try:
            status_code, data = get_expense_by_id(id)
            if status_code == 200:
                st.dataframe(data)
            else:
                st.error(data)
                
        except Exception as e:
            st.error("Failed to establish a new connection. Please connect to the internet to see the Expense.")

        
st.divider()    
    
st.subheader("🏷️Track Expense By Category")

# show expenses of a given category
category = st.selectbox(
    "Category [The category under the which the expense is classified, such as food, travel, or utilities.]",
    CATEGORIES,
)

if st.button("Find Expense", type="primary", key="2"):
    try:
        status_code, data = get_expenses_by_category(category)
        if status_code == 200:
            st.dataframe(data)
            
        else:
            st.error(data)
            
    except Exception as e:
        st.error("Failed to establish a new connection. Please connect to the internet to see the Expenses.")
        
    
    
st.divider()

    
st.subheader("🗓️Track Expense By Date")

# show expenses of a given date
date = st.date_input("Date [The date on which the exepense was made.]")

if st.button("Find Expense", type="primary", key="3"):
    try:
        status_code, data = get_expenses_by_date(str(date))
        if status_code == 200:
            st.dataframe(data)
            
        else:
            st.error(data)
            
    except Exception as e:
        st.error("Failed to establish a new connection. Please connect to the internet to see the Expenses.")