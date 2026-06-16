def calculate_monthly_kwh(power, hours, quantity):
    # mothly kwh
    return(power * hours * quantity) / 1000

def calculate_monthy_bill(kwh, rate):
    # monthly bill
    return kwh * rate