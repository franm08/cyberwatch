# models.py

# Dummy incident log
incident_log = [
    {
        "type": "Phishing",
        "severity": "High",
        "date": "2025-08-23",
        "response": "Employee training and system lockdown"
    }
]

# Dummy vendor profiles
vendor_profiles = [
    {
        "name": "VendorX",
        "stores_pii": True,
        "has_encryption": True,
        "soc2_certified": True,
        "gdpr_compliant": True,
        "ccpa_compliant": True,
        "cmmc_compliant": True
    }
]

# Function to add a vendor
def add_vendor(data):
    vendor_profiles.append(data)
    return data

# Function to log an incident
def log_incident(data):
    incident_log.append(data)
    return data

# Function to calculate compliance score
def calculate_compliance_score():
    if not vendor_profiles:
        return {"compliance_score": 0}

    total_score = 0
    for vendor in vendor_profiles:
        score = sum([
            vendor.get("soc2_certified", False),
            vendor.get("gdpr_compliant", False),
            vendor.get("ccpa_compliant", False),
            vendor.get("cmmc_compliant", False)
        ])
        total_score += score / 4 * 100  # Average compliance per vendor

    average_score = round(total_score / len(vendor_profiles))
    return {"compliance_score": average_score}