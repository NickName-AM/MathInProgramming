def gcd(a ,b):
    while b != 0:
        t = a
        # q = a // b
        a = b
        b = t % b
    
    g = a
    return g


## Tests
# g1 = gcd(7, 24) = 1 -> relatively prime or co-prime
# g2 = gcd(36, 10) = 2
# g3 = gcd(25, 60) = 5
# g4 = gcd(2740, 1760)
# print(g4)