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

    z = dt - d
    zw = rpv - z
    res = []
    if rpvyn == 'y':
        if dt < rpv: #provjera da li je materijal iznad rpva
            sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
            sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
            res.append(sigma_u_min)
            res.append(sigma_u_max)
            return res
        else: #provjera da li je materijal ispod rpva
            sigma_u_vl_min = spec_tezina_vlazna_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s min tablicnom vrijednosti 
            sigma_u_vl_max = spec_tezina_vlazna_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s max tablicnom vrijednosti 
            u = 1000 * zw # porni tlak na dubini
            res.append(sigma_u_vl_min)
            res.append(sigma_u_vl_max)
            res.append(u)
            return res
    else:
        sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
        sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
        res.append(sigma_u_min)
        res.append(sigma_u_max)
        return res

def unos_pod_s():
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

    while True: #unos da li ima podzemne vode
        try:
            rpvyn = input('Da li postoji podataka o RPV-u [y/n] = ')
        except:
            print('Error - neispravan unos! \nUnesi y/n')
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
        else:
            calc_stress(d, vrs, rpvyn, rpv, db, dt)
            ans_tot_min += calc_stress(d, vrs, rpvyn, rpv, db, dt)[0]
            ans_tot_max += calc_stress(d, vrs, rpvyn, rpv, db, dt)[1]
            u += calc_stress(d, vrs, rpvyn, rpv, db, dt)[2]

    
          
    