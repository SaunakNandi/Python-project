num=[1,2,3,4,5,6,7,8,9]
x=[0]
for i in num:
    x.append(i)
print(x)
print()
#LIST COMPREHENSION
print("List comprehension")
list=[n for n in num]
print(list)
list1=[]
list=[n**2 for n in num] #Power
print(list)

print("Put even numbers")
for i in num:
    if i%2==0:
        list1.append(i)
print(list1)
var=[]
#Appending  letters and numbers
for i in 'abcd':
    for j in num:
        var.append((i,j))
print(var)
# Alternative way for this
var=[(i,j) for i in 'abcd' for j in num]
print(var)

#Zip function
name=['bruce','tony','steve','peter','wade']
hero=['hulk','iron man','captain america','spiderman','deadpool']
dict={}
for nm,h in zip(name,hero):
    dict[nm]=h
print(dict)

#Alternative way
dict={nm:h for nm,h in zip(name,hero)}
print(dict)


dict={nm:h for nm,h in zip(name,hero) if nm!='peter'}
print(dict)

#Set COMPREHENSION
n=[1,1,2,2,2,3,3,3,3,4,4,4,5,5,6,6,6,7,8,8,9,9,9,9,9]
my_set=set()
for i in n:
    my_set.add(i)
print(my_set)

#Alternative waay
my_set={i for i in n}
print(my_set)

#Generator COMPREHENSION
gen=(m*m for m in num)
#print(gen)
for i in gen:
    print(i)
