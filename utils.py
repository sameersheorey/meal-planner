from datetime import datetime, timedelta

def get_dates_in_between(start_date_str, end_date_str):
    # Parse the start and end dates into datetime objects
    start_date = datetime.strptime(start_date_str, '%A, %d %B')
    end_date = datetime.strptime(end_date_str, '%A, %d %B')

    # Initialize a list to store the dates
    dates_list = []

    # Iterate over the dates from start to end, inclusive
    current_date = start_date
    while current_date <= end_date:
        dates_list.append(current_date.strftime('%A, %d %B'))
        current_date += timedelta(days=1)

    return dates_list

# Example usage:
start_date_str = 'Monday, 16 April'
end_date_str = 'Wednesday, 25 April'
dates_in_between = get_dates_in_between(start_date_str, end_date_str)
print(dates_in_between)