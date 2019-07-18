# -*- coding: utf-8 -*-
def volumen_zasipa(d1, d2, h1, h2):
    '''
    Izracun potrebnog volumena zasipa
    ulazni podaci: fi busenja i fi ugradnje, dubina busenja i dubina ugradnje
    d1 = fi busenja [m]
    d2 = fi ugradnje [m]
    h1 = dubina busenja [m]
    h2 = dubina ugradnje [m]
    '''
    import math
    v1 = math.pi * (d1/2)**2 * h1 #izracun volumena valjka tj busenja
    v2 = math.pi * (d2/2)**2 *h2 #izracun volumena valjka tj ugradnje

    ans_v = float("{0:.2f}".format(v1 - v2)) #razlika volumena = volumen zasipa

    return ans_v