import pandas as pd
import os
import shutil
import glob
import sys
import time
import psutil

# Folder containing your "Purchase" Excel files
folder_path = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Purchase"
output_folder = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Purchase"
merged_output_file_base = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Purchase\Merged_Purchase.xlsx"

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

# Define Assigned/Unassigned formula logic
def assigned_unassigned_formula(row):
    nliter = row["NLITER"]  # Column J in the formula
    pick_id = str(row["PICK_ID"]).strip().upper()  # Column E in the formula
    supplier_id = int(row["SUPPLIER_ID"]) if not pd.isna(row["SUPPLIER_ID"]) else 0  # Column A in the formula

    # Apply the IFS logic
    if nliter < 0 and supplier_id == 9100:
        return "Unassigned"
    if nliter < 0 and supplier_id == 9800 and pick_id == "SHELLED":
        return "SHELL-EDMONTON"
    if nliter < 0 and supplier_id == 9800 and pick_id == "SHELLKA":
        return "SHELL-KAMLOOPS"    
    elif nliter < 0:
        return "Assigned"
    elif pick_id == "SHELLKA":
        return "SHELL-KAMLOOPS"
    elif pick_id == "SHELLED":
        return "SHELL-EDMONTON"
    elif pick_id == "SHELLBB":
        return "SHELL-BURNABY"
    elif pick_id == "PL621081" and supplier_id == 9700:
        return "Parkland SHELL-BURMOUNT"
    elif pick_id == "PARKBOW" and supplier_id == 9700:
        return "Parkland Bowden"
    elif pick_id == "PL628751" and supplier_id == 9700:
        return "Parkland Kamloops"
    elif pick_id == "PL621672" and supplier_id == 9700:
        return "Parkland PRBC"
    elif pick_id == "PARKEDM" and supplier_id == 9700:
        return "Parkland 653498 Edmonton"
    elif pick_id == "4RASH" and supplier_id == 9800:
        return "SHELL-ASHCROFT"
    elif pick_id == "TARASH" and supplier_id == 9900:
        return "TARGRAY-ASHCROFT"
    elif pick_id == "TARTRAIL" and supplier_id == 9900:
        return "TARGRAY-TRAIL"
    else:
        return "Unassigned"


# Define PICK_CENTER formula logic
def pick_center_formula(row):
    # Normalize inputs to ensure consistency
    database = str(row["Database"]).strip().capitalize()  # Capitalize to handle case issues
    supplier_id = int(row["SUPPLIER_ID"]) if not pd.isna(row["SUPPLIER_ID"]) else None
    pick_id = str(row["PICK_ID"]).strip().upper()  # Convert to uppercase to handle case issues

    #print(f"Database: {database}, Supplier ID: {supplier_id}, Pick ID: {pick_id}")



    # Logic for PICK_CENTER column
    
    if database == "Cranbrook" and supplier_id == 9700 and pick_id == "PARKBOW":
        return "Parkland Bowden"
    elif database == "Cranbrook" and supplier_id == 9100 and pick_id == "ESSO1":
        return "ESSO-Suncor Kamloops for resale"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSO1":
        return "ESSO-Suncor Kamloops for resale"
    elif database == "Cce" and supplier_id == 9000 and pick_id == "ESSO C/L":
        return "IOL-Customers"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSO":
        return "Kamloops-Terminal"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSOA":
        return "Ashcroft Esso Terminal"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSO4":
        return "IOL-Calgary"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSOPG":
        return "IOL Purchases  Prince George"
    elif database == "Cce" and supplier_id == 9900 and pick_id == "TARASH":
        return "Targray-Ashcroft"
    elif database == "Castlegar" and supplier_id == 9900 and pick_id == "TARTRAIL":
        return "Targray-Trail"
    elif database == "Cranbrook" and supplier_id == 9900 and pick_id == "TARTRAIL":
        return "Targray-Trail"   
    elif database == "Cranbrook" and supplier_id == 9700 and pick_id == "PARKEDM":
        return "Parkland 653498 Edmonton"
    elif database == "Castlegar" and supplier_id == 3031 and pick_id == "KAM":
        return "Cool Creek Kamloops"
    elif database == "Castlegar" and supplier_id == 4024 and pick_id == "CRAN":
        return "Cranbrook Terminal"
    elif database == "Castlegar" and supplier_id == 9100 and pick_id == "ESSO2":
        return "Terminal-Edmonton"
    elif database == "Castlegar" and supplier_id == 9100 and pick_id == "ESSO3":
        return "ESSO Lougheed terminal"
    elif database == "Cranbrook" and supplier_id == 5011 and pick_id == "KAM":
        return "Cool Creek Kamloops"
    elif database == "Cranbrook" and supplier_id == 5052 and pick_id == "CAS":
        return "Castlegar-Terminal"
    elif database == "Cranbrook" and supplier_id == 9100 and pick_id == "ESSO-2":
        return "Terminal-Edmonton"
    elif database == "Cranbrook" and supplier_id == 9100 and pick_id == "ESSO3":
        return "ESSO Lougheed terminal"
    elif database == "Cce" and supplier_id == 3104 and pick_id == "CASTLEGR":
        return "Castlegar-Terminal"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSO3":
        return "IOL Edmonton"
    elif database == "Cce" and supplier_id == 9100 and pick_id == "ESSO2":
        return "ESSO Lougheed Terminal"
    elif database == "Cce" and supplier_id == 9700 and pick_id == "PL628751":
        return "Parkland Kamloops"
    elif database == "Cce" and supplier_id == 9700 and pick_id == "PL621081":
        return "Parkland SHELL-BURMOUNT"
    elif database == "Cce" and supplier_id == 9800 and pick_id == "SHELLBB":
        return "SHELL-BURNABY"
    elif database == "Cce" and supplier_id == 3104 and pick_id == "RMCRAN":
        return "ROCKY MOUNTAIN ENERGY Cranbrook"
    elif database == "Cce" and supplier_id == 9700 and pick_id == "PL621672":
        return "Parkland PRBC"
    elif database == "Cce" and supplier_id == 9800 and pick_id == "SHELLKA":
        return "SHELL-KAMLOOPS"
    elif database == "Cce" and supplier_id == 9800 and pick_id == "SHELLED":
        return "SHELL-EDMONTON"
    elif database == "Cce" and supplier_id == 9800 and pick_id == "4RASH":
        return "Ex-Ashcroft-Terminal"
    elif database == "Castlegar" and supplier_id == 9800 and pick_id == "SHELLKA":
        return "SHELL-KAMLOOPS"
    elif database == "Castlegar" and supplier_id == 9000 and pick_id == "ESSO C/L":
        return "IOL-Customers"
    elif database == "Castlegar" and supplier_id == 9100 and pick_id == "ESSO":
        return "Kamloops-Terminal"
    elif database == "Castlegar" and supplier_id == 9100 and pick_id == "ESSO1":
        return "Calgary-Terminal"
    elif database == "Castlegar" and supplier_id == 9700 and pick_id == "PARKBOW":
        return "Parkland Bowden"
    elif database == "Cranbrook" and supplier_id == 9100 and pick_id == "ESSO":
        return "Calgary-Terminal"
    elif database == "Cranbrook" and supplier_id == 9000 and pick_id == "145374":
        return "Cranbrook-Cardlock"
    else:
        return "Unknown"

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
purchase_files = [file for file in os.listdir(folder_path) if file.lower().startswith("purchase") and file.lower().endswith('.xlsx')]


# Check if there are no matching files
if not purchase_files:
    print("No 'Purchase' files found in the folder.")
    sys.exit()  # Exit the program
else:

    # Process each "Purchase" file
    for file_name in os.listdir(folder_path):
        if file_name.lower().startswith("purchase") and file_name.lower().endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            
            # Read the Excel file
            df = pd.read_excel(file_path)

            #print(df.columns)
            
            # Delete unnecessary columns
            df.drop(columns=["CCURRENCYID", "CCURRENCYSYMBOL"], inplace=True, errors='ignore')

               # Filter rows based on supplier_id
            valid_supplier_ids = [9000, 9100, 9800, 9900]
            df = df[df["SUPPLIER_ID"].isin(valid_supplier_ids)]

            # Filter rows where supplier_id is 9000 and NLITER > 0
            df = df[~((df["SUPPLIER_ID"] == 9000) & (df["NLITER"] > 0))]

              # Rename "CUSTOMER_NAME" to "NAME" if it exists
            if "CUSTOMER_NAME" in df.columns:
                df.rename(columns={"CUSTOMER_NAME": "NAME"}, inplace=True)
                #print(f"'CUSTOMER_NAME' column renamed to 'NAME' in {file_name}")


            
            file_name_lower = file_name.lower()  # Convert file_name to lowercase for case-insensitive comparison
            
            # Add "Database" column
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
            df["MOD"] = "Purchase"
            
            # Add "Assigned/Unassigned" column
            df["Assigned/Unassigned"] = df.apply(assigned_unassigned_formula, axis=1)
            
            # Add "GAS/Diesel" column
            df["GAS/Diesel"] = df["PROD_DESC"].apply(gas_diesel_formula)

            # Add "Mon/Year" column
            df["YearMon"] = df["DBUY"].apply(yearmon_formula)
            
            # Add "PICK_CENTER" column
            df["PICK_CENTER"] = df.apply(pick_center_formula, axis=1)
            
            # Add "Clear/Dyed" column
            df["Clear/Dyed"] = df["PROD_DESC"].apply(clear_dyed_formula)

            #df.insert(df.columns.get_loc("NLITER") + 1, "Volume", df["NLITER"].abs())
            #df.insert(df.columns.get_loc("AMOUNT") + 1, "AMOUNT1", df["AMOUNT"].abs())

            

            
            # Save the processed file
            output_file_path = os.path.join(output_folder, f"Processed_{file_name}")
            df.to_excel(output_file_path, index=False)
            
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


# Ensure DBUY is in datetime format
merged_df["DBUY"] = pd.to_datetime(merged_df["DBUY"], errors="coerce")

# Group data by year
merged_df["Year"] = merged_df["DBUY"].dt.year

# Save yearly data into separate Excel files
for year, year_df in merged_df.groupby("Year"):
        
    if pd.notna(year):  # Skip rows with invalid dates
        output_file = f"{merged_output_file_base}_{int(year)}.xlsx"

        # Drop the Year column
        year_df = year_df.drop(columns=["Year"], inplace=False)

        if os.path.exists(output_file):
            # Read existing data from the file
            existing_df = pd.read_excel(output_file)

            # Append new data and drop duplicates in one step
            combined_df = pd.concat([existing_df, year_df], ignore_index=True).drop_duplicates(subset=existing_df.columns[:15])

        else:
            # Directly use the new data if the file does not exist
            combined_df = year_df.drop_duplicates(subset=year_df.columns[:15])

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
