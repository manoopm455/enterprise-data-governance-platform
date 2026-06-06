# Module 10: Governance Change Management Policy & Workflow
**Document Classification:** Standard Operating Procedure (SOP)
**Scope:** Updates to Corporate Metadata Specifications, Glossaries, and Validation Automation

To guarantee 100% data audit traceability, any changes, updates, or deletions to our data assets, classification schemas, or validation rules must adhere strictly to this Git-based version control operational workflow.

---

## 1. Step-by-Step Production Change Lifecycle

[Main Branch] ──────► Create Feature Branch ──────► Update Metadata/SQL File
                            (e.g., feat/add-ledger)               │
                                                                   ▼
[Main Production] ◄─── Automated CI/CD Passes ◄─── Peer Review / Steward Sign-off
   (Updated Asset)        (Folder 08 Script Runs)        (Pull Request Created)

---

## 2. Operational Workflow Execution Steps

### Step 1: Isolation (Branch Creation)
* **Action:** Developers or Data Stewards must never commit directly to the `main` branch. All modifications must occur in a dedicated feature branch.
* **Naming Standard:** `governance/update-[module]-[topic]` (e.g., `governance/update-03-hotel-ledger`).

### Step 2: Implementation & Modification
* **Action:** Execute changes directly inside the relevant markdown files, technical dictionaries, or script modules.
* **Commit Message Standard:** Every commit must include a clear change justification prefix (e.g., `docs: updated total_price_usd type constraint for legal clearance`).

### Step 3: Automated Peer Review & Gating
* **Action:** Submit a GitHub Pull Request (PR) from the feature branch to the `main` production branch.
* **Automated Validation:** The submission instantly triggers our programmatic schema check script (`08_governance_automation/schema_validator.py`). If the script discovers unassigned metadata or naming convention breaches, the deploy gateway blocks compilation automatically.

### Step 4: Data Steward Sign-Off (The Human Element)
* **Action:** A formal peer review and approval must be completed by an appointed member of the Assigned Data Steward Group before a pull request can be merged.

### Step 5: Merge & Immutable Historical Audit Trail
* **Action:** Once both automated and human gates pass, the PR is merged into `main`. GitHub logs an irreversible, time-stamped history of who requested the change, who reviewed it, and exactly what lines of code were modified. This provides a 100% audit-ready trail for external regulatory body inspections.
