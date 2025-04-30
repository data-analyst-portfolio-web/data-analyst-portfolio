# 📈 Price Change Notification System (Excel Automation)

This project automates the generation of daily Price Change Notifications (PCNs) for an oil and gas company using Microsoft Excel. It features embedded business logic, VBA macros, and a robust customer-tiered pricing structure to dynamically calculate fuel prices across multiple locations and customer groups. The system integrates real-time rack pricing, freight and facility charges, tax rules, and markups to produce ready-to-distribute pricing updates with minimal manual input.

## 💼 Project Overview
- Automatically computes price/liter per fuel type
- Adjusts for taxes, markup, and freight costs
- Supports 10+ customer pricing groups (C0–C5, Special, Reseller)
- Built-in macros to clean and import daily CSV feeds

## 🧠 Core Features
- Tax automation by province (GST, PST, QST)
- Freight & Facility lookup by site number
- Group-based markups
- Address lookup for location

## 🔁 Daily Workflow
1. Paste RCP CSV into `RCP Input`
2. Run `RCPSORT` and `Import` macros
3. Review results in group tabs (e.g., `C1 Group`, `C2 Group`)
4. Export or distribute updated PCNs

## 📂 Files Included
- `PCN Effective Apr 11, 2025.xlsm`: Main Excel Workbook file with all logic
- `logic_summary.md`: Markdown breakdown of formulas and logic
- `macro_code.vba`: Full macro automation script

## 🧾 Sample Reports & Screenshots

![Input Sheet](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/PCN/Images/PCN.PNG)
![RCP Input](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/PCN/Images/RCP%20Input.PNG)
![C1](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/PCN/Images/C1.PNG)

## 👨‍💼 Author
**Mohammad Zakirul Islam Khan**  
📍 Vancouver, BC  
📧 zakirul.islam973@gmail.com  
[LinkedIn](https://www.linkedin.com/in/mzik)
[GitHub](https://github.com/data-analyst-portfolio-web)
