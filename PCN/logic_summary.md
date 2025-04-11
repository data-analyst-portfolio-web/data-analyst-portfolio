
# 🧠 Logic Summary - Price Change Notification System

This document explains the key logic and formula structures behind the Excel-based PCN (Price Change Notification) system used by Cool Creek Energy.

---


## 1. Base Price Calculation Logic (Updated)

This formula determines the base rack price depending on the **site ID** (location) and **product type**:

```excel
=IF(
  OR(A28=521400, A28=529519, A28=519378, A28=519382, A28=519380, A28=519357, A28=549727, A28=519373, A28=519370, A28=519371, A28=519377, A28=519387, A28=521176, A28=521177, A28=524588),
  IF(
    OR(D28="BIODIESEL", D28="BIODIESEL DYED", D28="DIESEL LS", D28="D LS DYED"),
    kdrk,
    IF(
      OR(D28="ETHANOL REG", D28="REGULAR", D28="REG DYED", D28="ETH REG DYE"),
      krrk,
      IF(D28="UNBRAND DEF", DEFbase, kprk)
    )
  ),
  IF(
    A28=519355,
    IF(
      OR(D28="BIODIESEL", D28="BIODIESEL DYED", D28="DIESEL LS", D28="D LS DYED"),
      vdrk,
      IF(
        OR(D28="ETHANOL REG", D28="REGULAR", D28="REG DYED", D28="ETH REG DYE"),
        vrrk,
        ""
      )
    ),
    E28
  )
)
```

**Site Groups:** Kamloops-related and Vanderhoof (519355)  
**Product Groups:** Diesel, Gasoline (Regular, Mid), DEF  
**Fallback:** Uses E28 if no conditions are met.


**Inputs:**
- `Rack Price` by city (Kamloops, Calgary, etc.)
- `Freight & Facility` charges (site-specific)
- `Markup` per customer group (C0–C5)

**Example Formula:**
```excel
=IF(AND(A28=site_list,...), IF(D28="BIODIESEL", base_value, ...), fallback)
```

---

## 2. Tax Calculation

**Tax logic includes:**
- Federal (Excise)
- Provincial (PST, QST)
- Carbon and Local Taxes
- GST/HST from `TAXTABLE`

**Examples:**
```excel
=VLOOKUP(C28, TAXTABLE, 2, FALSE) ' GST
=VLOOKUP(C28, TAXTABLE, 3, FALSE) ' PST
```

---


## 3. Group Pricing Logic (Updated - C1 Group Example)

Sheets like `C1 Group`, `C2 Group`, etc., reference group-specific markup tiers calculated in the `Input Data` sheet.

**Pricing Formula:**
```
Final Price = Net Price + Freight + Markup + Taxes
```

**C1 Group Example Formula:**
```excel
=IF(
  OR(D28="BIODIESEL", D28="BIODIESEL DYED", D28="DIESEL LS", D28="D LS DYED"),
  _dsl1 + N28,
  IF(D28="ETHANOL REG", _ereg1 + N28,
    IF(D28="REGULAR", _reg1 + N28,
      IF(D28="PREM DYED", _puld1 + N28,
        IF(D28="PREMIUM", _punl1 + N28,
          IF(D28="REG DYED", _unld1 + N28,
            IF(D28="ETH REG DYE", _unld1 + N28,
              IF(D28="ETH MID", _mid1 + N28,
                IF(D28="MID", _mid1 + N28,
                  IF(D28="UNBRAND DEF", _def1 + N28)
                )
              )
            )
          )
        )
      )
    )
  )
)
+
IF(
  OR(A28=521400, A28=529519, A28=519378, A28=519382, A28=519380, A28=519357, A28=549727, A28=519373, A28=519370, A28=519371, A28=519377, A28=519387, A28=521176, A28=521177, A28=524588),
  AE28,
  IOL
)
```

- `_dsl1, _ereg1, _reg1`, etc.: Group-specific markups  
- `N28`: Net price (typically base price)  
- `AE28 / IOL`: Freight component depending on site


Sheets like `C1 Group`, `C2 Group`, etc., reference group-specific markup tiers calculated in the `Input Data` sheet.

**Pricing Formula:**
```
Final Price = Net Price + Freight + Markup + Taxes
```

---

## 4. Site Lookup & Address Mapping

Pulls address and metadata based on `Site Number` from the `EFS_SITE` sheet.

```excel
=VLOOKUP(A28, EFS_SITE, 4, FALSE)
```

---

## 5. VBA Automation (Macros)

### RCPSORT
Cleans and imports trimmed site-specific data.

### Import
Transfers daily CSV-pasted data into the main processing sheet.

```vba
' See macro_code.vba for full scripts
```
