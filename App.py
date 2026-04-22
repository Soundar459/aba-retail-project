import streamlit as st
import pandas as pd
import pickle

st.title("🛍️ Retail Customer Analytics Dashboard")

# ✅ Load SMALL online dataset (for deployment)
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

# ✅ Load model
model = pickle.load(open("model.pkl", "rb"))

# Sidebar input
st.sidebar.header("Customer Input")

frequency = st.sidebar.number_input("Purchase Frequency", min_value=1)
avg_value = st.sidebar.number_input("Average Order Value", min_value=1.0)

# Prediction
if st.button("Predict Customer Value"):
    result = model.predict([[frequency, avg_value]])

    if result[0] == 1:
        st.success("💰 High Value Customer")
    else:
        st.warning("⚠️ Low Value Customer")

# ✅ Correct visualization (based on this dataset)
st.subheader("📊 Population by State")
st.bar_chart(df.set_index("State")["Population"])

# Optional extra chart
st.subheader("📍 Area by State")
st.bar_chart(df.set_index("State")["Rank"])
