import datetime
d= datetime.date(2019,12,31)
print(d)

td=datetime.date.today()
print(td)
print()

#Using time delta to go back and future date
delta=datetime.timedelta(days=7)
sum=td+delta
print(sum)
print(td-delta)

#time remai  for my birthday
bd=datetime.date(2020,10,2)
x=bd-td
print(x)
print("Calculating in sec. ",x.total_seconds())

#Using datetime
dt=datetime.datetime(2020,6,26,1,20,45)
print(dt)
print(dt.date())
print(dt.time())


tdel=datetime.timedelta(hours=48)
print("48 hours from now",dt+tdel)
