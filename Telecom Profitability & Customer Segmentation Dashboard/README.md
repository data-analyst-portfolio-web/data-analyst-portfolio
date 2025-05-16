# 📘 Telecom Profitability & Customer Segmentation Dashboard

This project delivers a Power BI dashboard that uncovers profit trends, churn risks, and customer segmentation patterns using telecom subscriber and billing data. It enables commercial and product teams to explore and act on insights that drive revenue growth and retention.

---

## 🚀 Project Objective

Enable telecom stakeholders to:
- Identify high and low-margin customer groups.
- Monitor revenue and cost trends across services and regions.
- Track churn risks and retention outcomes.
- Segment customers based on engagement, ARPU, and lifecycle.

---

## 🧰 Tools & Technologies

| Tool        | Purpose                                      |
|-------------|----------------------------------------------|
| Power BI    | Dashboard creation and visual analytics       |
| SQL Server  | Data extraction and preparation               |
| DAX         | KPI measures and time intelligence            |
| Excel/CSV   | Sample and processed datasets                 |
| Python (opt)| Churn scoring and customer clustering         |

---

## 📊 Key Features

### 🔹 Profitability Metrics
- Revenue vs Cost trends
- Margin by Product (Mobile, Internet, Bundles)
- Gross Profit by Region / City

### 🔹 Customer Segmentation
- By ARPU, Contract, Tenure
- Dynamic filters: Age Group, Loyalty Tier
- Lifetime Value calculation (LTV)

### 🔹 Advanced KPIs
- Churn Rate
- Data Monetization: Revenue per GB
- Net Subscriber Growth
- Service Bundle Penetration

### 🔹 Predictive Signals (Optional)
- Forecasted revenue
- Early churn risk detection
- Cohort retention patterns

---

## 📁 Folder Structure

```
Telecom_Analytics_Dashboard/
│
├── data/
│   ├── raw/
│   │   ├── subscribers.csv
│   │   ├── usage.csv
│   │   ├── billing.csv
│   │   └── churn_labels.csv
│   └── processed/
│       └── telecom_model_dataset.xlsx
│
├── scripts/
│   ├── extract_subscribers.sql
│   ├── extract_usage.sql
│   ├── extract_billing.sql
│   └── churn_segmentation.py
│
├── visuals/
│   ├── profitability_dashboard.png
│   ├── segmentation_view.png
│   ├── churn_risk_panel.png
│   └── forecast_chart.png
│
├── report/
│   ├── Telecom_Profitability.pbix
│   └── Telecom_Profitability_Template.pbit
│
├── docs/
│   ├── KPI_definitions.md
│   ├── data_model_schema.png
│   └── report_walkthrough.md
│
└── README.md
```

---

## 📈 Sample DAX Snippets

```dax
ARPU = DIVIDE(SUM(Billing[Revenue]), DISTINCTCOUNT(Users[SubscriberID]))

Churn Rate = 
    DIVIDE(
        CALCULATE(COUNTROWS(Churn), Churn[Churned] = TRUE),
        COUNTROWS(Churn)
    )

Lifetime Value (LTV) = [ARPU] * [Average Customer Lifespan (Months)]
```

---

## 🔐 Data Privacy

All data is anonymized for demonstration purposes and does not contain personally identifiable information (PII). Use of row-level security (RLS) is supported for real implementation.

---

## 👨‍💼 Author

**Mohammad Zakirul Islam Khan**  
📍 Vancouver, BC, Canada  
📧 zakirul.islam973@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mzik)  
🔗 [GitHub](https://github.com/data-analyst-portfolio-web)
