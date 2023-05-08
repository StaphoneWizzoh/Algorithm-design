from math import log10
import math

def bitString(n,s):
    if n==1 :return s
    return [digit + bits for digit in bitString(1, s) for bits in bitString(n-1, s)]



def karatsuba(x,y):
     # Base case
     if x<10 or y<10:
         return x*y
     
     # Sets n, the number of digits in the highest input number
     n=max(int(log10(x)+1), int(log10(y)+1))
     
     # rounds up n/2
     n_2 = int(math.ceil(n/2.0))
     
     # adds 1 if n is uneven
     n = n if n%2==0 else n+1
     
     # splits the input numbers
     a,b = divmod(x, 10**n_2)
     c,d = divmod(y, 10**n_2)
     
     # applies the three recursive steps
     ac = karatsuba(a, c)
     bd = karatsuba(b, d)
     ad_bc = karatsuba((a+b), (c+d)) - ac - bd
     
     #performs the multiplication
     return(((10**n)*ac)+bd+((10**n_2)*(ad_bc)))
 
    
print(karatsuba(123456789, 987654321))