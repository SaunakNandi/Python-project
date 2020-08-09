import datetime
import pytz



#strftime
dt_mn=datetime.datetime.now(tz=pytz.timezone("Indian/Comoro"))
print(dt_mn)
print(dt_mn.strftime("%B %d, %Y"))
