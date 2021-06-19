# This is the function script for the boilerplate time calculator written by Michael Barrett for freecodecamp.org

# Define the function below

def add_time(start, duration, weekday_start = 'blank'):

    # Extract and define the variables
    
    start_hour = int(start.split(':')[0])
    if start_hour == 12:
        start_hour = 0
    start_minute = start.split(':')[1]
    start_minute = int(start_minute.split()[0])
    start_meridiem = start.split()[1]
    if start_meridiem == 'AM':
        start_meridiem = int(0)
    elif start_meridiem == 'PM':
        start_meridiem = int(1)
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])
    start_day = 0

    # Add them all up

    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    new_meridiem = start_meridiem
    new_day = start_day

    # Now we need to reduce

    while new_minute > 59:
        new_hour = new_hour + 1
        new_minute = new_minute - 60
    while new_hour > 11:
        new_meridiem = new_meridiem + 1
        new_hour = new_hour - 12
    if new_hour == 0:
        new_hour = 12
    while new_meridiem > 1:
        new_day = new_day + 1
        new_meridiem = new_meridiem - 2

    # Now let's consider the day of the week

    if weekday_start.lower() == 'sunday':
        new_weekday = 0
    elif weekday_start.lower() == 'monday':
        new_weekday = 1
    elif weekday_start.lower() == 'tuesday':
        new_weekday = 2
    elif weekday_start.lower() == 'wednesday':
        new_weekday = 3
    elif weekday_start.lower() == 'thursday':
        new_weekday = 4
    elif weekday_start.lower() == 'friday':
        new_weekday = 5
    elif weekday_start.lower() == 'saturday':
        new_weekday = 6
    elif weekday_start == 'blank':
        new_weekday = -1

    if new_weekday != -1:
        new_weekday = new_weekday + new_day
        while new_weekday > 6:
            new_weekday = new_weekday - 7

    # Let's take the integers and make them strings

    new_time = str(new_hour) + ':' + '{:02d}'.format(new_minute)
    if new_meridiem == 0:
        new_time += ' AM'
    else:
        new_time += ' PM'
    if new_weekday == 0:
        new_time += ', Sunday'
    elif new_weekday == 1:
        new_time += ', Monday'
    elif new_weekday == 2:
        new_time += ', Tuesday'
    elif new_weekday == 3:
        new_time += ', Wednesday'
    elif new_weekday == 4:
        new_time += ', Thursday'
    elif new_weekday == 5:
        new_time += ', Friday'
    elif new_weekday == 6:
        new_time += ', Saturday'
    if new_day == 1:
        new_time += ' (next day)'
    elif new_day > 1:
        new_time += ' ({} days later)'.format(new_day)

    return new_time
