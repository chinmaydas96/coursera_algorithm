# Uses python3


no = input().split()
a = int(no[0])
b = int(no[1])


def gcd(a, b):
    if (a >= b):
        while (b != 0):
            a, b = b, a % b
        return a

    else:
        return gcd(b, a)


print (gcd(a, b))
