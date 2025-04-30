import pandas as pd
import os

# Define the folder containing the CSV files
csv_folder = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\CL\Summary"

# List of CSV files to merge (Update file names accordingly)
csv_files = [
    os.path.join(csv_folder, "CL_Assigned_summ.csv"),
    os.path.join(csv_folder, "CL_External_summ.csv"),
    os.path.join(csv_folder, "CL_Unassign_summ.csv")
]

# Define output file name
output_file = os.path.join(csv_folder, "CL_Assign_Unassign_External.csv")

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through each CSV file and read into a DataFrame
for file in csv_files:
    if os.path.exists(file):  # Check if the file exists
        df = pd.read_csv(file)
        data_frames.append(df)
        print(f"Appended: {file}")
    else:
        print(f"File not found: {file}")

# Merge all DataFrames into one
if data_frames:
    merged_df = pd.concat(data_frames, ignore_index=True)

    # Save to a new CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"\n✅ Merged CSV file created: {output_file}")
else:
    print("\n❌ No valid CSV files to merge.")
