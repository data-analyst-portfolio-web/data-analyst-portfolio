# 📘 Telecom Profitability & Customer Segmentation Dashboard

A Power BI dashboard project designed to deliver **insights into profit trends, customer value, churn indicators**, and usage segmentation across telecom services. It supports strategic decisions by transforming raw subscriber and usage data into actionable KPIs and visual narratives.

---

## 🚀 Project Objective

Enable telecom stakeholders to:
- Identify high and low-margin customer groups.
- Monitor revenue and cost trends across services and regions.
- Track churn risks and retention outcomes.
- Segment customers based on engagement, ARPU, and lifecycle.

---

## 🧰 Tools & Technologies

| Tool       | Purpose                                 |
|------------|------------------------------------------|
| Power BI   | Dashboard design and KPI visualization   |
| SQL Server | Data transformation and modeling         |
| DAX        | Calculated columns, measures, time logic |
| Python (opt.) | Segmentation, churn scoring models    |

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
├── data/
│   ├── raw/
│   ├── processed/
├── scripts/
├── visuals/
├── report/
├── docs/
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

## 🔐 Notes
- Customer and account data is anonymized for demo purposes.
- Dashboards support row-level security and date hierarchies.
