def myFun(*argv):
    for arg in argv:
       print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

dic={"car":"maruthi","colour":"red","year":2019}
print(dic['car'])
print(dic['colour'])
print(dic['year'])

#dict={1:"a",2:"b"}
#n=str(input("Enter the string value"))
#m=int(input("Enter the value"))
#if n in dict.value():
        #print("true")
#else:
        #print("false")

import method
method.greet("name")


def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" %(key, value))

myfun(first='greek', mid='for', last='geeks')


x= lambda a:a-20
print("sub=", x(30))