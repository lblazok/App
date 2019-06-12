def calc_stress(d, vrs, rpvyn, rpv, db, dt):
    '''
    Izracunavanje naprezanja na odredenoj dubini.
    Pretpostavka je da su hotizontalna = vertikanim naprezanjima

    Ulaz:   Debljina sloja [m] d
            Vrsta materijala vrs
            rpvyn dali ima podzemne vode
            RPV [m] rpv
            Dubina busotine [m] db
            Trenutna dubina [m] dt

            

    Izlaz:  Ukupna naprezanja
            Efektivna naprezanja
            sigma min
            sigma max
            sigma min ef
            sigma max ef
            u
'''
    spec_tezina_suha_min = {'gravel': 15,
                        'sand': 13,
                        'silt': 14,
                        'clay': 14}

    spec_tezina_suha_max = {'gravel': 17,
                        'sand': 16,
                        'silt': 18,
                        'clay': 21}

    spec_tezina_vlazna_min = {'gravel': 20,
                        'sand': 18,
                        'silt': 18,
                        'clay': 16}

    spec_tezina_vlazna_max = {'gravel': 22,
                        'sand': 20,
                        'silt': 20,
                        'clay': 22}

    z = dt - d #dubina na kojoj racuna naprezanje
    zw = rpv - z #debljina stupca vode
    if rpvyn == 'y':
        if dt < rpv: #provjera da li je materijal iznad rpva
            sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
            sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
            
            return sigma_u_min, sigma_u_max
        else: #provjera da li je materijal ispod rpva
            sigma_u_vl_min = spec_tezina_vlazna_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s min tablicnom vrijednosti 
            sigma_u_vl_max = spec_tezina_vlazna_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s max tablicnom vrijednosti 
            u = 1000 * zw # porni tlak na dubini
            sigma_ef_min = sigma_u_vl_min - u
            sigma_ef_max = sigma_u_max - u

            return sigma_u_min, sigma_u_max, sigma_ef_min, sigma_ef_min, u
    else:
        sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
        sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
        
        return sigma_u_min, sigma_u_max

def unos_pod_s(rpvyn):
    '''
    Unos podataka za modul calc_stress
    '''
    i = 1
    ans_tot_min = 0
    ans_tot_max = 0
    ans_ef_min = 0
    ans_ef_max = 0
    u = 0 
    while True: #unos broja slojeva
        try:
            i = int(input('Unesi broj slojeva = '))
        except:
            print('Broj slojeva mora biti broj!')
            continue
        else:
            break

    
    
    while True: #unos RPV-a
        try:
            rpv = float(input('Unesi RPV [m] = '))
        except:
            print('Error - neispravan unos! \nRPV mora biti broj!')
            continue
        else:
            break

    while True: #unos dubine busotine
        try:
            db = input('Unesi dubinu busenja [m] = ')
        except:
            print('Error - neispravan unos! \nDubina busenja mora biti broj!')
            continue
        else:
            break
    dt = 0
    for x in range(i):
        while True: #unos debljine sloja
            try:
                d = input('Unesi debljinu sloja [m] = ')
            except:
                print('Error - neispravan unos! \nDebljina sloja mora biti broj!')
                continue
            else:
                break
        
    
        while True: #unos vrste materijala
            try:
                vrs = input('Unesi vrstu materijala \n(gravel/sand/silt/clay) = ')
            except:
                print('Error - neispravan unos! \nUnos mora biti gravel/sand/silt/clay')
                continue
            else:
                break

        dt += d

        if rpvyn == 'n':
            rpv = db
                
            ans_tot_min += calc_stress(d, vrs, rpvyn, rpv, db, dt)[0]
            ans_tot_max += calc_stress(d, vrs, rpvyn, rpv, db, dt)[1]
            return ans_tot_min, ans_tot_max, dt
        else:
            calc_stress(d, vrs, rpvyn, rpv, db, dt)
            ans_tot_min += calc_stress(d, vrs, rpvyn, rpv, db, dt)[0]
            ans_tot_max += calc_stress(d, vrs, rpvyn, rpv, db, dt)[1]
            ans_ef_min += calc_stress(d, vrs, rpvyn, rpv, db, dt)[2]
            ans_ef_min += calc_stress(d, vrs, rpvyn, rpv, db, dt)[3]
            u += calc_stress(d, vrs, rpvyn, rpv, db, dt)[4]
            
            return ans_tot_min, ans_tot_max, ans_ef_min, ans_ef_max, u, dt
    
          
def main():
    while True: #unos da li ima podzemne vode
        try:
            rpvyn = input('Da li postoji podataka o RPV-u [y/n] = ')
        except:
            print('Error - neispravan unos! \nUnesi y/n')
            continue
        else:
            breakn
    unos_pod_s(rpvyn)
    print('=============================================================================')
    if rpvyn == 'n':
        print('Ukupno minimalno naprezanje na dubini '+ str(unos_pod_s(rpvyn)[2])+ 'iznosi = '+ str(unos_pod_s(rpvyn)[0]) + '\n')
        print('Ukupno maksimalno naprezanje na dubini '+ str(unos_pod_s(rpvyn)[2])+ 'iznosi = '+ str(unos_pod_s(rpvyn)[1]) + '\n')
    
    else:
        print('Ukupno minimalno naprezanje na dubini od '+ str(unos_pod_s(rpvyn)[5])+ ' iznosi = '+ str(unos_pod_s(rpvyn)[0]))
        print('Efektivno minimalno naprezanje na dubini od '+ str(unos_pod_s(rpvyn)[5])+ ' iznosi = '+ str(unos_pod_s(rpvyn)[2]) + '\n')
        print('Ukupno maksimalno naprezanje na dubini od '+ str(unos_pod_s(rpvyn)[5])+ ' iznosi = '+ str(unos_pod_s(rpvyn)[1]))
        print('Efektivno maksimalno naprezanje na dubini od '+ str(unos_pod_s(rpvyn)[5])+ ' iznosi = '+ str(unos_pod_s(rpvyn)[3]) + '\n')
        print('Porni tlak na dubini od '+ str(unos_pod_s(rpvyn)[5])+ ' iznosi = '+ str(unos_pod_s(rpvyn)[4]) + '\n')
    
    input('Pritisni Enter za izlaz')

main()

    