# Module 04: Data Classification Taxonomy & Security Mapping

This directory establishes the formal security classification framework applied across our global travel platform's data assets to ensure strict regulatory compliance.

---

## 1. Enterprise Security Classification Levels

### Tier 1: Confidential / PII (Personally Identifiable Information)
*   **Definition:** Highly sensitive data elements that can uniquely identify an individual. Subject to strict GDPR rules.
*   **Data Fields Mapped:** `full_name`, `email_address` (from our customer identity assets)
*   **Access Control Rule:** Restrict direct access; data must be masked or pseudonymized before entering analytics environments.

### Tier 2: Internal Use Only
*   **Definition:** Operations data that does not contain personal identity but belongs to internal commercial operations.
*   **Data Fields Mapped:** `booking_id`, `vendor_property_id`, `payment_status_flag`
*   **Access Control Rule:** Accessible to internal employee roles with active business justifications.

### Tier 3: Public
*   **Definition:** Non-sensitive, aggregate operational metadata that poses zero risk if shared externally.
*   **Data Fields Mapped:** Country currency conversion rates, standardized ISO regional codes (`country_residence`).

---

## 2. Regulatory Compliance Target Mapping
To verify that our technical pipelines match this policy, our classification labels map directly to the physical system architecture tracked in `03_metadata_management/technical_dictionary.md`.
