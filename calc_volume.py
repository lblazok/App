def volumen_zasipa(d1, d2, h1, h2):
    '''
    Izracun potrebnog volumena zasipa
    ulazni podaci: fi bušenja i fi ugradnje, dubina bušenja i dubina ugradnje
    d1 = fi bušenja [m]
    d2 = fi ugradnje [m]
    h1 = dubina bušenja [m]
    h2 = dubina ugradnje [m]
    '''
    import math
    v1 = math.pi * (d1/2)**2 * h1
    v2 = math.pi * (d2/2)**2 *h2

    ans_v = float("{0:.2f}".format(v1 - v2))

    if ans_v < 0:
        return "Error - provjeri unesene podatke"
    else:
        return ans_v
    


def unos_pod(i):
    '''
    Unos podataka u sustav. Nakon izrade UI taj modul unos_pod vise nece biti potreban
    '''
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    while True:
        try:
            d1 = float(input('Unesi fi ' + str(i+1).translate(SUB) +' busenja [m] =  '))
        except:
            print('Unos mora biti broj!!!!')
            continue
        else:
            break
    
    while True:
        try:
            d2 = float(input('Unesi fi '+ str(i+1).translate(SUB) +' ugradnje [m] = '))
        except:
            print('Unos mora biti broj!!!!')
            continue
        else:
            break

    while True:
        try:
            h1 = float(input('Unesi dubinu '+ str(i+1).translate(SUB) +' busenja [m] = '))
        except:
            print('Unos mora biti broj!!!!')
            continue
        else:
            break

    while True:
        try:
            h2 = float(input('Unesi dubinu '+ str(i+1).translate(SUB) +' ugradnje [m] = ' ))
        except:
            print('Unos mora biti broj!!!!')
            continue
        else:
            break
    
    
    

    ans = volumen_zasipa(d1, d2, h1, h2)
    
    return ans

def main():
    i = int(input('Unesi broj profila bušenja/ugradnje = '))
    
    ans = 0
    for x in range(i):
        ans += unos_pod(x)
    
    print("Volumen = " + str(ans))

    input('Pritisni "Enter" za izlaz')

main ()