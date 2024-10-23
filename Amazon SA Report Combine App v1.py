import glob
import pandas as pd
import os
import warnings

# Suppress specific openpyxl warnings
warnings.simplefilter("ignore", category=UserWarning)

# Function to combine Excel files based on specific naming patterns
def combine_excel_files(report_name, script_directory):
    # Use glob to find all Excel files that match the report_name pattern with variations
    files = glob.glob(os.path.join(script_directory, f"*{report_name}*(*).xlsx"))
    print(f"Excel files found for '{report_name}':", files)

    # Check if any files were found before attempting to concatenate
    if files:
        try:
            # Initialize an empty list to hold dataframes
            dataframes = []
            
            # Loop through each file and load the DataFrame, printing the shape for debugging
            for f in files:
                df = pd.read_excel(f)
                print(f"Loaded {f} with shape: {df.shape}")
                dataframes.append(df)
            
            # Concatenate all dataframes
            combined_df = pd.concat(dataframes, ignore_index=True)

            # Define the output file name and save the combined DataFrame to the same directory
            output_file = os.path.join(script_directory, f"combined_{report_name}.xlsx")
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
