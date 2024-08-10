import datetime, bday_messages

date1 = datetime.date.today()
date2 = datetime.date(2024, 8, 10)

days_away = date2 - date1

if(date1 == date2):
  print(bday_messages.random_messages)
else:
  print(f"My next birthday is {days_away.days} days away!")
