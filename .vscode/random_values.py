import random

val=random.random()
print(val)

val1=random.randint(1,5)
print(val1)

greeting=['hello','hi','whatsup','hey']
value= random.choice(greeting)
print(value+' Nanndy')

#Printing a number of choices randomly
color=['red','blue','yellow']
value=random.choices(color,k=20)
print(value)

#Using 'weight' to show how the likeliness of a color to occur red=18 blu=18 and yellow =2   total =38
#therefore red has 18/38 chanceto occur  ,yellow has 2/38  chance to occur

value=random.choices(color,weights=[18,18,2],k=20)
print(value)
print()
#Using cards
deck=list(range(1,53))
print(deck)
random.shuffle(deck)
print(deck)

smp=random.sample(deck,k=8)
print(smp)
