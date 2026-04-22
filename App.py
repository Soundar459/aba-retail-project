import streamlit as st
import pandas as pd
import pickle

st.title("🛍️ Retail Customer Analytics Dashboard")

# Load data
df = pd.read_excel("Online Retail.xlsx")
df = df.dropna()
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.sidebar.header("Customer Input")

frequency = st.sidebar.number_input("Purchase Frequency", min_value=1)
avg_value = st.sidebar.number_input("Average Order Value", min_value=1.0)

if st.button("Predict Customer Value"):
    result = model.predict([[frequency, avg_value]])

    if result[0] == 1:
        st.success("💰 High Value Customer")
    else:
        st.warning("⚠️ Low Value Customer")

st.subheader("📊 Revenue by Country")
country_data = df.groupby("Country")["TotalPrice"].sum()
st.bar_chart(country_data)

st.subheader("📦 Top Products")
top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)