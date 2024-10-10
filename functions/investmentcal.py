import streamlit as st
import pandas as pd

# Investment calculator page


def investment_calculator_page():
    # Title of the app
    st.title('Real Estate Investment Calculator')

    # Property Details - Input fields
    st.header('Property Details (Input fields)')

    # Create 4 columns for input fields
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        financing_option = st.selectbox("Financing Option", ["Loan", "Cash"])
        interest_only_payment_option = st.selectbox(
            "Interest Only Payment Option", ["Yes", "No"])
        interest_only_period = st.number_input(
            "Interest Only Period (Months)", value=12)

    with col2:
        ltv = st.number_input("Loan to Value (LTV)", value=70.0)
        annual_interest_rate = st.number_input(
            "Annual Interest Rate", value=6.0)
        amortization_period = st.number_input(
            "Amortization Period (years)", value=25)

    with col3:
        monthly_rental_income = st.number_input(
            "Monthly Rental Income", value=3000)
        square_foot = st.number_input("Square Foot", value=1000)
        current_rent_per_sqft = st.number_input(
            "Current Rent per Sqft", value=3.0)

    with col4:
        purchase_price = st.number_input(
            "Purchase Price of the Property", value=300000)
        general_vacancy = st.number_input("General Vacancy (%)", value=10)

    # OPEX - Input fields
    st.header('OPEX (Input fields)')

    # Create 4 columns for OPEX inputs
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        real_estate_taxes = st.number_input("Real Estate Taxes", value=10000)

    with col6:
        insurance = st.number_input("Insurance", value=1000)

    with col7:
        utilities = st.number_input("Utilities", value=2000)

    with col8:
        management_fee = st.number_input("Management Fee", value=1000)
        other_expenses = st.number_input("Other Expenses", value=0)

    # Additional Inputs
    st.header('Additional Inputs')

    # Create 4 columns for additional inputs
    col9, col10, col11, col12 = st.columns(4)

    with col9:
        potential_rent_sqft = st.number_input("Potential Rent/Sqft", value=5.0)

    with col10:
        cap_rate = st.number_input("Cap Rate (%)", value=8.0)

    with col11:
        renewal_rent_sqft = st.number_input("Renewal Rent/Sqft", value=4.0)

    with col12:
        growth_rate_income = st.number_input(
            "Growth Rate of Income (%)", value=3.0)
        growth_rate_expense = st.number_input(
            "Growth Rate of Expense (%)", value=2.0)

    # Calculations
    st.header("Results")

    # Create 4 columns for results display
    res_col1, res_col2, res_col3, res_col4 = st.columns(4)

    if st.button("Calculate"):
        # Net Sales Proceed (5 Years)
        net_sales_proceed = purchase_price * \
            (1 + (growth_rate_income / 100)) ** 5 * (1 - general_vacancy / 100)
        res_col1.metric("Net Sales Proceed (5 Years)",
                        f"${net_sales_proceed:,.2f}")

        # Annual ROI Calculation
        annual_roi = (monthly_rental_income * 12) / purchase_price * 100
        res_col2.metric("Annual ROI", f"{annual_roi:.2f}%")

        # Unleveraged IRR Calculation
        unleveraged_irr = (annual_roi + cap_rate) / 2
        res_col3.metric("Unleveraged IRR", f"{unleveraged_irr:.2f}%")

        # Leveraged IRR Calculation (simplified)
        leveraged_irr = unleveraged_irr * (1 + ltv / 100)
        res_col4.metric("Leveraged IRR", f"{leveraged_irr:.2f}%")

        # Showing final results
        st.success(
            f"Leverage IRR: {leveraged_irr:.2f}% | Unleveraged IRR: {unleveraged_irr:.2f}% | Net Sales Proceed: ${net_sales_proceed:,.2f} | Annual ROI: {annual_roi:.2f}%")

        # Store results in session state
        st.session_state['net_sales_proceed'] = net_sales_proceed
        st.session_state['annual_roi'] = annual_roi
        st.session_state['unleveraged_irr'] = unleveraged_irr
        st.session_state['leveraged_irr'] = leveraged_irr
        st.session_state.monthly_rental_income = monthly_rental_income
        st.session_state.general_vacancy = general_vacancy

    # (Insert the investment calculator code here)
    pass  # Placeholder for the investment calculator code
