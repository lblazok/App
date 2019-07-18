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
    pov_ulaza = povrsina * n #izracun povrsine ulaza vode u zdenac (propusnost filtera)
    max_kap = float("{0:.5f}".format(pov_ulaza * vm)) #maksimalni kapacitet koji moze dati ta duljina filetra
    opt_kap = float("{0:.5f}".format(pov_ulaza * vm * 0.7)) #optimalni kapacitet
    return max_kap