import os
#os.rename('Test5.txt','udmey.txt')
print(os.listdir())

os.chdir('C:/Users/Admin/Desktop/')
#Path tree of every file in desktop
for dirpath,dirname,filename in os.walk('C:/Users/Admin/Desktop/'):
    print("Current path: ",dirpath)
    print("Directory: ",dirname)
    print("File name: ",filename)
    print()

#Base name ,directory name
print("see")
print(os.path.basename('C:/Users/Admin/Desktop/.vscode'))
print(os.path.dirname('C:/Users/Admin/Desktop/.vscode'))
print(os.path.split('C:/Users/Admin/Desktop/.vscode'))

#To check it exist or not
print(os.path.exists('C:/Users/Admin/Desktop/.vscode'))

print(os.path.isfile('C:/Users/Admin/Desktop/.vscode'))
print(os.path.isdir('C:/Users/Admin/Desktop/.vscode'))
