from flask import Flask, request, jsonify
from models import log_incident, incident_log
from models import add_vendor, vendor_profiles
from models import calculate_compliance_score
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Cyber Risk Tracker running!"}

@app.route("/log-incident", methods=["POST"])
def log_incident_route():
    data = request.get_json()
    logged = log_incident(data)
    return jsonify({"message": "Incident logged", "incident": logged})

@app.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify({"incidents": incident_log})

@app.route("/add-vendor", methods=["POST"])
def add_vendor_route():
    data = request.get_json()
    scored = add_vendor(data)
    return jsonify({"message": "Vendor added", "vendor": scored})

@app.route("/vendors", methods=["GET"])
def get_vendors():
    return jsonify({"vendors": vendor_profiles})

@app.route("/compliance", methods=["GET"])
def get_compliance_score():
    return jsonify(calculate_compliance_score())

import csv

@app.route("/export", methods=["GET"])
def export_all():
    if not vendor_profiles or not incident_log:
        return jsonify({"error": "No data to export"}), 400

    # Export vendors
    with open("vendors.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=vendor_profiles[0].keys())
        writer.writeheader()
        writer.writerows(vendor_profiles)

    # Export incidents
    with open("incidents.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=incident_log[0].keys())
        writer.writeheader()
        writer.writerows(incident_log)

    # Export compliance
    with open("compliance.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["compliance_score"])
        writer.writeheader()
        writer.writerow(calculate_compliance_score())

    return jsonify({"message": "✅ Exported all CSVs"})

if __name__ == "__main__":
    app.run(debug=True)