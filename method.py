#sum of array
def _sum(arr, n):
    return (sum(arr))


arr = []
arr = [12, 3, 4, 15]
n = len(arr)
ans = _sum(arr, n)
print(ans)

2.#factorial of number


def factorial(n):

    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5;
print("Factorial of", num, "is",
      factorial(num))

3.#string which accepts only vowels
def check(string):
    vowels = set("aeiou")
    s = set({})
    for char in string :
        if char in vowels:
            s.add(char)
        else:
            pass
    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")
if __name__ == "__main__":
        string = "SEEquoiaL"
        string = string.lower()
        check(string)

4.# using lamda function to sort dict

lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]


print("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age']))

print("\r")
print("The list printed sorting by age and name: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])))

print("\r")

print("The list printed sorting by age in descending order: ")
print (sorted(lis, key = lambda i: i['age'], reverse=True))





5.#create  list tuples

list1=[1,2,3,4]
res = [(val, pow(val, 3)) for val in list1]
print(res)

