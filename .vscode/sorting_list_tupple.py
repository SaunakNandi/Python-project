l=[1,4,2,5,6,3,9,7,8]
print(sorted(l,reverse=True))
l.sort()
print(l)

#tupple
tup=(4,5,2,7,1,9,3,8,7,6)
print(sorted(tup))

#Arranging elements on the basis of the value
n=(-6,-3,-5,1,5,3,2)
print(sorted(n))
x=sorted(n,key=abs)
print()
print("Arranging elements on the basis of the value")
print(x)
