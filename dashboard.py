import dash
from dash import html
from dash import dash_table
import pandas as pd

# 1. Load and Process Your Data
def load_data(file_path):
    """Loads data from a CSV file into a Pandas DataFrame."""
    try:
        local_df = pd.read_csv(file_path)
        return local_df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def align_data(budget_df_in, actual_df_in, key_column='Line Item'):
    """Merges budget and actual dataframes based on a common key column."""
    merged_df_local = pd.merge(budget_df_in, actual_df_in, on=key_column, how='outer')
    return merged_df_local

def calculate_variances(merged_df_in):
    """Calculates the absolute and percentage variances."""
    if 'Budget' in merged_df_in.columns and 'Actual' in merged_df_in.columns:
        merged_df_local = merged_df_in.copy()
        merged_df_local['Variance (Absolute)'] = merged_df_local['Actual'] - merged_df_local['Budget']
        merged_df_local['Variance (%)'] = (merged_df_local['Variance (Absolute)'] / merged_df_local['Budget']) * 100
        return merged_df_local
    else:
        print("Error: 'Budget' and 'Actual' columns are required for variance calculation.")
        return merged_df_in.copy()

def flag_significant_variances(variance_df_in, pct_threshold):
    """Flags significant variances based on a percentage threshold."""
    variance_df_local = variance_df_in.copy()
    variance_df_local['Significant Variance'] = False
    variance_df_local['Variance Note'] = ''
    if 'Variance (%)' in variance_df_local.columns and 'Budget' in variance_df_local.columns:
        for index, row in variance_df_local.iterrows():
            pct_var = row['Variance (%)']
            budget = row['Budget']
            if pd.notna(budget) and budget != 0:
                if pd.notna(pct_var) and abs(pct_var) >= pct_threshold:
                    variance_df_local.loc[index, 'Significant Variance'] = True
                    variance_df_local.loc[index, 'Variance Note'] = f"Significant variance: Percentage >= {pct_threshold:.2f}%"
            elif pd.notna(budget) and budget == 0:
                actual = row.get('Actual', 0)
                if pd.notna(actual) and actual != 0:
                    variance_df_local.loc[index, 'Significant Variance'] = True
                    variance_df_local.loc[index, 'Variance Note'] = "Significant variance: Budget was zero, Actual is non-zero"
    return variance_df_local

budget_file = 'budget_data.csv'
actual_file = 'actual_data.csv'
percentage_threshold = 5.5  # Your threshold

budget_df = load_data(budget_file)
actual_df = load_data(actual_file)

if budget_df is not None and actual_df is not None:
    merged_df = align_data(budget_df, actual_df)
    variance_df = calculate_variances(merged_df)
    variance_flagged_df = flag_significant_variances(variance_df, percentage_threshold)

    # 2. Initialize the Dash app
    app = dash.Dash(__name__)

    # 3. Define the layout of the dashboard
    app.layout = html.Div(children=[
        html.H1(children='Budget vs. Actual Variance Analysis'),

        # 4. Display the data table
        dash_table.DataTable(
            id='variance-table',
            columns=[{"name": i, "id": i} for i in variance_flagged_df.columns],
            data=variance_flagged_df.to_dict('records'),
            style_cell={'textAlign': 'left'},
            style_header={
                'backgroundColor': 'lightgrey',
                'fontWeight': 'bold'
            },
            # 5. Style rows with significant variances
            style_data_conditional=[
                {
                    'if': {'row_index': 'even'},
                    'backgroundColor': 'whitesmoke'
                },
                {
                    'if': {
                        'filter_query': '{Significant Variance} eq true'
                    },
                    'backgroundColor': 'tomato',
                    'color': 'white'
                }
            ]
        )
    ])

    # 6. Run the Dash app
    if __name__ == '__main__':
        app.run(debug=True)
else:
    print("Error: Could not load budget and actual data.")