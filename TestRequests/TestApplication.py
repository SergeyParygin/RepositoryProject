import pandas
from datetime import datetime

start_date_str = "01.01.2015"
end_date_str = "12.12.2015"
start_date = datetime.strptime(start_date_str, "%d.%m.%Y").date()
end_date = datetime.strptime(end_date_str, "%d.%m.%Y").date()

data = pandas.read_csv('Crimes.csv')
#print(data.count())
datetime.strptime(data.Date.ix[0],'%d/%m/%Y %H:%M:%S %p')
#data.Date.apply(lambda d: datetime.strptime(data.Date.ix[0], '%m/%d/%y %H:%M'))
#print(data.__doc__)
dates = pandas.to_datetime(data.Date)
data_temp = data[pandas.to_datetime(data.Date).dt.year==2015]
print(data_temp.count())

#print (data[data.Date == 2015])
#print(data.head(5))

print(data_temp['Primary Type'].value_counts())