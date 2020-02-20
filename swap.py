list1=[1,2,3,4,5,6]
f=list1[0]
list1[0]=list1[5]
list1[5]=f
print(list1)