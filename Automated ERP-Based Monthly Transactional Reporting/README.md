# 📊 Monthly Operations Reporting & Analysis System

This project automates the generation, transformation, and analysis of monthly operations data—including Cardlock (CL), Delivered, Lube, and Purchase modules. It supports high-level summaries and detailed customer-level insights using Python-based ETL scripts, integrated Excel analytics, and automated SFTP data ingestion.

---

## 🔍 Project Objectives

- Automate monthly collection and processing of raw billing data from ERP
- Generate yearly transaction logs for each module
- Produce monthly and YTD reports for management review
- Analyze trends by site, product, and customer
- Provide insights into pricing structure and profitability

---

## 🧠 Process Overview

1. **Data Collection**
   - Monthly billing data is exported from ERP as Excel files
   - 25 files are collected on the 3rd day of each month via SFTP
   - Files are organized in:
     ```
     /Reports/Monthly/Raw/CL
     /Reports/Monthly/Raw/Delivered
     /Reports/Monthly/Raw/Lube
     /Reports/Monthly/Raw/Purchase
     ```

2. **ETL with Python**
   - Scripts used:
     - `Unassigned.py`, `Assigned.py`, `External.py` (Cardlock)
     - `Delivered.py`, `Lube.py`, `Purchase.py`
   - Consolidates monthly data into yearly master files per category

3. **Summarization**
   - Summary scripts:
     - `CL_Unassign_summ.py`, `CL_Assigned_summ.py`, `CL_External_summ.py`
     - `Delivered_summ.py`, `Lube_summ.py`, `Purchase_summ.py`
   - Customer-level breakdowns:
     - `Delivered_summ_cust.py`, `Lube_summ_cust.py`

---

## 🧾 Sample Reports & Screenshots

### 📘 CL Summary Report

![CL Summary Report](images/cl_summary.png)

📥 [Download Full CL Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/CL_Report_2025.xlsx)

---

### 🛢️ Delivered Summary Overview

![Delivered Summary](images/delivered_summary.png)

📥 [Download Delivered Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Delivered_Report_2025.xlsx)

---

### 🧴 Lube Analysis Summary

![Lube Summary](images/lube_summary.png)

📥 [Download Lube Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Lube_Report_2025.xlsx)

---

### 📦 Purchase Transactions Trend

![Purchase Summary](images/purchase_summary.png)

📥 [Download Purchase Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Purchase_Report_2025.xlsx)

---

### 👥 Customer Analysis (Cardlock & Delivered)

![Customer CL Analysis](images/customer_cl.png)
![Customer Delivered Analysis](images/customer_delivered.png)

---

### 💡 Pricing Tier Distribution

![Pricing Distribution](images/pricing_distribution.png)

---

## 📂 Folder Structure

```
project/
├── data/
│   ├── raw/
│   │   ├── CL/
│   │   ├── Delivered/
│   │   ├── Lube/
│   │   └── Purchase/
├── scripts/
│   ├── Cardlock/
│   │   ├── Assigned.py
│   │   ├── Unassigned.py
│   │   ├── External.py
│   │   ├── CL_Assigned_summ.py
│   │   ├── CL_Unassign_summ.py
│   │   └── CL_External_summ.py
│   ├── Delivered/
│   │   ├── Delivered.py
│   │   └── Delivered_summ.py
│   ├── Lube/
│   │   ├── Lube.py
│   │   └── Lube_summ.py
│   └── Purchase/
│       ├── Purchase.py
│       └── Purchase_summ.py
├── customer_analysis/
│   ├── CL_Unassign_summ_cust.csv
│   ├── CL_External_summ_cust.csv
│   ├── Delivered_summ_cust.py
│   └── Lube_summ_cust.py
└── README.md
```

---

## 👨‍💼 Author

**Mohammad Zakirul Islam Khan**  
Business Analyst | Data Engineer  
📍 Vancouver, BC, Canada  
🔗 [LinkedIn](https://www.linkedin.com/in/mzik) | ✉️ zakirul.islam973@gmail.com
