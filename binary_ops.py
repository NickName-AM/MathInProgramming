def equalize_bits(a, b):
    a = str(a)
    b = str(b)

    la = len(a)
    lb = len(b)
    
    if la > lb:
        b = '0'*(la-lb) + b
    else:
        a = '0'*(lb-la) + a

    return (a, b)

def bin_add(a, b):
    a, b = equalize_bits(a, b)
    a = a[::-1]
    b = b[::-1]

    n = len(a)  # or 'b', it's the same
    c = 0       # carry
    s = ''

    for j in range(0, n):
        d = (int(a[j]) + int(b[j]) + c) // 2
        s += f'{int(a[j]) + int(b[j]) + c - 2*d}'
        c = d
    s+=str(c)

    return s[::-1]

def bin_mul(a, b):
    n = len(str(b))

    b = str(b)[::-1]

    bins = []

    for j in range(0, n):
        d = a * int(b[j]) * 10**j
        bins.append(d)
    
    s = 0
    for i in bins:
        s = bin_add(s, i)
    return s

