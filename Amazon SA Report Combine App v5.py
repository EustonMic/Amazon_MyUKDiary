import glob
import pandas as pd
import os
import warnings
import re

# Suppress specific openpyxl warnings
warnings.simplefilter("ignore", category=UserWarning)

# Function to normalize column names
def normalize_column_names(df):
    # Replace en dash with hyphen and clean up spaces
    df.columns = df.columns.str.replace(r'–', '-', regex=True)  # Replace en dash with hyphen
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)  # Replace multiple spaces with a single space
    df.columns = df.columns.str.strip()  # Remove leading and trailing whitespace
    df.columns = df.columns.str.title()  # Convert to title case
    df.columns = df.columns.str.replace(r'-\s*\(Click\)', '', regex=True)  # Remove '- (Click)' suffix
    df.columns = df.columns.str.replace(r'14-Day', '14 Day', regex=True)  # Standardize '14-Day' to '14 Day'
    df.columns = df.columns.str.strip()  # Ensure to remove any trailing spaces
    
    # Ensure unique column names by appending a suffix if duplicates exist
    original_columns = df.columns.tolist()
    new_columns = []
    for col in original_columns:
        if col in new_columns:
            suffix = 1
            new_col = f"{col}_{suffix}"
            while new_col in new_columns:
                suffix += 1
                new_col = f"{col}_{suffix}"
            new_columns.append(new_col)
        else:
            new_columns.append(col)
    
    df.columns = new_columns
    return df

# Function to combine Excel files based on specific naming patterns
def combine_excel_files(report_name, script_directory):
    # Define the output file name
    output_file = os.path.join(script_directory, f"combined_{report_name}.xlsx")

    # Remove existing combined file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Removed existing combined file: {output_file}")

    # Use glob to find all relevant Excel files matching the report_name pattern
    # Adjust pattern to be more inclusive for various file naming conventions
    files_with_suffixes = glob.glob(os.path.join(script_directory, f"*{report_name}*(*).xlsx"))
    files_without_suffix = glob.glob(os.path.join(script_directory, f"*{report_name}*.xlsx"))

    # Combine the lists and ensure unique file selection
    all_files = list(set(files_with_suffixes + files_without_suffix))
    print(f"Excel files found for '{report_name}':", all_files)

    # Check if any files were found before attempting to concatenate
    if all_files:
        try:
            # Initialize an empty list to hold dataframes
            dataframes = []
            
            # Loop through each file and load the DataFrame, printing the shape for debugging
            for f in all_files:
                df = pd.read_excel(f)
                print(f"Loaded {f} with shape: {df.shape}")

                # Normalize column names
                df = normalize_column_names(df)

                # Append normalized DataFrame to the list
                dataframes.append(df)
            
            # Concatenate all dataframes
            combined_df = pd.concat(dataframes, ignore_index=True)

            # Save the combined DataFrame to the specified output file
            combined_df.to_excel(output_file, index=False)
            print(f"Combined data for '{report_name}' has been saved successfully to:", output_file)
        except Exception as e:
            print("An error occurred while combining files:", e)
    else:
        print(f"No Excel files found for '{report_name}' in the script's directory.")

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_directory)

# Define the report names for the four types of raw data files
report_names = [
    "Sponsored Products Search term report",
    "Sponsored Products Advertised product report",
    "Sponsored Display Advertised product report",
    "Sponsored Brands Search term report"
]

# Loop through each report name and combine files
for report_name in report_names:
    combine_excel_files(report_name, script_directory)
