import streamlit as st
import pandas as pd

st.set_page_config(page_title="Supermarket Sales Dashboard")

st.title("Supermarket Sales Analysis Dashboard")

df = pd.read_csv("supermarket_sales.csv")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Total Revenue
st.metric(
    "Total Revenue",
    f"${df['Total'].sum():,.2f}"
)

# Branch Revenue
st.subheader("Branch Revenue")
st.bar_chart(
    df.groupby('Branch')['Total'].sum()
)

# Product Revenue
st.subheader("Product Line Revenue")
st.bar_chart(
    df.groupby('Product line')['Total'].sum()
)

# Payment Method
st.subheader("Payment Method Usage")
st.bar_chart(
    df['Payment'].value_counts()
)
