from multiplicative_inverse import multiplicative_inverse
## Find a number x such that
## x mod 5 = 2
## x mod 7 = 3
## x mod 8 = 1
## x mod 9 = 8

# How to find the above value?
# a = find('2m5', '3m7', '1m8', '8m9')

def find(*args):
    # Getting the remainder. 5 in '5m7'
    results = [int(i.split('m')[0]) for i in args]


    # Getting the divisor. 7 in '5m7'
    divisors = [int(i.split('m')[1]) for i in args]


    # Multiplying divisors
    m = 1
    for divisor in divisors:
        m*=divisor


    m_m = []    
    b = []
    for divisor in divisors:
        r = m / divisor
        m_m.append(r)
        
        g = multiplicative_inverse(r, divisor)
        b.append(g)

    x = 0
    for m_mm, bb, rr in zip(m_m, b, results):
        x += m_mm * bb * rr

    x = int(x) % m

    return x


# Tests
# a = find('0m5', '2m6', '2m7', '10m11')
# print(a)