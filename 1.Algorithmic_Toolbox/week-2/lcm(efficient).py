no = input().split(" ")
a = int(no[0])
b = int(no[1])
assert (a >= 0 and b >= 0), "a,b should be >= 0"
best = a * b


def gcd(a, b):
    if(a > b):
        while(b != 0):
            a, b = b, a % b
        return a


h = gcd(a, b)

print (a * b / h)
