# Problem 79: Calculate compound interest
# Find and fix the error

def compound_interest(principal, rate, time, n, rate_in_percent=True):
    """
    Calculate compound interest.
    
    principal: initial amount
    rate: annual interest rate (percent or decimal)
    time: time in years
    n: number of times interest is compounded per year
    rate_in_percent: True if rate is given in percent, False if in decimal
    """
    if rate_in_percent:
        rate = rate / 100  # convert percent to decimal
    
    amount = principal * (1 + rate / n) ** (n * time)
    interest = amount - principal
    return round(interest, 2)  # rounded to 2 decimals

# Example usage
p = 1000
r = 5  # 5%
t = 2
n = 4

print(f"Compound Interest: {compound_interest(p, r, t, n)}")  # 104.49