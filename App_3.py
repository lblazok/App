def call(i):
    ''' Funkcija koja zove potrebni modul
    1 = calc_volume
    2 = calc_Q
    3 = calc_stress
    '''

    
    

    if i == 1:
        import calc_volume
    elif i == 2:
        import calc_Q
    elif i == 3:
        import calc_stress

def izbornik():
    ''' Izbor modula'''
    
    while True:
        while True:
                try:
                    i = int(input('''
Za izracunavanje volumena zasipa upisi 1\n
Za izracunavanje kapaciteta zdenca upisi 2\n
Za izracunavanje naprezanja upisi 3 
Unos: '''))
                except:
                    print('Unos mora biti broj!')
                    continue
                else:
                    break
        call(i)
        while True:
            try:
                a = str(input('''
Za povratak na izbornik upisi y \n
Za izlaz iz programa upisi n
Unos: ''' ))
            except:
                print('Unos mora biti y ili n')
                continue
            else:
                break
    
        if a == 'y':
            
            call(i)
        else:
            exit()


def main():

    izbornik()

main()