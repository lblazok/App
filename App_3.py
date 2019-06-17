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
Za izračunavanje volumena zasipa upiši 1\n
Za izračunavanje kapaciteta zdenca upiši 2\n
Za izračunavanje naprezanja upiši 3 
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
Za povratak na izbornik upiši y \n
Za izlaz iz programa upiši n
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