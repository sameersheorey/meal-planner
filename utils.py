from datetime import datetime, timedelta

def get_dates_in_between(start_date_str, end_date_str):
    # Parse the start and end dates into datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    # Initialize a list to store the dates
    dates_list = []

    # Iterate over the dates from start to end, inclusive
    current_date = start_date
    while current_date <= end_date:
        dates_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return dates_list

def change_date_format(date_str):
    # Parse the date string into a datetime object
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Format the date as 'Day, DD Month'
    formatted_date = date.strftime("%A, %d %B")

    return formatted_date




