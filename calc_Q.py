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

    r = fi/2 #izracun radijusa iz promjera
    opseg = 2 * r * math.pi # izracun opsega
    povrsina = l * opseg #izracun povrsine cijevi
    pov_ulaza = povrsina * n #izracun površine ulaza vode u zdenac (propusnost filtera)
    max_kap = float("{0:.5f}".format(pov_ulaza * vm)) #maksimalni kapacitet koji moze dati ta duljina filetra

    return max_kap

def unos_par():
    '''
    unos podataka
    '''
    while True:
        try:
            l = float(input('Unesi duljinu filtera [m]: '))  #unos podata s provjerom tocnosti ulaza da se ibjegnu neocekivani errori
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
    
    ans = calc_Q(l, fi, n ,vm) # izracun kapaciteta filtera iz unesenih podataka
    return ans
    

def main():

    ans = unos_par()
    opt_ans = float("{0:.5f}".format(ans * 0.7)) # optimalni kapacitet zdenca koji je 70% maksimalnog
    print('Maksimalni kapacitet zdenca = ' + str(ans) + ' m^3/s' + ' ---> ' + str(ans*1000) + ' l/s')
    print('Optimani kapacitet zdenca = ' + str(opt_ans) + ' m^3/s'+ ' ---> ' + str(opt_ans*1000) + ' l/s' )
    input('Pritisni Enter za izlaz')

main()