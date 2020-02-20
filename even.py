d=(0.12,2.3,4.3,5.4,6.5,0.15)
print(sorted(d))
print(sorted(d,reverse=True))
print(max(d))
print(min(d))


set1={"pen","pencil","rubber"}
set2={"apple","tamato","pineapple"}
#set1.add("blackpen")
x=set1.copy()
print(x)
#print(set1)
#print(id(set1))
set1.discard("tam")
print(set1)
z=set1.union(set2)
print(z)





thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print([thisdict])
