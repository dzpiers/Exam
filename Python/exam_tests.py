import math

def p(n):
    if n<2:
        return False
    f=2
    while f<= math.sqrt(n):
        if n%f==0:
            return False
        f +=1
    return True

def tp(x,y):
    return x!= y and p(x) and p(y) and abs(x-y) <=2

result = []
for z in range(10000):
    result.append(tp(601,z))

print(sum(result))
