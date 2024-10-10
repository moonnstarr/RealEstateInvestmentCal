import streamlit as st
import pandas as pd
from functions import rentroll
from functions import cashflow
from functions import investmentcal


# Function definitions for each page

# Investment calculator page
def investment_calculator_page():
    investmentcal.investment_calculator_page()
    pass  # Placeholder for the investment calculator code


# Rent Roll Page
def rent_roll_page():
    rentroll.rent_roll_page()
    pass  # Placeholder for the rent roll code


# Cash Flow Page
def cashflow_page():
    cashflow.cashflow_page()
    pass  # Placeholder for the Cashflow code code


# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Page", ["Investment Calculator", "Rent Roll", "Cash Flow"])


# Display the selected page
if page == "Investment Calculator":
    investment_calculator_page()
elif page == "Rent Roll":
    rent_roll_page()
elif page == "Cash Flow":
    cashflow_page()
