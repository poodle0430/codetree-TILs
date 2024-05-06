a,b = input().split(' ')

a = int(a)
b = int(b)

def GCD(a,b):
    if b == 0: return a
    else: return GCD(b,a%b)

gcd = GCD(a,b)
lcm = a*b/gcd

print(gcd,int(lcm))