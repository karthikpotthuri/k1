import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
def add(a,b):
    sum=a+b
    print("the sum",sum)

def sub(a,b):
    sub=a-b
    print("the sum",sub)

def mul(a,b):
    mul=a*b
    print("the sum",mul)

def div(a,b):
    if b==0:
        print("division not possible")
    else:
        div=a/b
        print("the sum",div)

add(a,b)
sub(a,b)
mul(a,b)
div(a,b)