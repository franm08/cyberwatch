const API_BASE = "http://127.0.0.1:5000";

export const getCompliance = () =>
  fetch(`${API_BASE}/compliance`).then((res) => res.json());

export const getIncidents = () =>
  fetch(`${API_BASE}/incidents`).then((res) => res.json());

export const getVendors = () =>
  fetch(`${API_BASE}/vendors`).then((res) => res.json());