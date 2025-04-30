# 🧾 Monthly Fuel & Lube Transaction Reporting System

## Project Overview

This project automates the monthly generation of transaction-level and customer-level reports for Cardlock, Delivered, Lube, and Purchase modules. It is used by an oil and gas company to track and analyze product movements and purchasing trends using ERP-extracted data.

## Data Collection

- **Source:** ERP system (via SFTP every 3rd of each month)
- **Files:** ~25 raw Excel files per month, categorized by transaction type
- **Raw Data Folder Structure:**
  ```
  \Reports\Monthly\Raw\CL
  \Reports\Monthly\Raw\Delivered
  \Reports\Monthly\Raw\Lube
  \Reports\Monthly\Raw\Purchase
  ```

## Processing Workflow

1. **Raw Data Ingestion**
   - Files are sorted into designated folders
   - Naming convention follows YYYYMM pattern

2. **Transformation Scripts**
   - **Cardlock:** `Assigned.py`, `Unassigned.py`, `External.py`
   - **Delivered:** `Delivered.py`
   - **Lube:** `Lube.py`
   - **Purchase:** `Purchase.py`
   - These merge or append records to year-based Excel files

3. **Summary Generation**
   - **Cardlock Summary:** `CL_Unassign_summ.py`, `CL_Assigned_summ.py`, `CL_External_summ.py`
   - **Delivered:** `Delivered_summ.py`
   - **Lube:** `Lube_summ.py`
   - **Purchase:** `Purchase_summ.py`

4. **Customer-Level Analytics**
   - Advanced metrics including profit, volume trends, and transaction counts
   - Customer-focused scripts: `Delivered_summ_cust.py`, `Lube_summ_cust.py`, customer CSVs for CL

## Output

- Annual merged datasets for each module
- Monthly trend dashboards with:
  - Volume
  - Sales
  - Profit
  - Transaction count
- Customer summary & distribution reports by pricing bucket

## Technologies Used

- Python (Pandas, OpenPyXL)
- Excel PivotTables & Charts
- SFTP data retrieval
- ERP integration
