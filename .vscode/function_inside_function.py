def out():
    x='outer x'
    def inn():
        nonlocal x
        x='inner x'
        print(x)
    inn()
    print(x)

out()
