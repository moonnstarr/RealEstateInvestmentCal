import streamlit as st
import pandas as pd


# Function definitions for each page

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


# Rent Roll Page
def rent_roll_page():
    st.title('Rent Roll')

    # Create input fields for the rent roll
    st.header('Rent Roll Inputs')

    # Create 4 columns for rent roll inputs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        unit_number = st.number_input("Unit Number", min_value=1, value=1)
        number_of_units = st.number_input("Number of Units", value=1)
        monthly_rent = st.number_input("Monthly Rent for Unit", value=1000.0)

    with col2:
        square_footage = st.number_input("Square Footage", value=1000)
        current_rent_per_sqft = st.number_input(
            "Current Rent per Sqft", value=3.0)
        potential_rent_per_sqft = st.number_input(
            "Potential Rent/Sqft", value=5.0)

    with col3:
        tenant_name = st.text_input("Tenant Name")
        lease_start_date = st.date_input("Lease Start Date")

    with col4:
        lease_end_date = st.date_input("Lease End Date")
        vacancy_status = st.selectbox("Vacancy Status", ["Occupied", "Vacant"])
        notes = st.text_area("Notes", "")

    # Add to Rent Roll button
    if st.button("Add to Rent Roll"):
        rent_roll_data = {
            "Unit Number": unit_number,
            "Number of Units": number_of_units,
            "Monthly Rent": monthly_rent,
            "Current Rent per Sqft": current_rent_per_sqft,
            "Potential Rent/Sqft": potential_rent_per_sqft,
            "Tenant Name": tenant_name,
            "Lease Start Date": lease_start_date,
            "Lease End Date": lease_end_date,
            "Vacancy Status": vacancy_status,
            "Notes": notes,
        }

        # Convert the dictionary to a DataFrame
        new_entry = pd.DataFrame([rent_roll_data])

        # Initialize session state for rent roll if it doesn't exist
        if 'rent_roll' not in st.session_state:
            st.session_state.rent_roll = pd.DataFrame(
                columns=rent_roll_data.keys())

        # Concatenate the new entry to the existing DataFrame
        st.session_state.rent_roll = pd.concat(
            [st.session_state.rent_roll, new_entry], ignore_index=True)

    # Display the rent roll as a report
    if 'rent_roll' in st.session_state and not st.session_state.rent_roll.empty:
        st.subheader("Rent Roll Report")

        # Formatting the monetary values
        rent_roll_report = st.session_state.rent_roll.copy()
        rent_roll_report['Monthly Rent'] = rent_roll_report['Monthly Rent'].apply(
            lambda x: "${:,.2f}".format(x) if pd.notnull(x) else "$0.00")
        rent_roll_report['Current Rent per Sqft'] = rent_roll_report['Current Rent per Sqft'].apply(
            lambda x: "${:,.2f}".format(x) if pd.notnull(x) else "$0.00")
        rent_roll_report['Potential Rent/Sqft'] = rent_roll_report['Potential Rent/Sqft'].apply(
            lambda x: "${:,.2f}".format(x) if pd.notnull(x) else "$0.00")

        # Display the DataFrame without index
        st.dataframe(rent_roll_report)

    # Display total potential income
    if 'rent_roll' in st.session_state and not st.session_state.rent_roll.empty:
        # Ensure the column is converted to string for calculation
        monthly_rent_values = rent_roll_report['Monthly Rent'].str.replace(
            '$', '').str.replace(',', '')
        number_of_units_values = st.session_state.rent_roll['Number of Units'].astype(
            float)

        total_potential_income = (monthly_rent_values.astype(
            float) * number_of_units_values).sum()
        st.metric("Total Potential Monthly Income",
                  f"${total_potential_income:,.2f}")

    pass  # Placeholder for the rent roll code


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
