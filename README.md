# solar-micro-grid-optimization
autonomous solar battery micro grid optimizer for hackathon
# ☀️ Autonomous Solar-Battery Micro-Grid Optimizer

## Overview
A digital twin and AI-driven energy management system built for the sustainability hackathon. This application autonomously monitors solar generation, battery status, and building load to optimize power switching, eliminate peak-tariff penalties, and maximize renewable usage in real-time.

## Tech Stack
* **Language:** Python
* **Framework:** Streamlit (for interactive dashboard UI)
* **Data Processing:** Pandas, NumPy

## Key Features
* **Interactive Digital Twin:** Adjust live sliders for solar output, building load, battery state-of-charge, and tariff status.
* **Autonomous Optimization Engine:** Automatically triggers peak-shaving and battery storage depending on economic and environmental thresholds.
* **Live Impact Metrics:** Instantly calculates estimated financial savings ($\text{₹}$ saved) and carbon emissions avoided ($\text{CO}_2$).

## How to Run Locally
1. Clone or download the repository.
2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy
