import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_excel("Online Retail.xlsx")
df = df.dropna()
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

customer_df = df.groupby("CustomerID").agg({
    "TotalPrice": "sum",
    "InvoiceNo": "count"
}).rename(columns={"TotalPrice": "Total_Spent", "InvoiceNo": "Frequency"})

customer_df["Avg_Order_Value"] = customer_df["Total_Spent"] / customer_df["Frequency"]
customer_df["High_Value"] = (customer_df["Total_Spent"] > 1000).astype(int)

X = customer_df[["Frequency", "Avg_Order_Value"]]
y = customer_df["High_Value"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model created successfully!")