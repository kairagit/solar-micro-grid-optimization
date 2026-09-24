import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Solar & Battery Micro-Grid Optimizer",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Autonomous Solar-Battery Micro-Grid Optimizer")
st.markdown("### Digital Twin & AI-Driven Energy Management System")
st.write("This system continuously monitors solar generation, battery status, and building load to automatically optimize power switching, eliminate peak-tariff penalties, and maximize renewable usage.")

st.divider()

# Sidebar controls for real-time simulation testing
st.sidebar.header("🎛️ Simulation Controls")
st.sidebar.markdown("Use these sliders to test how the optimization engine responds to changing environmental conditions:")

current_solar = st.sidebar.slider("Solar Generation (kW)", 0.0, 10.0, 4.5)
current_load = st.sidebar.slider("Building Power Demand (kW)", 1.0, 10.0, 5.0)
battery_soc = st.sidebar.slider("Battery State of Charge (%)", 0, 100, 65)
is_peak_hours = st.sidebar.checkbox("Peak Electricity Tariff Active (High Cost)", value=True)

# --- OPTIMIZATION ENGINE LOGIC ---
net_power = current_solar - current_load
grid_power = 0.0
battery_action = "Idle"
battery_power_flow = 0.0

if net_power > 0:
    # Excess solar energy available
    if battery_soc < 100:
        battery_action = "Charging Battery (Storing Excess Solar)"
        battery_power_flow = net_power
    else:
        battery_action = "Battery Full - Exporting Excess to Grid"
        grid_power = -net_power  # Negative means feeding back into the grid
else:
    # Power deficit (Load > Solar)
    deficit = abs(net_power)
    if is_peak_hours and battery_soc > 20:
        battery_action = "Discharging Battery (Peak Shaving Active)"
        battery_power_flow = -min(deficit, 3.0)  # Max discharge constraint
        grid_power = deficit - abs(battery_power_flow)
    else:
        battery_action = "Drawing Power from Grid"
        grid_power = deficit

# --- IMPACT METRICS CALCULATION ---
rupees_saved = abs(current_solar * 11.5) if net_power > 0 else (3.0 * 14.0 if is_peak_hours else 0.0)
co2_avoided = current_solar * 0.85  # kg of CO2 per kWh of solar used

# --- DASHBOARD LAYOUT ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="⚡ Automated System Action", value=battery_action)
with col2:
    st.metric(label="🔌 Grid Power Draw", value=f"{max(0, grid_power):.2f} kW")
with col3:
    st.metric(label="💰 Estimated ₹ Saved", value=f"₹{rupees_saved:.2f}", delta="Peak Avoided")
with col4:
    st.metric(label="🌱 CO₂ Emissions Avoided", value=f"{co2_avoided:.2f} kg")

st.divider()

# Visualizing Power Flow
st.subheader("📊 Real-Time Power Flow Distribution")

chart_data = pd.DataFrame({
    "Component": ["Solar Gen", "Building Load", "Grid Draw", "Battery Flow"],
    "Power (kW)": [current_solar, current_load, max(0, grid_power), battery_power_flow]
})

st.bar_chart(chart_data, x="Component", y="Power (kW)", color="Component")

# System Log / Transparency Box
st.subheader("🛠️ Autonomous Decision Log")
if is_peak_hours and net_power < 0 and battery_soc > 20:
    st.success("✔ **Optimization Triggered:** Peak tariff hours detected. Automatically cut off expensive grid reliance and routed stored battery power to satisfy building load.")
elif net_power > 0:
    st.success("✔ **Optimization Triggered:** High solar generation detected. Automatically diverted excess power into battery storage instead of wasting it.")
else:
    st.warning("⚠️ **System Notice:** Battery reserves low or standard tariffs active. Operating on balanced grid integration.")

