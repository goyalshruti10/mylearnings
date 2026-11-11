str = " i love python "
print(str.strip())
print(len(str))
print(str.title())
print(str.count("o"))

str2= "123abc"

print(str2.isalpha())

print(str2.isalnum())

if str2.isalnum()==True:
    print("ok")
else:
    print("nooo")    


for i in range(1,10):
   print(f"{i}")


for i in range(1,10):
   print(i)


new = str.replace("love", "uff")

ind = new.index("uff")

print("index of uff is: ", ind)

print(new.upper())

vovwel_set = ['a', 'e', 'i', 'o', 'u']
sum =0
for char in str.lower():
    if (char in vovwel_set):
        sum +=1

print (sum)


inp_str = input("Input your string")
len_str = len(inp_str)

    



