
# 🧠 Logic Summary - Price Change Notification System

This document explains the key logic and formula structures behind the Excel-based PCN (Price Change Notification) system used by Cool Creek Energy.

---

## 1. Base Price Calculation Logic

**Inputs:**
- `Rack Price` by city (Kamloops, Calgary, etc.)
- `Freight & Facility` charges (site-specific)
- `Markup` per customer group (C0–C5)

**Example Formula:**

```excel
=IF(
   OR(A28 = 521400, A28 = 529519, A28 = 519378, A28 = 519382, A28 = 519380, 
      A28 = 519357, A28 = 549727, A28 = 519373, A28 = 519370, A28 = 519371, 
      A28 = 519377, A28 = 519387, A28 = 521176, A28 = 521177, A28 = 524588),
   IF(
      OR(D28 = "BIODIESEL", D28 = "BIODIESEL DYED", D28 = "DIESEL LS", D28 = "D LS DYED"),
      kdrk,
      IF(
         OR(D28 = "ETHANOL REG", D28 = "REGULAR", D28 = "REG DYED", D28 = "ETH REG DYE"),
         krrk,
         IF(D28 = "UNBRAND DEF", DEFbase, kprk)
      )
   ),
   IF(
      A28 = 519355,
      IF(
         OR(D28 = "BIODIESEL", D28 = "BIODIESEL DYED", D28 = "DIESEL LS", D28 = "D LS DYED"),
         vdrk,
         IF(
            OR(D28 = "ETHANOL REG", D28 = "REGULAR", D28 = "REG DYED", D28 = "ETH REG DYE"),
            vrrk,
            ""
         )
      ),
      E28
   )
)
```

---

## 2. Group Pricing Logic (C1–C5)

Each group sheet (`C1 Group`, `C2 Group`, etc.) calculates final prices using group-specific markups from the **Input Data** sheet. These tiers allow differentiated pricing by customer level.

---

### 🧮 C1 Pricing Formula:

```excel
=IF(
   OR(D28 = "BIODIESEL", D28 = "BIODIESEL DYED", D28 = "DIESEL LS", D28 = "D LS DYED"), _dsl1 + N28,
   IF(D28 = "ETHANOL REG", _ereg1 + N28,
   IF(D28 = "REGULAR", _reg1 + N28,
   IF(D28 = "PREM DYED", _puld1 + N28,
   IF(D28 = "PREMIUM", _punl1 + N28,
   IF(D28 = "REG DYED", _unld1 + N28,
   IF(D28 = "ETH REG DYE", _unld1 + N28,
   IF(D28 = "ETH MID", _mid1 + N28,
   IF(D28 = "MID", _mid1 + N28,
   IF(D28 = "UNBRAND DEF", _def1 + N28, ""))))))))))
+
IF(
   OR(A28 = 521400, A28 = 529519, A28 = 519378, A28 = 519382, A28 = 519380, A28 = 519357,
      A28 = 549727, A28 = 519373, A28 = 519370, A28 = 519371, A28 = 519377, A28 = 519387,
      A28 = 521176, A28 = 521177, A28 = 524588),
   AE28,
   IOL
)
```

---

### 🔍 Explanation:

- **D28 = Product type** → Chooses the correct group-specific markup (`_dsl1`, `_ereg1`, `_reg1`, etc.)
- **N28 = Freight & Facility charges**
- **A28 = Site ID** → Determines which freight logic to apply
- **AE28 / IOL** = Final tax or adjustment factor depending on site

---

### ✅ Final Group Net Price:
```
Final Price = Base Price + Freight/Facility (N28) + Group Markup (_xxx1) + Tax/PST/GST (AE28 or IOL)
```
