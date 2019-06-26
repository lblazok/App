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

import numpy as np
import matplotlib.pyplot as plt 

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
    

    
    
    if rpvyn == 'n': #Slucaj dok nema rpva
        return stress_n(d, vrs)
    elif dt[-1] > rpv and dt[-2] < rpv: # prelazni slucaj
        d_s = rpv - dt[-2]
        d_v = dt[-1] - rpv
        #if d_s + d_v == d:
        #a_min = stress_n(d_s, vrs)[0] + stress_y(d_v, vrs)[0]
        #a_max = stress_n(d_s, vrs)[1] + stress_y(d_v, vrs)[1]
        return stress_yn(d_s, d_v, vrs)
        
    else:                   # vlazni materijal
        return stress_y(d, vrs)
        

def stress_n(d, vrs):
    ''' racun naprezanja bez vode '''

    s_s_min = d * spec_tezina_suha_min[vrs]
    s_s_max = d * spec_tezina_suha_max[vrs]

    return s_s_min, s_s_max

def stress_y(d, vrs):
    '''Racun naprezanja s vodom'''

    s_v_min = d * spec_tezina_vlazna_min[vrs]
    s_v_max = d * spec_tezina_vlazna_max[vrs]

    return s_v_min, s_v_max

def stress_yn(d_s, d_v, vrs):
    ''' prelazni slucaj'''

    min = (d_s * spec_tezina_suha_min[vrs]) + (d_v * spec_tezina_vlazna_min[vrs])
    max = (d_s * spec_tezina_suha_max[vrs]) + (d_v * spec_tezina_vlazna_max[vrs])

    return min, max

def unos_pod_s(rpvyn, i):
    '''
    Unos podataka za modul calc_stress
    '''
    
    ans_tot_min = 0
    ans_tot_max = 0
    dt_a = [0] 
    dt_num = np.array([0])
    c_num_min = np.array([0])
    c_num_max = np.array([0])
    u_num = np.array([0])
    
    c_ef_num_min = np.array([0])
    c_ef_num_max = np.array([0])

    

    
    if rpvyn == 'y':
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
            db = float(input('Unesi dubinu busenja [m] = '))
        except:
            print('Error - neispravan unos! \nDubina busenja mora biti broj!')
            continue
        else:
            break
    dt = 0
    c=[]
    for x in range(i):
        while True: #unos debljine sloja
            try:
                d = float(input('Unesi ' + str(x+1) + '. debljinu sloja [m] = '))
            except:
                print('Error - neispravan unos! \nDebljina sloja mora biti broj!')
                continue
            else:
                break
        
    
        while True: #unos vrste materijala
            try:
                vrs = str(input('Unesi vrstu materijala \n(gravel/sand/silt/clay) = '))
            except:
                print('Error - neispravan unos! \nUnos mora biti gravel/sand/silt/clay')
                continue
            else:
                break
            
        dt += d
        
        dt_a.append(dt)
        dt_num = np.append(dt_num, dt)
    
        if rpvyn == 'n':
            rpv = db
            u_d_num = np.array(rpv)
            ans_tot_min = calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[0]
            ans_tot_max = calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[1]
            c.append(calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[0])
            c.append(calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[1])
            c_num_min = np.append(c_num_min, c_num_min[-1] + c[-2])
            c_num_max = np.append(c_num_max, c_num_max[-1] + c[-1])  
        else:
            
            
            #ans_tot_min = calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[0]
            #ans_tot_max = calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[1]
            u_d_num = np.array(rpv)
            u = 9.81 * (db-rpv)
            c.append(calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[0])
            c.append(calc_stress(d, vrs, rpvyn, rpv, db, dt_a)[1])
            c_num_min = np.append(c_num_min, c_num_min[-1] + c[-2])
            c_num_max = np.append(c_num_max, c_num_max[-1] + c[-1])
            u_d_num = np.append(u_d_num, db)
            
            
    if rpvyn == 'y':
        u_num = np.append(u_num, u)
        if rpv < dt:
                c_ef_num_min = np.append(c_ef_num_min, c_num_min[-1] - u)
                c_ef_num_max = np.append(c_ef_num_max, c_num_max[-1] - u)
    for x in range(0, len(c),2):
        ans_tot_min += c[x]
        
    for x in range(1, len(c), 2):
        ans_tot_max += c[x] 
            
    if rpvyn == 'n':
        return ans_tot_min, ans_tot_max, dt, c, c_num_min, c_num_max, dt_num
    else:     
        return ans_tot_min, ans_tot_max, u, dt, c, c_num_min, c_num_max, dt_num, c_ef_num_min, c_ef_num_max, u_num, u_d_num
    
def graf1(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    '''
    Crtanje grafova naprezanja
    Ulaz su array s podacima o dubini i vrijednostima naprezanja
    1 : min
    2 : max
    3 : u
    4 : ef min
    5 : ef max
    '''
    
    plt.style.use('ggplot') 
    plt.plot(x1, y1, label='Ukupno minimalno naprezanje')
    plt.plot(x2, y2, label='Ukupno maksimalno naprezanje')
    plt.plot(x3, y3, label='Porni tlak')
    plt.plot(x4, y4, label='Efektivno minimalno naprezanje')
    plt.plot(x5, y5, label='Efektivno maksimalno naprezanje')

    plt.gca().invert_yaxis()
    plt.xlabel('Naprezanja [kN/m^2]')
    plt.ylabel('Dubina [m]')
    plt.title('Naprezanja')
    plt.legend()
    plt.show()

def graf2(x1, y1, x2, y2):

    plt.style.use('ggplot') 
    plt.plot(x1, y1, label='Ukupno minimalno naprezanje')
    plt.plot(x2, y2, label='Ukupno maksimalno naprezanje')
    plt.gca().invert_yaxis()

    plt.xlabel('Naprezanja [kN/m^2]')
    plt.ylabel('Dubina [m]')

    plt.legend()
    plt.title('Naprezanja')
    plt.show()



def main():
    while True: #unos da li ima podzemne vode
        try:
            rpvyn = str(input('Da li postoji podataka o RPV-u [y/n] = '))
        except:
            print('Error - neispravan unos! \nUnesi y/n')
            continue
        else:
            break
    while True: #unos broja slojeva
        try:
            i = int(input('Unesi broj slojeva = '))
        except:
            print('Broj slojeva mora biti broj!')
            continue
        else:
            break
    res = []
    res = unos_pod_s(rpvyn,i)
    print('=============================================================================')
    if rpvyn == 'n':
        print('Ukupno minimalno naprezanje na dubini '+ str(res[2])+ ' m iznosi = '+ str(("{0:.2f}".format(res[4][-1])) + ' kN/m^2 \n'))
        print('Ukupno maksimalno naprezanje na dubini '+ str(res[2])+ ' m iznosi = '+ str(("{0:.2f}".format(res[5][-1])) + ' kN/m^2'))
        
        graf2(res[4], res[6], res[5], res[6])
        

    else:
        print('Ukupno minimalno naprezanje na dubini od '+ str(res[3])+ ' m iznosi = '+ str(("{0:.2f}".format(res[5][-1])+ ' kN/m^2')))
        print('Efektivno minimalno naprezanje na dubini od '+ str(res[3])+ ' m iznosi = '+ str(("{0:.2f}".format(res[8][-1]) + ' kN/m^2 \n')))
        print('Ukupno maksimalno naprezanje na dubini od '+ str(res[3])+ ' m iznosi = '+ str(("{0:.2f}".format(res[6][-1])+ ' kN/m^2')))
        print('Efektivno maksimalno naprezanje na dubini od '+ str(res[3])+ ' m iznosi = '+ str(("{0:.2f}".format(res[9][-1]) + ' kN/m^2 \n')))
        print('Porni tlak na dubini od '+ str(res[3])+ ' m iznosi = '+ str(("{0:.2f}".format(res[10][-1]) + ' kN/m^2 \n')))
        
        graf1(res[5], res[7], res[6], res[7], res[10], res[11], res[8], res[11], res[9], res[11])
            
    print('=============================================================================')
    
    

main()

    