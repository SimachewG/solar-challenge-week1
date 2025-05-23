# utils.py
import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

DATA_DIR = "data"

@st.cache_data
def load_data(country):
    filename = f"{country.lower()}_clean.csv"
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        st.error(f"Data file for {country} not found at {path}.")
        return pd.DataFrame()
    
    df = pd.read_csv(path)
    df["Country"] = country.capitalize()
    return df

def process_data(df, ghi_range):
    if df.empty:
        return df
    return df[(df["GHI"] >= ghi_range[0]) & (df["GHI"] <= ghi_range[1])]

def create_visualizations(df):
    if df.empty:
        st.warning("No data to display. Please adjust your filters or select a valid country.")
        return

    st.subheader("GHI Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(df["GHI"], bins=15, kde=True, ax=ax1, color="orange")
    ax1.set_xlabel("GHI (kWh/m²/day)")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

    if "DNI" in df.columns:
        st.subheader("DNI Boxplot by Country")
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df, x="Country", y="DNI", ax=ax2)
        ax2.set_ylabel("DNI (kWh/m²/day)")
        st.pyplot(fig2)
    
    st.subheader("Sample Data Preview")
    st.dataframe(df.head())
