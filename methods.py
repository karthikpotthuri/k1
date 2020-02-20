a="10"
for i in a:
   print(i)


a =[10,20,30,40,50,60,70,80]
for i in a[2:5]:
    print(i)





s="helOO ABHAA"
c=s.casefold()
print(len(s))
print(c)


list=[1,2,3]
list.extend('4')
print(list)



apple=['a','p','p','l','e']
index=apple.index('p')
print(index)


apple = ['a', 'p', 'p', 'l', 'e'] # Char list
even = [6,8,2,4] # int list
print(apple)
print(even)
# Calling Method
apple.sort()
even.sort()
# Displaying result
print("\nAfter Sorting:\n",apple)
print(even)


list="hello"
s=list[0:4:2]
print(s)

x={}
for i in range(1,11):
    x[i]=i*i
print(x)








def types(x):
 if x < 0:
       return "Hello!"
 else:
      return 0

print(types(1))
print(types(-1))










