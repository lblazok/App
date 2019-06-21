import matplotlib.pyplot as plt 
import numpy as np
from calc_stress import rpvyn, c_num_min, c_num_max, dt_num

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
    
    plt.plot(x1, y1, label='Ukupno minimalno naprezanje')
    plt.plot(x2, y2, label='Ukupno maksimalno naprezanje')
    plt.plot(x3, y3, label='Porni tlak')
    plt.plot(x4, y4, label='Efektivno minimalno naprezanje')
    plt.plot(x5, y5, label='Efektivno maksimalno naprezanje')

    plt.title('Naprezanja')
    plt.legend()
    plt.show

def graf2(x1, y1, x2, y2):


    plt.plot(x1, y1, label='Ukupno minimalno naprezanje')
    plt.plot(x2, y2, label='Ukupno maksimalno naprezanje')

    plt.legend()
    plt.title('Naprezanja')
    plt.show()

def main1():

    if rpvyn == 'n':
        return graf2(c_num_min, dt_num, c_num_max, dt_num)


