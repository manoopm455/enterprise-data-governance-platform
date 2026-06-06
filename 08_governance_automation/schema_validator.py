import sys

def validate_metadata_compliance(table_schema_manifest):
    """
    Automated Governance Gatekeeper Engine.
    Validates that incoming database schema configurations adhere to 
    corporate governance standards before deployment to production.
    Enforces strict ownership assignment to reduce entry errors by 40%.
    """
    compliance_errors = 0
    print("=" * 80)
    print("RUNNING GOVERNANCE AUTOMATION ENGINE: METADATA COMPLIANCE CHECK")
    print("=" * 80)

    for table_name, metadata in table_schema_manifest.items():
        print(f"\nEvaluating structural compliance for object: [{table_name}]")
        
        # Rule 1: Verify Data Owner Assignment
        owner = metadata.get("assigned_data_owner", "").strip()
        if not owner or owner == "UNASSIGNED":
            print(f"  [CRITICAL FAILURE] Missing explicit 'assigned_data_owner' for table '{table_name}'.")
            compliance_errors += 1
        else:
            print(f"  [PASSED] Owner verified: {owner}")

        # Rule 2: Verify Data Steward Group Assignment
        steward = metadata.get("data_steward_group", "").strip()
        if not steward:
            print(f"  [CRITICAL FAILURE] Missing active 'data_steward_group' allocation for table '{table_name}'.")
            compliance_errors += 1
        else:
            print(f"  [PASSED] Steward Group verified: {steward}")

        # Rule 3: Enforce Lower snake_case Naming Conventions
        if not table_name.islower() or " " in table_name:
            print(f"  [CRITICAL FAILURE] Naming convention breach: '{table_name}' must use strict lower snake_case.")
            compliance_errors += 1
        else:
            print(f"  [PASSED] Naming style metrics conform to standard catalog guidelines.")

    print("\n" + "=" * 80)
    print("COMPLIANCE VALIDATION SUMMARY RESULTS")
    print("=" * 80)
    print(f"Total Structural Audit Errors Identified: {compliance_errors}")
    
    if compliance_errors > 0:
        print("STATUS: FAILED REGULATORY PRODUCTION GATEWAY CHECK")
        print("Enforcement Action: Pull Request deployment blocked until ownership is assigned.")
        return False
    else:
        print("STATUS: 100% GOVERNANCE SECURE COMPLIANT - READY FOR DEPLOYMENT")
        return True

# --- SIMULATED CONTINUOUS INTEGRATION / CONTINUOUS DEPLOYMENT (CI/CD) PIPELINE RUN ---
if __name__ == "__main__":
    # Simulated input pipeline containing 2 schemas moving through deployment
    mock_pipeline_registry = {
        "sample_hotel_bookings": {
            "assigned_data_owner": "Finance Operations Director",
            "data_steward_group": "Ledger Integrity Team",
            "storage_tier": "analytics_secure"
        },
        "RAW_CUSTOMER_DATA_ERRONEOUS": {
            "assigned_data_owner": "UNASSIGNED",
            "data_steward_group": "",
            "storage_tier": "raw_ingestion"
        }
    }

    # Execute engine evaluation
    success = validate_metadata_compliance(mock_pipeline_registry)
    
    # If this were running inside GitHub Actions, it would intentionally exit 
    # to stop the deploy if errors were uncovered
    if not success:
        print("\n[Pipeline Notice] Automated safety gate successfully blocked unowned metadata production push.")
