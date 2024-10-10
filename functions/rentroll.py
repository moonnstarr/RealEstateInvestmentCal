import streamlit as st
import pandas as pd

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
