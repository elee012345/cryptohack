#  As we've seen, we can work within a finite field Fp, adding and multiplying elements, and always obtain another element of the field.
#  
#  For all elements g in the field, there exists a unique integer d such that g * d ≡ 1 mod p.
#  
#  This is the multiplicative inverse of g.
#  
#  Example: 7 * 8 = 56 ≡ 1 mod 11
#  
#  What is the inverse element: 3 * d ≡ 1 mod 13?
#  
#   Think about the little theorem we just worked with. How does this help you find the inverse of an element?

# 9
# we just need to find an integer 1 larger than a multiple of 13 (modular arithmetic) and we'll get 1 which is also 1 mod 13
# number 1 larger than multiples of 13 are 14, 27, 40, etc.
# 27 is a multiple of 3 as well, and 3 * 9 = 27, so the answer is 9