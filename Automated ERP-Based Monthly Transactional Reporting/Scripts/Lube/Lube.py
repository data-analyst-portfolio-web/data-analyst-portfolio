import pandas as pd
import os
import shutil
import glob
import sys
import time
import psutil

# Folder containing your "Unassigned" Excel files
folder_path = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Lube"
output_folder = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Lube"
merged_output_file_base = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Lube\Merged_Lube"


# Define YEARMON formula logic
def yearmon_formula(value):
    value = str(value).strip()  # Convert to string and remove leading/trailing spaces
    if len(value) >= 10:  # Ensure the string is long enough to extract parts
        return (value[6:10] + value[:2]).strip()  # Extract year and month as YYYYMM and trim
    return ""

def assigned_unassigned_formula(value):
    value = str(value).upper()
    
    # Check if the value starts with '7' and has exactly 5 digits
    if value.startswith('7') and len(value) == 5 and value.isdigit():
        return "Assigned"
    else:
        return "Unassigned"

def close_excel_processes():
    """Close all running Excel processes to release file locks."""
    for process in psutil.process_iter():
        try:
            if process.name().lower() == "excel.exe":
                process.terminate()  # Forcefully close Excel
                print("Closed an active Excel process.")
        except psutil.NoSuchProcess:
            pass  # Process already closed
        except Exception as e:
            print(f"Error closing Excel process: {e}")

def is_file_locked(file_path):
    """Check if a file is locked by another process."""
    try:
        with open(file_path, "r+"):
            return False  # File is not locked
    except PermissionError:
        return True  # File is locked

def wait_for_file_release(file_path, timeout=10):
    """Wait for a file to be released before deleting."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not is_file_locked(file_path):
            return True  # File is available for deletion
        print(f"File {file_path} is in use. Retrying in 1 second...")
        time.sleep(1)

    return not is_file_locked(file_path)  # Return whether the file is free now

# Initialize an empty list to store processed DataFrames
processed_data = []

# Get the list of relevant files
lube_files = [file for file in os.listdir(folder_path) if file.lower().startswith("lube") and file.lower().endswith('.xlsx')]

# Check if there are no matching files
if not lube_files:
    print("No 'Lube' files found in the folder.")
    sys.exit()  # Exit the program
else:
    # Process each "Unassigned" file
    for file_name in os.listdir(folder_path):
        if file_name.lower().startswith("lube") and file_name.lower().endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            
            # Read the Excel file, ensuring CUSTOMER_ID is treated as text
            df = pd.read_excel(file_path, dtype={"SORT_FIELD": str})
            df = pd.read_excel(file_path, dtype={"CNEWCUSTID": str})
            df = pd.read_excel(file_path, dtype={"CUSTOMER_ID": str})

            # Rename "CUSTOMER_NAME" to "NAME" if it exists
            if "CUSTOMER_NAME" in df.columns:
                df.rename(columns={"CUSTOMER_NAME": "NAME"}, inplace=True)
                #print(f"'CUSTOMER_NAME' column renamed to 'NAME' in {file_name}")

            # Check and remove the "Mon/Year" column if it exists
            if "Mon/Year" in df.columns:
                df = df.drop(columns=["Mon/Year"])
                print(f"'Mon/Year' column removed from {file_name}")

            # Convert SORT_FIELD column to string type
            df["SORT_FIELD"] = df["SORT_FIELD"].apply(lambda x: str(int(x)).zfill(5) if pd.notna(x) and str(x).isdigit() else str(x) if pd.notna(x) else "")
            df["CUSTOMER_ID"] = df["CUSTOMER_ID"].apply(lambda x: str(int(x)).zfill(5) if pd.notna(x) and str(x).isdigit() else str(x) if pd.notna(x) else "")
            df["CNEWCUSTID"] = df["CNEWCUSTID"].apply(lambda x: str(int(x)).zfill(5) if pd.notna(x) and str(x).isdigit() else str(x) if pd.notna(x) else "")

            # List of values to delete
            values_to_delete = ["01500", "02550", "04000", "00999", "40164"]

            # Filter out rows where CUSTOMER_ID matches the values or contains "IMP" or "IOL"
            df = df[
                ~df["CUSTOMER_ID"].str.upper().isin(values_to_delete) &  # Check for exact values
                ~df["CUSTOMER_ID"].str.upper().str.contains("IMP|IOL", na=False)  # Check for "IMP" or "IOL"
            ]
            
            file_name_lower = file_name.lower()  # Convert file_name to lowercase for case-insensitive comparison

            if "cce" in file_name_lower:
                database_value = "CCE"
            elif "castlegar" in file_name_lower:
                database_value = "Castlegar"
            elif "cranbrook" in file_name_lower:
                database_value = "Cranbrook"
            elif "pg" in file_name_lower:
                database_value = "PG"
            else:
                database_value = file_name.replace(".xlsx", "")

            
            df["Database"] = database_value

            # Add "Assigned/Unassigned" column
            df["Assigned/Unassigned"] = df["SORT_FIELD"].apply(assigned_unassigned_formula)
            
            # Add "Mon/Year" column
            df["YearMon"] = df["INVOICE_DATE"].apply(yearmon_formula)

            
            # Save the processed file
            output_file_path = os.path.join(output_folder, f"Processed_{file_name}")
            df.to_excel(output_file_path, index=False)

            if "Mon/Year" in df.columns:
               df = df.drop(columns=["Mon/Year"])
               
            # Append the processed DataFrame to the list
            processed_data.append(df)

            # Move the processed file to the "Processed" folder
            processed_folder = os.path.join(folder_path, "Processed")  # Define the processed folder path
            os.makedirs(processed_folder, exist_ok=True)  # Create the folder if it doesn't exist

            destination_path = os.path.join(processed_folder, file_name)  # Destination path for the file
            shutil.move(file_path, destination_path)  # Move the file to the "Processed" folder
            print(f"File moved to: {destination_path}")

# Merge all processed DataFrames into one
merged_df = pd.concat(processed_data, ignore_index=True)

if "Mon/Year" in merged_df.columns:
    merged_df = merged_df.drop(columns=["Mon/Year"], errors="ignore")


# Ensure INVOICE_DATE is in datetime format
merged_df["INVOICE_DATE"] = pd.to_datetime(merged_df["INVOICE_DATE"], errors="coerce")

# Group data by year
merged_df["Year"] = merged_df["INVOICE_DATE"].dt.year

# Save yearly data into separate Excel files
for year, year_df in merged_df.groupby("Year"):
    if "Mon/Year" in year_df.columns:
        year_df = year_df.drop(columns=["Mon/Year"], errors="ignore")
        
    if pd.notna(year):  # Skip rows with invalid dates
        output_file = f"{merged_output_file_base}_{int(year)}.xlsx"

        # Drop the Year column
        year_df = year_df.drop(columns=["Year"], inplace=False)

        if os.path.exists(output_file):
            # Read existing data from the file
            existing_df = pd.read_excel(output_file)

            # Append new data and drop duplicates in one step
            combined_df = pd.concat([existing_df, year_df], ignore_index=True).drop_duplicates(subset=existing_df.columns[:22])

        else:
            # Directly use the new data if the file does not exist
            combined_df = year_df.drop_duplicates(subset=year_df.columns[:22])

        # Save the final combined DataFrame back to the file
        combined_df.to_excel(output_file, index=False)
        print(f"Processed yearly file for {year}: {output_file}")



# Get all processed files matching the pattern
processed_files_pattern = os.path.join(output_folder, "Processed_*.xlsx")
processed_files = glob.glob(processed_files_pattern)

# Close Excel to release file locks
close_excel_processes()
time.sleep(3)  # Wait 3 seconds to allow process closure

# Attempt to delete each file
for file_path in processed_files:
    if wait_for_file_release(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    else:
        print(f"Skipping deletion: {file_path} is still in use after all attempts.")

print(f"Deletion process complete for pattern: {processed_files_pattern}")

print("Processing complete.")

