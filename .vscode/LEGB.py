x='global x'
y='global y'
def fun(x):
    x='local x'
    print(x)

def test():
    global y
    y='local y'
    print(y)

fun(x)
print(x)
print()
test()
print(y)
