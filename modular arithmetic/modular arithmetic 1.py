# Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:
# 
# 4 + 9 = 1
# 5 - 7 = 10
# 2 + 3 = 5
# 
# At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).
# 
# You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).
# 
# Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m.
# 
# Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m | a) then a ≡ 0 mod m.
# 
# Calculate the following integers:
# 
# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17
# 
# The solution is the smaller of the two integers.

sol1 = 11 % 6
sol2 = 8146798528947 % 17
print("sol1 is", sol1, "and sol2 is", sol2)
print("likewise, 5 mod 6 is", 5 % 6, "and 4 mod 17 is", 4 % 17)

# explanation is a little bit confusing but basically what it means is that if a = b % m then 
# a % m = b is also the same thing
# basically if you have any equation in the form a = b % m then b % m = a % m