cr=['history','math','english','science','geography']
print(cr[2:7])
cr.append('computer')
cr.insert(1, 'politcal science')
#print(cr)

cr1=['hindi','drawing']
cr.extend(cr1)
print(cr)
print()
print(sorted(cr))
i=1
for i,item in enumerate(cr,start=1):
    print(i,item)

print()
x=' , '.join(cr)
print(x)


cr1=cr
print(cr1)

cr.insert(0,'art')
print()
print(cr)
print(cr1)

# SETS
course1={'history','math','english','science','geography'}
course2={'politcal science','computer','english'}
#course1=course2
print(course1.intersection_update(course2))