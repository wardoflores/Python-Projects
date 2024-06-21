from datetime import datetime, timedelta

end_date = datetime.now()
start_date = datetime(2023, 8, 31)

current_date = start_date
while current_date <= end_date:
    print(current_date.strftime('%Y-%m-%d'))
    print()  # Add a blank line
    current_date += timedelta(days=1)