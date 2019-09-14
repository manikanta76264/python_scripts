import os
import datetime
f=datetime.date(2019,8,9)
print(f)
for k in os.listdir("F:\\python\\py_sripts\\scripts"):
    j=os.path.getmtime("F:\\python\\py_sripts\\scripts\\{}".format(k))
    if f<datetime.date.fromtimestamp(j):
        print(datetime.date.fromtimestamp(j),k)
