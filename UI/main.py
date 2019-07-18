from PyQt5 import QtWidgets
 
from app_ui import Ui_Program  # importing our generated file
 
import sys
from ui_calc_q_p import *
from ui_vol import *
 
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
 
        super(mywindow, self).__init__()

        
 
        self.ui = Ui_Program()
    
        self.ui.setupUi(self)
        self.ui.Q_gumb.clicked.connect(self.izracun_q) #klik na gumb racun na tabu Q vode
        self.ui.vol_novi_profil.clicked.connect(self.novi_stupac) #dodavanje novog stupca u tablici za izracun volumena na klik gumba
        self.ui.vol_racun_gumb.clicked.connect(self.racun_vol) #izracun volumena na klik

    def izracun_q(self): #izracun kolicine vode 

        l = float(self.ui.u_l.text()) #uzimanje vrijednosti iz polja i pretvaranje u float
        fi = float(self.ui.u_fi.text())
        n = float(self.ui.u_n.text())
        vm = float(self.ui.u_vm.text())

        ans = calc_Q(l, fi, n, vm)
        res = ( #ispis
            'Maksimalni kapacitet zdenca = ' + str(ans) + ' m^3/s' + ' ---> ' + str(ans*1000) + ' l/s''\n'
            'Optimani kapacitet zdenca = ' + str(ans * 0.7) + ' m^3/s'+ ' ---> ' + str(ans * 0.7 *1000) + ' l/s'
        )   
        self.ui.Izlaz.setText(res)  #dodavanje ispisa polju za rezultate

    def novi_stupac(self): # funkcija za dodavanje novog stupca tablici
        columnPosition = self.ui.tablica_volumen.columnCount()
        self.ui.tablica_volumen.insertColumn(columnPosition) 

    def racun_vol(self): #funkcija za racunanje volumena
        ans = 0
        i = self.ui.tablica_volumen.columnCount()
        res = []
        for row in range(i):
            array = []
            for col in range(4):
                array.append(float(self.ui.tablica_volumen.item(col,row).text()))
            
            res.append(volumen_zasipa(array[0], array[2], array[1], array[3]))
        
        for i in range(len(res)):
            ans += res[i]
        
        ans_str = "Volumen = " + str(ans) + " m^3"
        self.ui.vol_izlaz.setText(ans_str) #Ispis rezultata



app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())