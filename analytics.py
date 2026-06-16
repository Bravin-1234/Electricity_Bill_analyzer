import pandas as pd

def to_dataframe(records):
    columns= [
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
    
    return pd.DataFrame(records, columns=columns)

def total_consumption_analysis(df):
    total_kwh = df["monthly_kwh"].sum()
    return total_kwh

def total_bill(df):
    total_bill = df["total_bill"].sum()
    return total_bill