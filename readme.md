# Real Estate Investment Calculator

## Overview

The **Real Estate Investment Calculator** is a web application developed using Streamlit that helps investors analyze potential real estate investments. This app allows users to input various parameters related to property details, operating expenses, and additional inputs to calculate key financial metrics, including Net Sales Proceeds, Annual ROI, Unleveraged IRR, and Leveraged IRR.

## Features

- **Investment Calculator Page**: Users can input property details and operating expenses to calculate essential investment metrics.
- **Rent Roll Page**: Users can manage and calculate rental income from multiple properties dynamically.
- **Cash Flow Page**: A dashboard that summarizes cash flow calculations based on inputs from the Investment Calculator and Rent Roll pages.
- **Responsive Layout**: The application utilizes columns for a cleaner and more organized input layout.
- **Interactive Metrics**: Results are displayed dynamically as users input data.

## Technologies Used

- **Python**: The primary programming language for the application.
- **Streamlit**: A powerful framework for building interactive web applications.
- **Pandas**: For data manipulation and analysis.
- **Git**: Version control for tracking changes and collaborating.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/moonnstarr/RealEstateInvestmentCal.git
   cd RealEstateInvestmentCal

   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt

   ```

4. Run the Streamlit application:

   ```
   streamlit run app.py

   ```

5. Open your web browser and go below location to access the app
   ```
   http://localhost:8501
   ```

## Usage

Investment Calculator: Fill out the property details, operating expenses, and additional inputs. Click the "Calculate" button to view the results.

Rent Roll: Navigate to the Rent Roll page to enter details of multiple rental properties and see the calculated total rental income.

Cash Flow: Go to the Cash Flow page to view a summary of your cash flow metrics based on the inputs from the previous pages.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to create a pull request or open an issue.
License

## Acknowledgements

Streamlit for the awesome framework.
Pandas for data manipulation.

## Contact

For questions or feedback, please contact info@avionanalytics.com
