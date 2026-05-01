import streamlit as st

st.title("🍎 My Health Planner")

# Input Section
w = st.number_input("Current Weight (kg)", value=75.0)
b = st.number_input("BMR (Burn at rest)", value=1700.0)
g = st.number_input("Fasting Glucose", value=5.2)

st.divider()

# Planning Section
p_cal = st.number_input("Planned Calories", value=1800.0)
p_carbs = st.number_input("Planned Carbs (g)", value=150.0)
p_ex = st.number_input("Planned Exercise Burn", value=300.0)

# Calculations
net = p_cal - (b + p_ex)
# 7700 cal = 1kg
w_change = net / 7700
p_weight = w + w_change

# Glucose prediction
g_impact = (p_carbs * 0.01) - (p_ex * 0.002)
p_glucose = g + g_impact

st.divider()

# Results
st.header("🔮 Tomorrow's Prediction")
col1, col2 = st.columns(2)
col1.metric("Weight", f"{p_weight:.2f} kg", f"{w_change:.3f}")
col2.metric("Glucose", f"{p_glucose:.2f}", f"{g_impact:.2f}")

if net < 0:
    st.success(f"Deficit: {abs(net)} kcal")
else:
    st.warning(f"Surplus: {net} kcal")