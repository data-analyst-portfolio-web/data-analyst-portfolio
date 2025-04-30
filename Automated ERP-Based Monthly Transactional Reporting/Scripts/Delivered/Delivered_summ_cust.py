import pandas as pd
import os

# Define the folder containing Excel files
folder_path = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Delivered"
output_file = r"C:\Users\CCE\Documents\Cool Creek Docs\Reports\Melinda\Raw\Delivered\Summary\Delivered_summ_cust.csv"

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
        df = pd.read_excel(file_path, dtype={"CUSTOMER_ID": str}, usecols=[
            "DELIVERED_QTY", "COST_AMOUNT", "SALES_AMOUNT", "NPROFITAMT", "CUSTOMER_ID",
            "NAME", "PRODUCT_ID", "PROD_DESC", "Database", "MOD", "Assigned/Unassigned",
            "GAS/Diesel", "YearMon", "Clear/Dyed"])
        
        # Append the data to the list
        data_frames.append(df)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# Combine all data into a single DataFrame
if data_frames:
    combined_df = pd.concat(data_frames, ignore_index=True)

      # Replace NaN values in multiple columns with default values
    combined_df.fillna({
        "NAME": "Unknown",
        "PRODUCT_ID": "Unknown",
        "PROD_DESC": "Unknown",
        "Database": "Unknown",
        "MOD": "Unknown",
        "Assigned/Unassigned": "Unknown",
        "GAS/Diesel": "Unknown",
        "YearMon": "Unknown",
        "Clear/Dyed": "Unknown"
    }, inplace=True)

    # **Group and aggregate data** while keeping CUSTOMER_ID as text
    result = combined_df.groupby(["CUSTOMER_ID", "NAME", "PRODUCT_ID", "PROD_DESC", "Database", "MOD",
                                  "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed"], as_index=False).agg({
        "CUSTOMER_ID": "first",    # Keep original CUSTOMER_ID
        "DELIVERED_QTY": "sum",    # Sum DELIVERED_QTY
        "COST_AMOUNT": "sum",      # Sum Cost Amount
        "SALES_AMOUNT": "sum",     # Sum SALES_AMOUNT
        "NPROFITAMT": "sum"        # Sum NPROFITAMT
    })

    # **Calculate TRANSACTION_COUNT based on the frequency of CUSTOMER_ID**
    transaction_counts = combined_df.groupby(["CUSTOMER_ID", "NAME", "PRODUCT_ID", "PROD_DESC", "Database", "MOD",
                                              "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed"]).size().reset_index(name="TRANSACTION_COUNT")

    # **Merge TRANSACTION_COUNT into result**
    result = result.merge(transaction_counts, on=["CUSTOMER_ID", "NAME", "PRODUCT_ID", "PROD_DESC", "Database", "MOD",
                                                  "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed"])

    # **Ensure CUSTOMER_ID remains as text and is the first column**
    result["CUSTOMER_ID"] = result["CUSTOMER_ID"].astype(str)

    # **Rearrange columns to keep CUSTOMER_ID first**
    column_order = ["CUSTOMER_ID", "TRANSACTION_COUNT", "NAME", "PRODUCT_ID", "PROD_DESC", "Database", "MOD",
                    "Assigned/Unassigned", "GAS/Diesel", "YearMon", "Clear/Dyed", "DELIVERED_QTY", "COST_AMOUNT", "SALES_AMOUNT", "NPROFITAMT"]

    result = result[column_order]  # Reordering the columns

    # Save the result to a CSV file
    result.to_csv(output_file, index=False)
    print(f"Summary saved to: {output_file}")

else:
    print("No 'Merged_Delivered' Excel files found in the folder.")
