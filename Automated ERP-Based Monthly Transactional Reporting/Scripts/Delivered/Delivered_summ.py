import pandas as pd
import os

# Define the folder containing Excel files
folder_path = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Delivered"
output_file = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Delivered\Summary\Delivered_summ.csv"

# List all Excel files that start with "Merged_Delivered"
excel_files = [f for f in os.listdir(folder_path) if f.startswith("Merged_Delivered") and f.endswith((".xlsx", ".xls"))]

# Initialize an empty list to store DataFrames
data_frames = []

# Process each "Merged_Delivered" Excel file
for file_name in excel_files:
    file_path = os.path.join(folder_path, file_name)
    print(f"Processing: {file_path}")

    try:
        # Load specific columns from each Excel file
        df = pd.read_excel(file_path, usecols=["DELIVERED_QTY", "SALES_AMOUNT", "Database", "MOD", "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed"])
        
        # Append the data to the list
        data_frames.append(df)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# Combine all data into a single DataFrame
if data_frames:
    combined_df = pd.concat(data_frames, ignore_index=True)

    # Group and sum QTY and AMOUNT based on required columns
    result = combined_df.groupby(["Database", "MOD", "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed"], as_index=False).sum()

    # Save the result to a CSV file
    result.to_csv(output_file, index=False)
    print(f"Summary saved to: {output_file}")
else:
    print("No 'Merged_Unassigned' Excel files found in the folder.")
