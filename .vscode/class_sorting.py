class employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary= salary
    def __repr__(self):
        return f"{self.name}, {self.age}, ${self.salary}"

e1= employee("Mark",28,3000)
e2= employee("Martha",23,2800)
e3= employee("Denver",27,4500)

emp=[e1, e2, e3]
x=sorted(emp,key=lambda e: e.salary)
print(emp)
print(x)
