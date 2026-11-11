#list is mutable, mixed, ordred means can be found by index, usecase - sequence, dynamic data

marks = [30,10,2,88]
list1 = ["kk", 10,True,"jj"]

print(marks)

print(marks[2])
print(list1)
print(list1[2:4])


list1 = [1,4,5,6]
print(list1)
list1.append( "ufhhf")
print(list1)
list1.insert(2,9999)
print(list1)
list1[3]=400
print(list1)

lf =["aaple", "baana", "cherry"]
print(lf[0])
lf[1] ="orange"
print(lf)
