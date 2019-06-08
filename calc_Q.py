def calc_Q(l, fi, n, vm):
    '''
    ulaz:   Duljina filtera
            Promjer zdenca
            Propusnost filtera
            Maks. ulazna brzina
    
    racun:  Polumjer = promjer/2
            Opseg = 2* r *PI
            povrsina = duljina * opseg
            povrsina ulaza = povrsina * propusnost
            maks kapacitet = ulazna brzina * povrsina ulaza
    '''
    import math

    r = fi/2
    opseg = 2 * r * math.pi
    povrsina = l * opseg
    pov_ulaza = povrsina * n
    max_kap = float("{0:.5f}".format(pov_ulaza * vm))

    return max_kap

def unos_par():
    '''
    unos podataka
    '''
    while True:
        try:
            l = float(input('Unesi duljinu filtera [m]: '))
        except:
            print('Dubilja filetra mora biti broj!!!!')
            continue
        else:
            break

    while True:
        try:
            fi = float(input('Unesi promjer ugradnje [m]: '))
        except:
            print('Promjer ugradnje mora biti broj!!!!')
            continue
        else:
            break
    
    while True:
        try:
            n = float(input('Unesi propusnost filtera (0.00 - 0.50): '))
        except:
            print('Propusnost filtera mora biti broj!!!!')
            continue
        else:
            break

    while True:
        try:
            vm = float(input('Unesi ulaznu brzinu vode u ugradnju (0.01 - 0.06 m/s): '))
        except:
            print('Ulazna brzina mora biti broj!!!!')
            continue
        else:
            break
    
    ans = calc_Q(l, fi, n ,vm)
    return ans
    

def main():

    ans = float("{0:.5f}".format(unos_par()))
    opt_ans = float("{0:.5f}".format(ans * 0.7))
    print('Maksimalni kapacitet zdenca = ' + str(ans) + ' m^3/s' + ' ---> ' + str(ans*1000) + ' l/s')
    print('Optimani kapacitet zdenca = ' + str(opt_ans) + ' m^3/s'+ ' ---> ' + str(opt_ans*1000) + ' l/s' )
    input('Pritisni Enter za izlaz')

main()