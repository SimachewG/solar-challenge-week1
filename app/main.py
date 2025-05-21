# main.py
import streamlit as st
from utils import load_data, process_data, create_visualizations

def main():
    st.set_page_config(page_title="Solar Data Discovery", layout="wide")
    st.title("Cross-Country Solar Radiation Dashboard")
    st.markdown(
        "Use the sidebar to select a country and filter by Global Horizontal Irradiance (GHI)."
    )

    # Sidebar filters
    st.sidebar.header("Filters")
    country_options = ["Benin", "Togo", "Sierraleone"]
    selected_country = st.sidebar.selectbox("Select Country", country_options)
    ghi_range = st.sidebar.slider("GHI Range (kWh/m²/day)", 0.0, 10.0, (3.0, 7.0))

    # Load, filter, visualize
    raw_data = load_data(selected_country)
    filtered_data = process_data(raw_data, ghi_range)
    create_visualizations(filtered_data)

if __name__ == "__main__":
    main()
