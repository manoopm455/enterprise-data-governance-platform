# Module 05: Column-Level Data Lineage Map
**Pipeline Scope:** Ingestion Zone to Analytics View Transformation

This lineage map traces the end-to-end lifecycle of our customer data fields. It provides a technical audit trail showing exactly how raw data elements flow from our structural sources into final analytical reporting layers.

---

## 1. Upstream to Downstream Pipeline Architecture Map

[Raw Ingestion Tier]           [Transformation Engine]          [Secured Analytics Layer]
(Database: prod_raw)           (Governance Policies)             (View: analytics_secure)
        │                                 │                                │
        ├─── full_name ───────────────────┼───► SHA-256 Hashing ───────────┼──► full_name_hashed
        │                                 │                                │
        └─── email_address ───────────────┼───► Full Redaction ────────────┼──► email_address_masked

---

## 2. Detailed Column-Level Dependency Matrix

### Target View Object: analytics_secure.customer_reporting_view
* **Downstream Access Level:** Open Analytics & Internal Data Science Teams
* **Upstream Core Source:** prod_raw.raw_customers (Mapped from our catalog inventory)

| Target Column Name (Downstream) | Source Column Name (Upstream) | Data Transformation Applied | Governance Enforcement Rule |
| :--- | :--- | :--- | :--- |
| customer_id | customer_id | Direct Pass-Through | Kept as system primary key. Non-identifiable hash string. |
| full_name_hashed | full_name | SHA-256 Hashing | GDPR Enforced: Replaces raw names with static irreversible alphanumeric tokens. |
| email_address_masked | email_address | Full String Constant Substitution | PII Protection Rule: Completely overwrites communication pathways in analytics environments. |
| country_residence | country_residence | Direct Pass-Through | Public attribute. Retained for regional reporting boundaries. |

---

## 3. Data Flow Traceability Verification
* **System Input Audit Link:** Maps directly back to physical schemas defined in 03_metadata_management/technical_dictionary.md.
* **Classification Input Link:** Follows security tiers mapped out in 04_data_classification/security_classification.md.
