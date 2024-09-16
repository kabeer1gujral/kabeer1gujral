def isprime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5 +1)):
            if n%i==0:
                return False
        return True
def sumprime(num):
    sum = 0
    for i in range(num):
        if isprime(i):
            sum+=i
    return sum
print(sumprime(20))
