# 📊 Operations Dashboard for Fuel KPIs (Power BI)

## 🧭 Project Overview

This Power BI dashboard monitors and analyzes key operational metrics for fuel delivery services. It consolidates data from truck dispatch systems, tank telemetry, and delivery confirmations to provide actionable insights into efficiency, performance, and risk areas.

---

## 🎯 Business Problem

Fuel delivery operations often suffer from inefficiencies including untracked idle time, delivery delays, and tank fill inconsistencies. This dashboard addresses those issues by delivering real-time, data-driven operational insights.

---

## 🔍 KPIs & Metrics Tracked

### 🚚 Truck Utilization
- Ideal vs Actual Efficiency
- Idle Time %
- Miles per Gallon / Volume Delivered

### 📦 Delivery Performance
- On-Time vs Late Deliveries
- Total Deliveries by Region/Day
- Missed Deliveries Rate

### 🛢️ Tank Monitoring
- Average Fill % by Site
- Emergency Delivery Frequency
- Site Ranking by Consumption

---

## ⚙️ Tools & Techniques

| Tool        | Description                                              |
|-------------|----------------------------------------------------------|
| **Power BI**| Interactive dashboard creation, data modeling            |
| **DAX**     | Time intelligence, KPI calculations                      |
| **SQL**     | ETL from operations systems                              |
| **Excel/CSV**| Lookup/reference tables                                 |

---

## 📈 Outcome

- Reduced fuel delivery idle time by **18%**
- Improved tracking of tank fill levels and emergency risks
- Enabled real-time dispatch efficiency reviews
- Provided automated weekly executive insights

---

## 📐 Power BI Layout & DAX Measures

This dashboard is organized across four key pages, each serving a unique aspect of fuel delivery operations.

---

### 📄 Overview Page
**Filters**: Date, Region, Product, Customer Type  
**Visuals**:
- Line chart: Monthly Delivery Trend
- Bar chart: Volume by Region
- KPIs: Total Deliveries, On-Time %, Late Deliveries

#### Sample DAX:
```DAX
Total Deliveries = COUNT(delivery_summary[Delivery_ID])

On-Time Delivery % = 
DIVIDE(
    CALCULATE(COUNT(delivery_summary[Delivery_ID]), delivery_summary[Status] = "On Time"),
    [Total Deliveries]
)
```

---

### 🛢️ Tank Monitoring Page
**Filters**: Tank, Region, Fuel Type  
**Visuals**:
- Gauge: Tank Fill Level
- Bar Chart: Refill Frequency
- Table: Tank Logs

#### Sample DAX:
```DAX
Fill % = 
DIVIDE(
    tank_fill_logs[Volume_Filled_Liters], 
    RELATED(tank_metadata[Max_Capacity_Liters])
) * 100
```

---

### 🚚 Delivery Performance Page
**Filters**: Driver, Date, Customer Type  
**Visuals**:
- Card: Avg. Delivery Volume
- Table: Delivery Logs
- KPI: Exceptions, Delay %

#### Sample DAX:
```DAX
Average Delivery Volume = 
AVERAGE(delivery_summary[Volume_Liters])
```

---

### 🔧 Truck Efficiency Page
**Filters**: Truck ID, Region, Fuel Type  
**Visuals**:
- Cards: Distance Traveled, Fuel Used, Efficiency
- Bar Chart: Idle Time %

#### Sample DAX:
```DAX
Avg. Fuel Efficiency = 
DIVIDE(SUM(truck_routes[Distance_KM]), SUM(truck_routes[Fuel_Used_Liters]))

Idle Time % = 
DIVIDE(SUM(truck_routes[Idle_Minutes]), SUM(truck_routes[Idle_Minutes] + truck_routes[Driving_Minutes]))
```

---

These measures and visuals collectively allow stakeholders to monitor fuel operations, reduce inefficiencies, and take action based on real-time insights.

---

## 🧾 Sample Dashboard & Screenshots

### 📘 Summary of Dashboard

![Summary of Dashboard](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/CL%20Summary%20Report.PNG)

### 📘 Tank Monitoring

![Tank Monitoring](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/CL%20Summary%20Report.PNG)

### 📘 Delivery Performance

![Delivery Performance](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/CL%20Summary%20Report.PNG)

### 📘 Truck Efficiency

![Truck Efficiency](https://github.com/data-analyst-portfolio-web/data-analyst-portfolio/blob/main/Automated%20ERP-Based%20Monthly%20Transactional%20Reporting/Images/CL%20Summary%20Report.PNG)


## 👨‍💼 Author

**Mohammad Zakirul Islam Khan**  
📍 Vancouver, BC, Canada  
📧 zakirul.islam973@gmail.com  
[LinkedIn](https://www.linkedin.com/in/mzik)  
[GitHub](https://github.com/data-analyst-portfolio-web)
