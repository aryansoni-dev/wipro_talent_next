hourly_cost = 0.51

daily_cost = hourly_cost * 24
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30
num_of_days_918 = 918 / daily_cost

print(f"\nDaily cost: ${daily_cost:.2f}")
print(f"Weekly cost: ${weekly_cost:.2f}")
print(f"Monthly cost: ${monthly_cost:.2f}")
print(f"Number of days with $918 : {num_of_days_918:.0f} days.")