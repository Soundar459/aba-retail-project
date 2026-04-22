import streamlit as st
import pandas as pd

st.title("🛍️ Retail Customer Analytics Dashboard")

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

# Sidebar input (just UI demo)
st.sidebar.header("Customer Input")

frequency = st.sidebar.number_input("Purchase Frequency", min_value=1)
avg_value = st.sidebar.number_input("Average Order Value", min_value=1.0)

# Dummy prediction (no model)
if st.button("Predict Customer Value"):
    if frequency > 5 and avg_value > 50:
        st.success("💰 High Value Customer")
    else:
        st.warning("⚠️ Low Value Customer")

# Charts
st.subheader("📊 Population by State")
st.bar_chart(df.set_index("State")["Population"])

st.subheader("📍 Area Rank by State")
st.bar_chart(df.set_index("State")["Rank"])
