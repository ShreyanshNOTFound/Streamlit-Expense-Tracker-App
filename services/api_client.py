# importing modules and files
import requests
from config.config import API_URL
from utils.pandas_objects_validator import dataframe_validator, series_validator 

# a function to call the home endpoint
def about_api() -> str:
    # preparing the endpoint
    endpoint = f"{API_URL}/about"

    # fetching the response
    return requests.get(endpoint).json()["message"]

# a function to create a new expense
def add_expense(payload: dict) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/add_expense"

    # fetching the response
    response = requests.post(endpoint, json=payload).json()

    if response.get("message"):
        return (201, response.get("message"))

    return (400, response.get("detail"))

# a function to update an expense of given id
def update_expense(id: int, payload: dict) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/update_expense/{id}"

    # fetching the response
    response = requests.put(endpoint, json=payload).json()

    if response.get("message"):
        return (202, response.get("message"))

    return (404, response.get("detail"))

# a function to get all expenses
def get_expenses() -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/get_expenses"

    # fetching the response
    response = requests.get(endpoint).json()

    if not response.get("detail"):
        # prepairng df
        df = dataframe_validator(response)

        return (200, df)
    
    return (404, response["detail"])

# a function to get an expense of given id
def get_expense_by_id(id: int) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/get_expense/{id}"

    # fetching the response
    response = requests.get(endpoint).json()

    if not response.get("detail"):
        # prepairng series
        series = series_validator(response)

        return (200, series)

    return (404, response["detail"])

# a function to get all expenses of given category
def get_expenses_by_category(category: str) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/get_expenses_by_category/{category}"

    # fetching the response
    response = requests.get(endpoint).json()

    if not response.get("detail"):
        # prepairng df
        df = dataframe_validator(response)
        
        return (200, df)

    return (404, response["detail"])

# a function to get all expenses of given date
def get_expenses_by_date(date: str) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/get_expenses_by_date/{date}"

    # fetching the response
    response = requests.get(endpoint).json()

    if not response.get("detail"):
        # prepairng df
        df = dataframe_validator(response)

        return (200, df)

    return (404, response["detail"])

# a function to delete an expense of given id
def delete_expense(id: int) -> tuple:
    # preparing the endpoint
    endpoint = f"{API_URL}/delete_expense/{id}"

    # fetching the response
    response = requests.delete(endpoint).json()
    
    if response.get("message"):
        return (200, response.get("message"))
    
    return (404, response.get("detail"))