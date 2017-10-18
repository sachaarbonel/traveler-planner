from datetime import date, timedelta, datetime

# def convert_date(orig_date):
#     #orig_date = datetime.datetime(x,y,z)
#     orig_date = str(orig_date)
#     d = datetime.strptime(orig_date, '%Y-%m-%d')
#     d = d.strftime('%m-%d-%y')
#     return d

d1 = date(2017, 1, 1)  # start date
d2 = date(2017, 12, 31)  # end date

# d2= convert_date(d2)
# d1 = convert_date(d1)

delta = d2 - d1         # timedelta

listDates=[]
for i in range(delta.days + 1):
    listDates.append(d1 + timedelta(days=i))
print(listDates)
print(listDates[0])
print(len(listDates))





