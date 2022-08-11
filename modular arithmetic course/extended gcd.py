# Let a and b be positive integers.
# 
# The extended Euclidean algorithm is an efficient way to find integers u,v such that
# 
# a * u + b * v = gcd(a,b)
# 
#  Later, when we learn to decrypt RSA, we will need this algorithm to calculate the modular inverse of the public exponent.
# 
# 
# Using the two primes p = 26513, q = 32321, find the integers u,v such that
# 
# p * u + q * v = gcd(p,q)
# 
# Enter whichever of u and v is the lower number as the flag.
# 
#  Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.

# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html why was this not here on the previous challenge

# this makes so much sense
#  Extended Euclidean algorithm also finds integer coefficients x and y such that: 
#  
#    ax + by = gcd(a, b) 
# Examples:  
# 
# Input: a = 30, b = 20
# Output: gcd = 10
#         x = 1, y = -1
# (Note that 30*1 + 20*(-1) = 10)
# 
# Input: a = 35, b = 15
# Output: gcd = 5
#         x = 1, y = -2
# (Note that 35*1 + 15*(-2) = 5)


# much confusion
# only some copy paste

def euclid_algo(a, b):
    if a == 0:
        return b
    return euclid_algo(b % a, a)

def extended_euclid_algo(a, b):

    # keeps running this first part until the below condition is satisfied
    if a == 0:
        return b, 0, 1
    # once we actually assign this value we find the u and v for the numbers
    gcd, u, v = extended_euclid_algo(b % a, a)


    # now we move back through the functions and constantly update these numbers
    # when we reach the function called first then we have our answer
    new_u = v - ( b // a ) * u
    new_v = u
    return gcd, new_u, new_v

    

print( extended_euclid_algo(26513, 32321) )