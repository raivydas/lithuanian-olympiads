def leap_year(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False

def find_first_day(year):
    curr_day = 6
    curr_year = 1978
    if year == curr_year:
        return curr_day
    elif year < curr_year:
        while year != curr_year:
            curr_year -= 1
            if leap_year(curr_year):
                curr_day = (curr_day - 366) % 7
            else:
                curr_day = (curr_day - 365) % 7
        return curr_day
    else:
        while year != curr_year:
            if leap_year(curr_year):
                curr_day = (curr_day + 366) % 7
            else:
                curr_day = (curr_day + 365) % 7
            curr_year += 1
        return curr_day

def count_weekends(year):
    weekend_days = 0
    day_of_year = find_first_day(year)
    if leap_year(year):
        days_in_year = 366
    else:
        days_in_year = 365
    for curr_day in range(days_in_year):
        curr_weekday = (day_of_year + curr_day) % 7
        if curr_weekday == 5 or curr_weekday == 6:
            weekend_days += 1
    return weekend_days

