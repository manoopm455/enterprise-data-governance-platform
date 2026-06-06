# Module 03: Technical Metadata Dictionary & Schema Specifications

This file establishes the physical metadata layer mapping directly to the data assets stored within our catalog (`02_data_catalog/`).

---

## 1. Physical Schema Map: `sample_hotel_bookings.csv`
* **Object Name:** `hotel_bookings`
* **Data Domain:** Booking Ledger
* **Assigned Data Steward Group:** Ledger Integrity Team

| Physical Column Name | Database Data Type | Primary / Foreign Key | Is Nullable | Assigned Business Definition Mapping |
| :--- | :--- | :---: | :---: | :--- |
| `booking_id` | VARCHAR(64) | **PK** | NO | Unique internal alphanumeric booking voucher code. |
| `customer_id` | VARCHAR(64) | **FK** | NO | Relational link tying back to the master customer registry. |
| `vendor_property_id` | VARCHAR(32) | NO | NO | External vendor identification code for the specific hotel property. |
| `check_in_date` | DATE | NO | NO | Scheduled operational arrival date at the vendor location. |
| `total_price_usd` | NUMERIC(10,2) | NO | NO | Gross transaction amount processed in USD baseline currency. |
| `payment_status_flag` | VARCHAR(32) | NO | NO | Real-time billing validation states (`PENDING`, `SETTLED`, `REFUNDED`). |

---

## 2. Technical Schema Validation Policy
To maintain data pipeline integrity, any adjustments or additions to this schema layout must adhere to these programmatic rules:
1. **Case Style:** All physical column names must use strict lower `snake_case` notation.
2. **Key Requirements:** Every transaction table must explicitly declare a non-nullable Primary Key (`PK`).
3. **Null Constraints:** Financial metrics (such as `total_price_usd`) must be marked as `NOT NULL` to ensure downstream pipeline calculations do not fail.
