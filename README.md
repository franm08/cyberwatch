# 💻 **Cyber Risk & Compliance Tracker**

---

## 🚨 **Project Overview**

In a digital-first world, evaluating vendor cybersecurity posture is essential. This system enables teams to **log incidents**, **monitor compliance**, and **export auditable reports** in alignment with critical frameworks like **SOC2**, **NIST**, **GDPR**, **CCPA**, and **CMMC**.

---

## ✅ **Features**

1. **Vendor Compliance Scoring**  
   Evaluates vendors on six cybersecurity criteria, including encryption, PII storage, and certifications.

2. **Incident Logging**  
   Tracks and categorizes security incidents by type, severity, and response actions.

3. **Compliance Dashboard**  
   Computes an overall compliance score to gauge organizational security health.

4. **CSV Export**  
   Exports vendor, incident, and compliance data into CSV files for audits or reporting.

5. **React Frontend**  
   Clean, responsive dashboard for real-time monitoring and input.

---

## ⚙️ **How It Works**

### 🏢 **Step 1: Vendor Assessment**  
User submits vendor details (e.g., SOC2 certified, GDPR compliant). Each `true` boolean earns **1 point**. Total score determines the vendor’s compliance level.

### 🧯 **Step 2: Incident Logging**  
Security incidents are logged with **severity**, **type**, and **mitigation response**. These entries help track risk trends and assess organizational exposure.

### 📊 **Step 3: Score Computation**  
The backend aggregates all vendor data to compute an **overall compliance percentage**.

### 📤 **Step 4: Export**  
A single API call triggers **CSV generation** for all vendor and incident data — ready for compliance reporting.

---

## 🛠️ **Setup Instructions**

### 📦 **1. Prerequisites**

- Python 3.8+  
- Node.js 18+  
- npm  
- Git (optional)

---

### 🔙 **2. Backend Setup**

```bash
git clone https://github.com/your-username/cyber-risk-tracker.git
cd cyber-risk-tracker/backend
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install flask flask-cors
python app.py
```

Flask API runs at: **http://127.0.0.1:5000**

---

### 🎛️ **3. Frontend Setup**

```bash
cd ../frontend
npm install
npm start
```

React frontend runs at: **http://localhost:3000**

---

## 📜 **License**

This project is licensed under the **MIT License** — feel free to use or adapt for educational or organizational purposes.
