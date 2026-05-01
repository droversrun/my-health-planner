
st.set_page_config(page_title="Health Predictor", layout="centered")

st.title("🍎 My Health Planner")
st.write("Plan your day to see tomorrow's predicted results.")

# 1. Inputs
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Current Weight (kg)", value=75.0)
        bmr = st.number_input("Your BMR (Daily Burn)", value=1700)
    with col2:
        glucose = st.number_input("Fasting Glucose", value=5.2)
        target = st.number_input("Target Glucose", value=5.0)

st.divider()

# 2. Planning
st.header("📅 Today's Plan")
plan_cal = st.number_input("Planned Calories to Eat", value=1800)
plan_carbs = st.number_input("Planned Carbs (g)", value=150)
plan_ex = st.number_input("Planned Exercise Burn (kcal)", value=300)

# 3. Logic
# 7700 calories = 1kg
net_cal = plan_cal - (bmr + plan_ex)
weight_change = net_cal / 7700
predicted_weight = weight + weight_change

# Simple glucose logic
glucose_impact = (plan_carbs * 0.01) - (plan_ex * 0.002)
predicted_glucose = glucose + glucose_impact

# 4. Predictions
st.divider()
st.header("🔮 Tomorrow's Prediction")
c1, c2 = st.columns(2)
c1.metric("Predicted Weight", f"{predicted_weight:.2f} kg", f"{weight_change:.3f} kg")
c2.metric("Predicted Glucose", f"{predicted_glucose:.2f}", f"{glucose_impact:.2f} impact")

if net_cal < 0:
    st.success(f"Great plan! You are in a {abs(net_cal)} calorie deficit.")
else:
    st.warning(f"Note: You are in a {net_cal} calorie surplus.")
