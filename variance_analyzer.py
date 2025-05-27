import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def align_data(budget_df, actual_df, key_column='Line Item'):
    """Merges budget and actual dataframes based on a common key column."""
    merged_df = pd.merge(budget_df, actual_df, on=key_column, how='outer')
    return merged_df

def calculate_variances(merged_df):
    """Calculates the absolute and percentage variances."""
    if 'Budget' in merged_df.columns and 'Actual' in merged_df.columns:
        merged_df['Variance (Absolute)'] = merged_df['Actual'] - merged_df['Budget']
        merged_df['Variance (%)'] = (merged_df['Variance (Absolute)'] / merged_df['Budget']) * 100
    else:
        print("Error: 'Budget' and 'Actual' columns are required for variance calculation.")
    return merged_df

def flag_significant_variances(variance_df, pct_threshold):
    """Flags significant variances based on a percentage threshold (>=)."""
    variance_df['Significant Variance'] = False
    variance_df['Variance Note'] = ''

    if 'Variance (%)' in variance_df.columns and 'Budget' in variance_df.columns:
        for index, row in variance_df.iterrows():
            pct_var = row['Variance (%)']
            budget = row['Budget']

            print(f"Line Item: {row['Line Item']}, Percentage Variance: {pct_var}") # DEBUG PRINT

            if pd.notna(budget) and budget != 0:
                if pd.notna(pct_var) and abs(pct_var) >= pct_threshold: # Changed > to >=
                    variance_df.loc[index, 'Significant Variance'] = True
                    variance_df.loc[index, 'Variance Note'] = f"Significant variance: Percentage >= {pct_threshold:.2f}%"
            elif pd.notna(budget) and budget == 0:
                actual = row.get('Actual', 0)
                if pd.notna(actual) and actual != 0:
                    variance_df.loc[index, 'Significant Variance'] = True
                    variance_df.loc[index, 'Variance Note'] = "Significant variance: Budget was zero, Actual is non-zero"
    else:
        print("Error: 'Variance (%)' and 'Budget' columns are required for percentage-based flagging.")

    return variance_df

if __name__ == "__main__":
    budget_file = 'budget_data.csv'
    actual_file = 'actual_data.csv'

    budget_df = load_data(budget_file)
    actual_df = load_data(actual_file)

    if budget_df is not None and actual_df is not None:
        merged_df = align_data(budget_df, actual_df)
        variance_df = calculate_variances(merged_df)

        # Define your significance threshold (percentage) WITH DECIMALS
        percentage_threshold = 5   # Example: 5.5%

        # Call the updated flagging function
        variance_flagged_df = flag_significant_variances(variance_df.copy(), percentage_threshold)

        # Set Pandas display options to show all columns
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)

        print("\nBudget vs. Actual Performance with Variances and Flags (Percentage Based):")
        print(variance_flagged_df)

        # Optional: Sort by Line Item
        # variance_flagged_df = variance_flagged_df.sort_values(by='Line Item')
        # print("\nSorted Budget vs. Actual Performance with Variances and Flags:")
        # print(variance_flagged_df)