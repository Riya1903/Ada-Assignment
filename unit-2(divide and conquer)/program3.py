#Recursive algorithm for computing the greatest common divisor (GCD):

def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

a = 25
b = 45
print(gcd(a, b))
