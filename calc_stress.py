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

z = td - d
zw = rpv - d

if rpvyn == 'y':
    if td < rpv: #provjera da li je materijal iznad rpva
        sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
        sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
        return sigma_u_max, sigma_u_min
    else: #provjera da li je materijal ispod rpva
        sigma_u_vl_min = spec_tezina_vlazna_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s min tablicnom vrijednosti 
        sigma_u_vl_max = spec_tezina_vlazna_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je vlazan s max tablicnom vrijednosti 
        u = 1000 * zw # porni tlak na dubini
        return sigma_u_vl_max, sigma_u_vl_min, u
else:
    sigma_u_min = spec_tezina_suha_min[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s min tablicnom vrijednosti 
    sigma_u_max = spec_tezina_suha_max[vrs] * 9.81 * z #izracun ukupnog naprezanja materijala ako je suhi s max tablicnom vrijednosti
    return sigma_u_max, sigma_u_min


