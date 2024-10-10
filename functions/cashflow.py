import streamlit as st
import pandas as pd

# Cash Flow Page


def cashflow_page():
    # Title of the page
    st.title('Cash Flow Dashboard')

    # Check if the Investment Calculator values are set in the session state
    if 'monthly_rental_income' not in st.session_state or 'general_vacancy' not in st.session_state:
        st.warning("Please complete the Investment Calculator page first.")
        return

    # Retrieve the monthly rental income and general vacancy from session state
    monthly_rental_income = st.session_state.get('monthly_rental_income', 0)
    general_vacancy = st.session_state.get('general_vacancy', 0)

    # Input fields for Cash Flow calculations
    st.header('Cash Flow Inputs')

    # Create columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        gross_potential_revenue = st.number_input(
            "Gross Potential Revenue",
            value=monthly_rental_income * 12,
            key='gross_potential_revenue'
        )
        absorption_vacancy = st.number_input(
            "Absorption and Turnover Vacancy (%)",
            value=10,
            key='absorption_vacancy'
        )

    with col2:
        operating_expenses = st.number_input(
            "Operating Expenses",
            value=15000,
            key='operating_expenses'
        )

    with col3:
        principal_debt_payment = st.number_input(
            "Principal Debt Payment",
            value=1000,
            key='principal_debt_payment'
        )
        interest_payment = st.number_input(
            "Interest Payment",
            value=500,
            key='interest_payment'
        )

    # Calculate Effective Gross Revenue
    effective_gross_revenue = gross_potential_revenue * \
        (1 - (absorption_vacancy / 100)) * (1 - (general_vacancy / 100))

    # Calculate Net Operating Income
    net_operating_income = effective_gross_revenue - operating_expenses

    # Cash Flow After Debt Service
    cash_flow_after_debt_service = net_operating_income - \
        (principal_debt_payment + interest_payment)

    # Display the results
    st.header("Cash Flow Results")

    # Create columns for results display
    res_col1, res_col2, res_col3 = st.columns(3)

    with res_col1:
        st.metric("Effective Gross Revenue",
                  f"${effective_gross_revenue:,.2f}")

    with res_col2:
        st.metric("Net Operating Income", f"${net_operating_income:,.2f}")

    with res_col3:
        st.metric("Cash Flow After Debt Service",
                  f"${cash_flow_after_debt_service:,.2f}")


pass  # Placeholder for the Cashflow code code
