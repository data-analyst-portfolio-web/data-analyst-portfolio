
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

## 3. Group Pricing Logic

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
