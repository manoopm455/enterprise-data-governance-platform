-- =====================================================================
-- ENTERPRISE DATA GOVERNANCE: REPEATABLE COMPLIANCE VALIDATION OPERATIONS
-- Target Database Clusters: prod_customer_cluster & prod_ledger_db
-- Objective: Automate detection of orphaned assets and retention leaks
-- =====================================================================

-- CHECK 1: COMPLIANCE METADATA ANOMALIES (Orphaned Assets)
-- Flags any active table in the system that violates our mandate by missing an assigned Steward Group
SELECT 
    table_catalog,
    table_schema,
    table_name,
    data_steward_group,
    assigned_data_owner
FROM 
    enterprise_metadata_catalog.information_schema.tables
WHERE 
    data_steward_group IS NULL 
    OR assigned_data_owner = 'UNASSIGNED'
    OR assigned_data_owner = '';


-- CHECK 2: DATA QUALITY TRANSACTION INTEGRITY
-- Flags any billing records where financial amounts are negative or missing
-- This enforces our structural quality standards across upstream data pipelines
SELECT 
    booking_id,
    customer_id,
    total_price_usd,
    payment_status_flag
FROM 
    prod_ledger_db.booking_zone.hotel_bookings
WHERE 
    total_price_usd <= 0.00 
    OR total_price_usd IS NULL;


-- CHECK 3: GDPR RETENTION ENGINE AUDIT (Article 5 Compliance)
-- Identifies any customer profile records where the account was marked 'DELETED'
-- but the system has failed to purge the record after the legal 2-year (730 days) limit
SELECT 
    customer_id,
    account_status,
    account_deletion_date,
    DATEDIFF(CURRENT_DATE(), account_deletion_date) AS days_retained_post_deletion
FROM 
    prod_customer_cluster.identity_zone.raw_customers
WHERE 
    account_status = 'DELETED'
    AND DATEDIFF(CURRENT_DATE(), account_deletion_date) > 730;
