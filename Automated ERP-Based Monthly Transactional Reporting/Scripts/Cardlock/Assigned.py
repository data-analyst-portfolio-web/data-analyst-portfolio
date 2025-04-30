import pandas as pd
import os
import shutil
import glob
import sys
import time
import psutil

# Folder containing your "Assigned" Excel files
folder_path = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\CL"
output_folder = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\CL"
merged_output_file_base = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\CL\Merged_Assigned.xlsx"

# Columns to keep for Assigned files
columns_to_keep = [
    "CTICKETID", "SUPPLIER_INVOICE", "NQTYINV", "NCOSTINV", "NAMTINV", 
    "TAX_ID", "CDESTINATIONID", "PICK_ID", "SUPPLIER_ID", "DTICKET", 
    "CDESTINATIONNAME", "PROD_DESC"
]

# Define GAS/Diesel formula logic
def gas_diesel_formula(value):
    value = str(value).upper()
    if any(keyword in value for keyword in ["GASOLINE", "GAS", "ETHANOL", "BLEND", "UNLEADED"]):
        return "GAS"
    elif any(keyword in value for keyword in ["DEF", "BULK"]):
        return "DEF"
    else:
        return "Diesel"

# Define Clear/Dyed formula logic
def clear_dyed_formula(value):
    value = str(value).upper()
    if any(keyword in value for keyword in ["GASOLINE", "GAS", "ETHANOL", "BLEND", "UNLEADED"]):
        return "GAS-Dyed" if "DYED" in value else "GAS-Clear"
    elif any(keyword in value for keyword in ["DEF", "BULK"]):
        return "DEF"
    else:
        return "Diesel-Dyed" if "DYED" in value else "Diesel-Clear"

# Define YEARMON formula logic
def yearmon_formula(value):
    value = str(value).strip()  # Convert to string and remove leading/trailing spaces
    if len(value) >= 10:  # Ensure the string is long enough to extract parts
        return (value[6:10] + value[:2]).strip()  # Extract year and month as YYYYMM and trim
    return ""

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
assigned_files = [file for file in os.listdir(folder_path) if file.lower().startswith("assigned") and file.lower().endswith('.xlsx')]

# Check if there are no matching files
if not assigned_files:
    print("No 'Assigned' files found in the folder.")
    sys.exit()  # Exit the program
else:
    # Process each "Assigned" file
    for file_name in os.listdir(folder_path):
        if file_name.lower().startswith("assigned") and file_name.lower().endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
        
            # Read the Excel file
            df = pd.read_excel(file_path)
            
            # Keep only the required columns
            df = df[columns_to_keep]

            # Drop rows where DTICKET is null
            df = df.dropna(subset=["DTICKET"])

            
            # Rename columns and convert values to positive
            df.rename(columns={"NQTYINV": "VOLUME", "NAMTINV": "AMOUNT"}, inplace=True)
            if "VOLUME" in df.columns:
                df["VOLUME"] = df["VOLUME"].abs()
            if "AMOUNT" in df.columns:
                df["AMOUNT"] = df["AMOUNT"].abs()
            
            # Add "Database" column
            file_name_lower = file_name.lower()  # Convert file_name to lowercase for case-insensitive comparison
            
            if "cce" in file_name_lower:
                database_value = "CCE"
            elif "castlegar" in file_name_lower:
                database_value = "Castlegar"
            elif "cranbrook" in file_name_lower:
                database_value = "Cranbrook"
            else:
                database_value = file_name.replace(".xlsx", "")
            
            df["Database"] = database_value
            
            # Add "MOD" column
            df["MOD"] = "CL"
            
            # Add "Assigned/Unassigned" column
            df["Assigned/Unassigned"] = "Assigned"
            
            # Add "GAS/Diesel" column
            df["GAS/Diesel"] = df["PROD_DESC"].apply(gas_diesel_formula)
            
            # Add "Mon/Year" column
            df["YearMon"] = df["DTICKET"].apply(yearmon_formula)           
            
            # Add "Clear/Dyed" column
            df["Clear/Dyed"] = df["PROD_DESC"].apply(clear_dyed_formula)
            
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
    

# Ensure DTICKET is in datetime format
merged_df["DTICKET"] = pd.to_datetime(merged_df["DTICKET"], errors="coerce")

# Group data by year
merged_df["Year"] = merged_df["DTICKET"].dt.year

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
            combined_df = pd.concat([existing_df, year_df], ignore_index=True).drop_duplicates(subset=existing_df.columns[:12])

        else:
            # Directly use the new data if the file does not exist
            combined_df = year_df.drop_duplicates(subset=year_df.columns[:12])

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
