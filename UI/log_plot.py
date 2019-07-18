import numpy as np 
import matplotlib as plt

def log_plot(bu_x, bu_y, ug_x, ug_y):
    """
    Crtanje log plota
    ulaz:   array za x
            array za y
    
    izlaz je graf koji ima x scale 
    """

    plt.plot(bu_x, bu_y, label="Bušenje")
    plt.plot(ug_x, ug_y, label="Ugradnja")

    plt.legend()
    plt.title('Tehnički profil')
    plt.show()