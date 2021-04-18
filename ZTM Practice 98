import datetime
week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
inp = '08 15 1965'
def historical_weekday(date):
    date_objects = date.split(' ')
    datetime_date = datetime.date(int(date_objects[2]),int(date_objects[0]),
                                  int(date_objects[1]))
    day_index = datetime_date.weekday()
    return print(f'The day was a {week_days[day_index]}')
historical_weekday(inp)
