# 📅 Age Calculator
# Input: user's date of birth.
# Output: age in years, months, days.

from datetime import datetime

dob = input("Enter your date of birth (YYYY-MM-DD): ")
dob_date = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.now()
age = today - dob_date

years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30

print(f"You are {years} years, {months} months, and {days} days old.")