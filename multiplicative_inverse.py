## Ex: Multiplicative inverse of 1700 in Z200


def multiplicative_inverse(a, b):
    '''
    Finding multiplicative inverse of a in Zb
    '''
    d = {
        -1 : {
            'ri' : a,
            'qi' : None,
            'xi' : 1,
            'yi' : 0
            },
        0 : {
            'ri' : b,
            'qi' : None,
            'xi' : 0,
            'yi' : 1
            }
    }

    ri = None
    n = 0
    while ri != 0:
        n+=1
        ri = d[n-2]['ri'] % d[n-1]['ri']
        qi = d[n-2]['ri'] // d[n-1]['ri']
        xi = d[n-2]['xi'] - qi * d[n-1]['xi']
        yi = d[n-2]['yi'] - qi * d[n-1]['yi']

        d[n] = {
            'ri' : ri,
            'qi' : qi,
            'xi' : xi,
            'yi' : yi,
        }
    value = d[n-1]['xi']
    
    if value not in range(0,b):
        if value > b:
            value = value % b
        else:
            value = b - (abs(value) % b)
    
    return value


## Test
# d = multiplicative_inverse(15,26)
# print(d)


print(multiplicative_inverse(15, 26))