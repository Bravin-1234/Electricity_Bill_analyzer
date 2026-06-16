def give_recommendations(df):
    tips = []
    
    total_kwh = df["kwh"].sum()
    
    for _, row in df.groupby("appliance").sum().iterrows():
        percent = (row["kwh"] / total_kwh) * 100
        if percent > 40:
            tips.append(f"!!{row.name} is consuming{percent:.1f}% of energy.Consider efficiency upgrade. ")
            
            if total_kwh > 200:
                tips.append("High overall consumption. Reduce heavy appliance usage or switch to energy-efficient models.")
                
                if not tips:
                    tips.append("your energy usage is balanced.")