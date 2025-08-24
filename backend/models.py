incident_log = []  # Temporary in-memory log

def log_incident(incident):
    incident_log.append(incident)
    return incident

vendor_profiles = []

def score_vendor(vendor):
    score = 0
    if vendor.get("stores_pii"):
        score += 2
    if not vendor.get("has_encryption"):
        score += 2
    if not vendor.get("soc2_certified"):
        score += 1
    if not vendor.get("gdpr_compliant"):
        score += 1
    if not vendor.get("ccpa_compliant"):
        score += 1
    if not vendor.get("cmmc_compliant"):
        score += 1

    # Add score to vendor and return
    vendor["risk_score"] = score
    return vendor

def add_vendor(vendor):
    scored = score_vendor(vendor)
    vendor_profiles.append(scored)
    return scored

def calculate_compliance_score():
    score = 100

    # Subtract points if vendors are non-compliant
    for vendor in vendor_profiles:
        score -= vendor.get("risk_score", 0)

    # Subtract points for high-severity incidents
    for incident in incident_log:
        if incident.get("severity", "").lower() == "high":
            score -= 5
        elif incident.get("severity", "").lower() == "medium":
            score -= 3
        elif incident.get("severity", "").lower() == "low":
            score -= 1

    # Bound the score between 0 and 100
    score = max(0, min(score, 100))
    return {"compliance_score": score}