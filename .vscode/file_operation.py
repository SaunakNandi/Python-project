with open("user.txt",'r') as f:
    size=20
    #content= f.read()
    #content1=f.readline()
    #print(content)
    #content2=f.readlines()
    ##print(content2)
    #for line in f:
    #    print(line,end="")

    #TO print certain amount of words
    #content= f.read(90)
    #print(content)



    f_cont=f.read(size)
    print(len(f_cont))
    while len(f_cont)>0:
        print(f_cont,end='(- -)')
        f_cont=f.read(size)

    #To seek the cusor at desired position
    print()
    f.seek(0)
    print(f.read(10))



#Writing and creating a file use w to write and create a file
#with open("user0.txt",'w') as f1:
#    f1.write("bokachoda")

#makig a exact copy of user.txt
with open('user.txt','r') as rf:
    with open("user0.txt",'w') as wf:
        for i in rf:
            wf.write(i)

with open("imag.jpg",'r') as rf:
    with open('new_image.jpg','wb') as wf:
        for i in rf:
            wf.write(i)
