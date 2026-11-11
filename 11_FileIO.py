f = open("file_example.txt","r")

content = f.read()

print(content)

f.close()


f = open("John.txt", "w") ## overwrites every time
string = '''
jon is nice
'''
f.write(string)

f.close()

f = open("John.txt", "a") ## overwrites every time
string = '''
jon is nice.
john is doe
'''
f.write(string)

f.close()

with open("John.txt","r") as f:   #####with - context manager
    content = f.read()
    print(content)


with open("notes.txt","w") as f:
    f.write("Learning is fun")

with open("notes.txt","r") as f:
    print(f.read())

    
with open("tasks.txt","w") as f:
    f.write("""
    Learning is fun
    i want to be big
    lead, manager , mango
    """)

with open("tasks.txt","a+") as f:
    f.write("""
        Learning is fun
        i want to be big
        lead, manager , mango
        i will
        """)
    f.seek(0)
    print(f.read())