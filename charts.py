import plotly.express as px 

def create_pie_chart(df):
    fig = px.pie(df, values="kwh", names="appliance", title="Energy Consumption by Appliance")
    return fig

def create_monthly_chart(df):
    fig = px.bar(df, x="month", y="bill", title="Monthly Electricity Bill")
    return fig