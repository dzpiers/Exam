## Copy code here
print(2**10000)

print("Python"[-3])

def foo(x, y):
    z = bar(y)
    x = 2 * z
    return x
def bar(w):
    return w ** 2
goo = foo(11, 88)
print(goo)

# Python code to demonstrate naive method
# to compute factorial
n = 10
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of 10 is : ", fact)

def f(a,b):
    for x in b:
        a.append(x)
    print(a)

print(f([1,2,3], [3,4,5]))