# 📈 Price Change Notification System (Excel Automation)

This project automates the generation of daily price notifications (PCNs) for Cool Creek Energy using Microsoft Excel with embedded logic, macros, and customer-tiered pricing.

## 💼 Project Overview
- Automatically computes price/liter per fuel type
- Adjusts for taxes, markup, and freight costs
- Supports 10+ customer pricing groups (C0–C5, Special, Reseller)
- Built-in macros to clean and import daily CSV feeds

## 🧠 Core Features
- Tax automation by province (GST, PST, QST)
- Freight & Facility lookup by site number
- Group-based markups
- Address lookup and EFS integration

## 🔁 Daily Workflow
1. Paste RCP CSV into `RCP Input`
2. Run `RCPSORT` and `Import` macros
3. Review results in group tabs (e.g., `C1 Group`, `C2 Group`)
4. Export or distribute updated PCNs

## 📂 Files Included
- `Cool Creek Energy Ltd PCN Effective Apr 11, 2025.xlsm`: Main Excel Workbook file with all logic
- `logic_summary.md`: Markdown breakdown of formulas and logic
- `macro_code.vba`: Full macro automation script
- `images/`: Screenshots of the workbook

## 👨‍💼 Author
**Mohammad Zakirul Islam Khan**  
📍 Vancouver, BC  
📧 zakirul.islam973@gmail.com  
[LinkedIn](https://www.linkedin.com/in/mzik)
[GitHub](https://github.com/data-analyst-portfolio-web)
