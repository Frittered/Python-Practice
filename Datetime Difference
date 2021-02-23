from datetime import datetime
current = datetime.now()
past = '2020-12-31 23:52'
current_stripped = datetime.strptime(current.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
past_stripped = datetime.strptime(past, "%Y-%m-%d %H:%M")
difference = current_stripped-past_stripped
print(difference.days)
