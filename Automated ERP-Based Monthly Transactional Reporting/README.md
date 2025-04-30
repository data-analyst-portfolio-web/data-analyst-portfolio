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

![CL Summary Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/CL%20Summary%20Report.PNG)

📥 [Download Full CL Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/CL_Report_2025.xlsx)

---

### 🛢️ Delivered Summary Overview

![Delivered Summary](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Delivered%20Summary.PNG)

📥 [Download Delivered Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Delivered_Report_2025.xlsx)

---

### 🧴 Lube Analysis Summary

![Lube Summary](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Lube%20Summary.PNG)

📥 [Download Lube Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Lube_Report_2025.xlsx)

---

### 📦 Purchase Transactions Trend

![Purchase Summary](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Purchase%20Summary.PNG)

📥 [Download Purchase Report](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Reports/Purchase_Report_2025.xlsx)

---

### 👥 Customer Analysis (Cardlock & Delivered)

![Customer CL Analysis](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Customer%20CL%20Analysis.PNG)
![Customer Delivered Analysis](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Customer%20Delivered%20Analysis.PNG)

---

### 💡 Pricing Tier Distribution

![Pricing Distribution](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/Pricing%20Distribution.PNG)

---

## 📂 Folder Structure

```
Project/
├── Images/
├── Reports/
├── data/
│   ├── raw/
│   │   ├── CL/
│   │   ├── Delivered/
│   │   ├── Lube/
│   │   └── Purchase/
├── scripts/
│   ├── Cardlock/
│   ├── Delivered/
│   ├── Lube/
│   └── Purchase/
├── customer_analysis/
└── README.md
```

---

## 👨‍💼 Author

**Mohammad Zakirul Islam Khan**  
Business Analyst | Data Engineer  
📍 Vancouver, BC, Canada  
🔗 [LinkedIn](https://www.linkedin.com/in/mzik) | ✉️ zakirul.islam973@gmail.com
