import datetime
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)

dy=date.today()-timedelta(1)
df = date.today() + timedelta(1)
print('yestreday : ' , dy )
print('today: ' , date.today())
print('tomorrow : ', df)

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print()
print(dt)
print() 
 
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2021-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()
