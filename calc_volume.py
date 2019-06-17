def volumen_zasipa(d1, d2, h1, h2):
    '''
    Izracun potrebnog volumena zasipa
    ulazni podaci: fi busenja i fi ugradnje, dubina busenja i dubina ugradnje
    d1 = fi busenja [m]
    d2 = fi ugradnje [m]
    h1 = dubina busenja [m]
    h2 = dubina ugradnje [m]
    '''
    import math
    v1 = math.pi * (d1/2)**2 * h1 #izracun volumena valjka tj busenja
    v2 = math.pi * (d2/2)**2 *h2 #izracun volumena valjka tj ugradnje

    ans_v = float("{0:.2f}".format(v1 - v2)) #razlika volumena = volumen zasipa

    return ans_v
    


def unos_pod(i):
    '''
    Unos podataka u sustav. Nakon izrade UI taj modul unos_pod vise nece biti potreban
    '''
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    while True: # Unos podataka s provjerom tocnosti formata unosa
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
    i = int(input('Unesi broj profila busenja/ugradnje = '))
    
    ans = 0
    for x in range(i):
        ans += unos_pod(x)
    
    if ans < 0:
        print('Error - volumen ne moze biti negativan. \nProvjeri unesene podatke!')
    else:
        print("Volumen = " + str(ans))

    input('Pritisni "Enter" za izlaz')

main ()