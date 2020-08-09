month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap(year):
    return year % 4==0

def days_month(m):
    if 12<m<1:
        print('invalid')
    elif 1<=m<=12:
        print('Days of this month ',month[m])

print(leap(2020))
days_month(4)