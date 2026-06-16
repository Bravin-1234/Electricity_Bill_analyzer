import streamlit as st
import pandas as pd
import plotly.express as px

from database import init_db, fetch_all
# initialize the database
init_db()

# Page Settings
st.set_page_config(page_title="Electricity Bill Analyzer", layout="wide")
st.title("Electricity Bill Analyzer")

# Get data from the database
records = fetch_all()
if records:
    # Convert records to DataFrame
    columns = [
        "id",
        "month",
        "appliance",
        "power",
        "hours",
        "quantity",
        "daily_kwh",
        "monthly_kwh",
        "tariff",
        "total_bill",
        "timestamp"
    ]
    df = pd.DataFrame(records, columns=columns)

    # Display the data in a table
    st.subheader("Energy Consumption Data")
    st.dataframe(df)

    # -------------------------------------
    # Monthly Analysis
    # -------------------------------------
    st.subheader("Monthly Analysis")
    
    months = df["month"].unique()
    selected_month = st.selectbox("Select Month", months)
    
    month_data = df[df["month"] == selected_month]
    total_energy = month_data["monthly_kwh"].sum()
    total_bill = month_data["total_bill"].sum()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Energy Consumption (kWh)", f"{total_energy:.2f}")
        
        with col2:
            st.metric("Total Bill (KES)", f"{total_bill:.2f}")
            
# ---------------------------------
# Appliance Consumption
# ---------------------------------

st.subheader("Appliance Consumption Analysis")
appliance_consumption= (
    month_data
    .groupby("appliance")["monthly_kwh"]
    .sum()
    .reset_index()
)   

fig = px.pie(appliance_consumption, values="monthly_kwh", names="appliance", title="Energy Consumption by Appliance")
st.plotly_chart(fig)

# ---------------------------------
# Give Recommendations
# ---------------------------------
st.subheader("Energy Saving Recommendations")
highest = appliance_consumption.sort_values(by="monthly_kwh", ascending=False)

for index, row in highest.iterrows():
    appliance = row["appliance"]
    consumption = row["monthly_kwh"]
    
    if consumption > 100:
        st.warning(f"{appliance} is consuming {consumption:.2f} kWh. Consider reducing usage hours or use an energy-efficient model.")
    elif consumption > 50:
        st.info(f"{appliance} has a moderate consumption of {consumption:.2f} kWh. Monitor  its daily usage.")
    else:
        st.success(f"{appliance} has a low consumption of {consumption:.2f} kwh")
        
    
    # --------------------------------
    # Highest Consumption Appliance
    # --------------------------------  
    
    top = highest.iloc[0]
    st.subheader("Highest Consumption Appliance")
    st.write(f"The appliance with the highest consumption is {top['appliance']} with {top['monthly_kwh']:.2f} kWh.")
else:
    st.error("No data available. Please add records to the database.")