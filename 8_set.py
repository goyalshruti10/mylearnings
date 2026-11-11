#set are non duplicate, non ordered so i cant retrive with index

s = {3,23,"j",11}

print(s, type(s))

print(s)

s.add(888)

print(s)

s1 = {9,0,9,1}

c = s.union(s1)
print(c)

c = s.intersection(s1)
print(c)