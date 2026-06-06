# Module 01: Business Context & Data Ownership Charter

## 1. Governance Domain Scope: Core Travel Platform
This module establishes clear, non-technical organizational ownership across our global travel platform's core data assets.

### A. Customer Operations Sub-Domain
* **Operational Boundary:** Manages user identity verification, authentication, profile preferences, and geographical residence records.
* **Business Owner:** VP of Customer Success
* **Data Steward Group:** Customer Identity Operations (ID-Ops) Team
* **Technical Custodian:** IAM Engineering Team

### B. Core Booking Ledger Sub-Domain
* **Operational Boundary:** Manages reservation events, cross-vendor inventory checks (hotels, car rentals), currency exchanges, and transaction tracking.
* **Business Owner:** VP of Core Finance
* **Data Steward Group:** Ledger Integrity Team
* **Technical Custodian:** Transaction Pipelines Team

---

## 2. Accountability Matrix (RACI)
To prevent regulatory or compliance gaps, this matrix defines data ownership and responsibilities when pipeline changes occur.

| Functional Activity | Business Owner | Data Steward | Analytics Lead | Compliance/Legal CoE |
| :--- | :---: | :---: | :---: | :---: |
| **Modifying Production Schema** | Accountable | Responsible | Consulted | Informed |
| **Re-classifying PII Fields** | Accountable | Responsible | Informed | Consulted |
| **Updating Data Retention Limits** | Informed | Responsible | Informed | Accountable |

* **R:** Responsible (Does the work) | **A:** Accountable (Approves/Signs off) | **C:** Consulted (Provides input) | **I:** Informed (Kept up to date)*
