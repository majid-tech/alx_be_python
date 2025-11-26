from datetime import datetime, date, time, timedelta

# Current date and time: 2024-03-25 15:30:45
# Enter the number of days to add to the current date: 10
# Future date: 2024-04-04

def display_current_datetime():
    current_date = datetime.now()
    return current_date

print('Current date and time:', display_current_datetime())

def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + timedelta(days=num_of_days)
    return future_date.strftime("%Y-%m-%d")

print('Future date:',calculate_future_date())

