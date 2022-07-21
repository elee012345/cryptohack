import base64
from Crypto.Util.number import *
from pwn import *

# The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b).
# 
# For a = 12, b = 8 we can calculate the divisors of a: {1,2,3,4,6,12} and the divisors of b: {1,2,4,8}. Comparing these two, we see that gcd(a,b) = 4.
# 
# Now imagine we take a = 11, b = 17. Both a and b are prime numbers. As a prime number has only itself and 1 as divisors, gcd(a,b) = 1.
# 
# We say that for any two integers a,b, if gcd(a,b) = 1 then a and b are coprime integers.
# 
# If a and b are prime, they are also coprime. If a is prime and b < a then a and b are coprime.
# 
# Think about the case for a prime and b > a, why are these not necessarily coprime?
# note to self: for example a is 17 b is 34 a is already a factor of b
# 
# 
# There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.
# 
# Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it.
# 
# Now calculate gcd(a,b) for a = 66528, b = 52920 and enter it below.

# I'm not going to try to brute force this lol
# euclid's algorithm for my purposes is this:
# The Algorithm
# The Euclidean Algorithm for finding GCD(A,B) is as follows:
# If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
# If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
# Write A in quotient remainder form (A = B⋅Q + R) (you can kind of skip this step, you basically input a%b, b into the return)
# Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
# i hate recursion

# basic reasoning is using recursion to say 'ive found a factor thats a factor yay'
# then we can find more factors with that
# idk
def euclid_algo(a, b):
    print("a is", a)
    print("b is", b)
    if a == 0:
        return b
    elif b == 0:
        return a
    print("a mod b is", a%b)
    return euclid_algo(b, a % b)

print( euclid_algo(66528, 52920) )