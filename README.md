# Budget vs. Actual Variance Analysis Dashboard

This project provides an interactive web-based dashboard for financial variance analysis, built using Python and the Dash framework. It allows users to quickly compare budgeted figures against actuals, calculate variances, and visually identify significant discrepancies.

## Key Features

* **Data Loading:** Reads budget and actual data from CSV files.
* **Variance Calculation:** Computes absolute and percentage variances.
* **Significant Variance Flagging:** Automatically flags variances exceeding a predefined percentage threshold.
* **Interactive Data Table:** Displays all relevant financial data in a sortable and searchable table.
* **Visual Highlighting:** Uses conditional formatting to highlight flagged significant variances in red.

## How to Run This Dashboard

To get this dashboard up and running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/your-repo-name.git](https://github.com/YourGitHubUsername/your-repo-name.git)
    cd your-repo-name
    ```
    *(Remember to replace `YourGitHubUsername/your-repo-name.git` with the actual URL of your GitHub repository.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare Data:**
    * Ensure you have your `budget_data.csv` and `actual_data.csv` files in the root directory of the project. These files should have a common 'Line Item' column.

5.  **Run the Application:**
    ```bash
    python dashboard.py
    ```

6.  **Access the Dashboard:**
    Open your web browser and navigate to the address displayed in your terminal (usually `http://127.0.0.1:8050/`).

## Dependencies

This project requires the following Python libraries:
* `dash`
* `pandas`

*(These are automatically listed and installed from `requirements.txt`.)*

## Data Structure Expectation

`budget_data.csv` and `actual_data.csv` should typically have columns like:
* `Line Item` (for merging and identification)
* `Budget` (in `budget_data.csv`)
* `Actual` (in `actual_data.csv`)
* *(Other relevant columns as per your financial data)*