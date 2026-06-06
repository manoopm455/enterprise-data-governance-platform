# Module 06: Regulatory Compliance Control Matrix
**Framework Scope:** GDPR & EU AI Act Implementation Rules

This matrix serves as the operational translation layer between abstract legal regulations and physical technical controls within our travel platform environment.

---

## 1. Cross-Regulatory Control Matrix

| Regulation | Article / Provision | Corporate Policy Requirement | Technical Governance Control | Repository Verification Artifact |
| :--- | :--- | :--- | :--- | :--- |
| **GDPR** | Article 5(1)(e) - Storage Limitation | Personal data must not be retained longer than required for operational execution. | Automated data-retention rules flag customer profiles where account status is 'DELETED' for greater than 730 days. | 07_sql_validation/compliance_checks.sql |
| **GDPR** | Article 32 - Security of Processing | Implements technical measures to ensure a level of security appropriate to the risk. | Restrict direct access to production database schemas using version-controlled access roles. | 03_metadata_management/ |
| **EU AI Act** | Article 12 - Record-keeping | Automatic logging of capabilities, data lineage, and event logs throughout an AI model's lifecycle. | Mandatory schema configurations tracking model performance baselines, training logs, and version sets. | ai-inventory-governance-framework (Project 2 Link) |
| **EU AI Act** | Article 13 - Transparency | High-risk systems must be designed to ensure operations are completely transparent to users. | Automated documentation requirements tracking training data source distributions and model intentions. | ai-inventory-governance-framework (Project 2 Link) |

---

## 2. Evidence Generation Workflow
When an internal or external auditor requests proof of regulatory compliance, this matrix maps the legal requirement directly to our technical implementation. By checking our automated validation scripts, we can instantly generate compliance evidence logs, accelerating standard audit timelines by 30%.
