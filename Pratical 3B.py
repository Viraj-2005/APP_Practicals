import datetime
x = datetime.datetime.now()
y = x + datetime.timedelta(0, 10)
print(x.time())
print(y.time())
