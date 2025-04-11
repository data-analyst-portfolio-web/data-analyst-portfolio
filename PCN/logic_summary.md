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


---

## 3. Freight & Facility Charge Logic

Calculates location-specific freight and facility fees based on site ID and product.

```excel
=IF(
   AND(A28<>521400,A28<>529519,A28<>519378,A28<>519382,A28<>519380,A28<>519357,
       A28<>521399,A28<>519373,A28<>519370,A28<>519371,A28<>519377,A28<>519387,
       A28<>521176,A28<>521177,A28<>519355,A28<>524588),
   0,
   IF(D28="UNBRAND DEF", 0, HLOOKUP(A28, FrtFac, 2, FALSE))
)
```

---

## 4. GST/HST Tax Calculation Logic

This formula applies conditional GST/HST rules for UNBRAND DEF products and uses lookup for others.

```excel
=IF(
   AND(C28="BC", D28="unbrand def"), 0.12,
   IF(AND(C28="SK", D28="unbrand def"), 0.11,
   IF(AND(C28="MB", D28="unbrand def"), 0.13,
   VLOOKUP(C28, TAXTABLE, 2, FALSE)))
)
```

---

## 5. PST/QST Tax Lookup Logic

Province-specific PST or QST tax lookup.

```excel
=VLOOKUP(C28, TAXTABLE, 3, FALSE)
```

---

## 6. Address Lookup Logic

Fetches the customer location’s full address using the site number.

```excel
=VLOOKUP(A28, EFS_SITE, 4, FALSE)
```
```


### 🔍 Formula Breakdown: Base Price Calculation

This formula selects the correct **base rack price** based on site number and fuel type. The logic branches depending on the site ID and product type.

---

### 🧠 Explanation:

- **`A28`** = Site number (location identifier)
- **`D28`** = Fuel product type

---

### 🚩 Step-by-Step Logic:

1. **If `A28` matches one of the known site IDs**:
    - These sites use **Kamloops pricing structure**.
    - Check the product type (`D28`) and return one of the following:
      - `kdrk` for diesel-type fuels (BIODIESEL, DIESEL LS, etc.)
      - `krrk` for regular gasoline (REGULAR, ETHANOL REG, etc.)
      - `DEFbase` for UNBRAND DEF
      - `kprk` as default fallback

2. **If `A28` is specifically 519355 (a Vancouver location)**:
    - Apply **Vancouver pricing structure**:
      - `vdrk` for diesel-type
      - `vrrk` for regular fuel types

3. **If no site match is found**:
    - Return value from `E28` (presumably a default/fallback rack price or user input)

---

This modular structure allows pricing to be automatically pulled based on city logic and refined by product type, ensuring robust and flexible base price assignment.
