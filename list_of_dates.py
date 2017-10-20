from datetime import date, timedelta, datetime

def printListOfDates():
	d1 = date(2017, 1, 1)  # start date
	d2 = date(2017, 12, 31)  # end date
	delta = d2 - d1         # timedelta
	listDates=[]
	for i in range(delta.days + 1):
		listDates.append(d1 + timedelta(days=i))
	return listDates

# dList = printListOfDates()
# print(dList[364])




