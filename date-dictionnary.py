from datetime import date, timedelta

d1 = date(2017, 1, 1)  # start date
d2 = date(2017, 12, 31)  # end date

delta = d2 - d1         # timedelta

for i in range(delta.days + 1):
    print(d1 + timedelta(days=i))