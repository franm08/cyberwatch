import React, { useEffect, useState } from "react";
import { getVendors, getIncidents, getCompliance } from "./api";

export default function Dashboard() {
  const [vendors, setVendors] = useState([]);
  const [incidents, setIncidents] = useState([]);
  const [compliance, setCompliance] = useState(null);

  useEffect(() => {
    getVendors().then(data => setVendors(data.vendors || []));
    getIncidents().then(data => setIncidents(data.incidents || []));
    getCompliance().then(data => setCompliance(data.compliance_score));
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Cyber Risk Dashboard</h1>

      <h2>Vendors</h2>
      <ul>
        {vendors.map((v, idx) => (
          <li key={idx}>{v.name} (Risk: {v.risk_score})</li>
        ))}
      </ul>

      <h2>Incidents</h2>
      <ul>
        {incidents.map((i, idx) => (
          <li key={idx}>{i.date} - {i.type} ({i.severity})</li>
        ))}
      </ul>

      <h2>Compliance Score</h2>
      <p>{compliance !== null ? `${compliance}%` : "Loading..."}</p>
    </div>
  );
}