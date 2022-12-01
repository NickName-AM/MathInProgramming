## Ex: Multiplicative inverse of 1700 in Z200

from tabulate import tabulate

def multiplicative_inverse(a, b):
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
    
    #For table
    list=[]
    list.append([])
    list[0].extend(["ri","qi","xi","yi"])
    
    i=1
    for key,value in d.items():
        list.append([])
        list[i] = [value[data] for data in value]
        i += 1
    print(tabulate(list,headers='firstrow',tablefmt='fancy_grid'))

    #Multiplicative inverse
    # if d[n-1]['xi'] < 0:
        

    # print(d[n-1]['xi'])
    # print(b)

def main():
    multiplicative_inverse(15,26)



if __name__ == '__main__':
    main()

## Test
# d = multiplicative_inverse(15,26)
# print(d)

