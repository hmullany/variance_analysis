# Budget vs. Actual Variance Analysis Dashboard

This project is a Python-based dashboard that displays the variance between budget and actual financial performance. It uses the Dash framework to create an interactive table and highlights significant variances for easy identification.

## Key Features

* Displays budget, actual, and variance data in a tabular format.
* Highlights significant variances with a red background.
* Uses CSV files for input data.

## How to Run

1.  Clone this repository.
2.  Create a virtual environment (optional): `python -m venv venv`
3.  Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) / `venv\Scripts\activate` (Windows)
4.  Install dependencies: `pip install dash pandas`
5.  Place `budget_data.csv` and `actual_data.csv` in the same directory as `dashboard.py`.
6.  Run the application: `python dashboard.py`
7.  Open your browser to the displayed address.

## Dependencies

* Dash
* Pandas

## Data Files

* `budget_data.csv`: Contains budget data.
* `actual_data.csv`: Contains actual performance data.
