dic={'name': 'Saunak','age':19}
print('My name is {0} and I am {1} years old'.format(dic['name'],dic['age']))
x='My name is {0[name]} and I am {0[age]} years old'.format(dic)
print(x)
#FRom listo
z=['bablu',23]
sen='My name is {0[0]} and I am {0[1]} years old'.format(z)
print(sen)

#Using class
class person():
    def __init__(self,name,age):
        self.name=name
        self.age= age
pl= person("Markus",35)
new='My name is {0.name} and I am {0.age} years old'.format(pl)
print(new)

#Using keyword value
form='My name is {name} and I am {age} years old'.format(**dic)
print(form)

for i in range(1,11):
    a='value is {:02}.'.format(i)
    print(a)

pi=3.14267
print("Value is {:.2f}".format(pi))


print("1 MB is ={:,.2f}".format(1024))
print()
#datetime and string format
import datetime
date= datetime.datetime(2020,3,20,12,30,5)
dt="{:%B %d %Y}".format(date)
print(dt)

sen="{0:%B %d %Y} fell on {0:%A} and was the {0:%j} day of the year".format(date)
print(sen)
