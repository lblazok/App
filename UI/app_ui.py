# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Program(object):
    def setupUi(self, Program):
        Program.setObjectName("Program")
        Program.resize(1105, 776)
        self.centralwidget = QtWidgets.QWidget(Program)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Pocetni_frame = QtWidgets.QFrame(self.centralwidget)
        self.Pocetni_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pocetni_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Pocetni_frame.setObjectName("Pocetni_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.Pocetni_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.Moduli = QtWidgets.QTabWidget(self.Pocetni_frame)
        self.Moduli.setTabPosition(QtWidgets.QTabWidget.North)
        self.Moduli.setObjectName("Moduli")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Q_gumb = QtWidgets.QPushButton(self.tab)
        self.Q_gumb.setGeometry(QtCore.QRect(710, 240, 141, 51))
        self.Q_gumb.setCheckable(False)
        self.Q_gumb.setDefault(False)
        self.Q_gumb.setFlat(False)
        self.Q_gumb.setObjectName("Q_gumb")
        self.Izlaz = QtWidgets.QTextBrowser(self.tab)
        self.Izlaz.setGeometry(QtCore.QRect(290, 370, 541, 111))
        self.Izlaz.setObjectName("Izlaz")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(286, 150, 366, 156))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.u_l = QtWidgets.QLineEdit(self.layoutWidget)
        self.u_l.setObjectName("u_l")
        self.horizontalLayout_5.addWidget(self.u_l, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.u_fi = QtWidgets.QLineEdit(self.layoutWidget)
        self.u_fi.setObjectName("u_fi")
        self.horizontalLayout_4.addWidget(self.u_fi, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.u_n = QtWidgets.QLineEdit(self.layoutWidget)
        self.u_n.setObjectName("u_n")
        self.horizontalLayout_3.addWidget(self.u_n, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.u_vm = QtWidgets.QLineEdit(self.layoutWidget)
        self.u_vm.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.u_vm.setObjectName("u_vm")
        self.horizontalLayout.addWidget(self.u_vm, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(290, 350, 58, 18))
        self.label_5.setObjectName("label_5")
        self.Moduli.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tablica_volumen = QtWidgets.QTableWidget(self.tab_2)
        self.tablica_volumen.setGeometry(QtCore.QRect(20, 50, 421, 171))
        self.tablica_volumen.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.tablica_volumen.setTabKeyNavigation(True)
        self.tablica_volumen.setAlternatingRowColors(True)
        self.tablica_volumen.setShowGrid(True)
        self.tablica_volumen.setGridStyle(QtCore.Qt.SolidLine)
        self.tablica_volumen.setWordWrap(True)
        self.tablica_volumen.setCornerButtonEnabled(True)
        self.tablica_volumen.setRowCount(1)
        self.tablica_volumen.setColumnCount(4)
        self.tablica_volumen.setObjectName("tablica_volumen")
        item = QtWidgets.QTableWidgetItem()
        self.tablica_volumen.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tablica_volumen.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tablica_volumen.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tablica_volumen.setHorizontalHeaderItem(3, item)
        self.tablica_volumen.horizontalHeader().setCascadingSectionResizes(False)
        self.tablica_volumen.horizontalHeader().setHighlightSections(False)
        self.tablica_volumen.horizontalHeader().setSortIndicatorShown(False)
        self.tablica_volumen.horizontalHeader().setStretchLastSection(False)
        self.vol_novi_profil = QtWidgets.QPushButton(self.tab_2)
        self.vol_novi_profil.setGeometry(QtCore.QRect(20, 240, 151, 51))
        self.vol_novi_profil.setObjectName("vol_novi_profil")
        self.vol_racun_gumb = QtWidgets.QPushButton(self.tab_2)
        self.vol_racun_gumb.setGeometry(QtCore.QRect(200, 240, 151, 51))
        self.vol_racun_gumb.setObjectName("vol_racun_gumb")
        self.vol_izlaz = QtWidgets.QTextBrowser(self.tab_2)
        self.vol_izlaz.setGeometry(QtCore.QRect(20, 410, 411, 251))
        self.vol_izlaz.setObjectName("vol_izlaz")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 380, 58, 18))
        self.label_11.setObjectName("label_11")
        self.graf_vol = QtWidgets.QGraphicsView(self.tab_2)
        self.graf_vol.setGeometry(QtCore.QRect(600, 50, 461, 611))
        self.graf_vol.setObjectName("graf_vol")
        self.Moduli.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.Moduli, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.Pocetni_frame)
        Program.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Program)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1105, 30))
        self.menubar.setObjectName("menubar")
        self.menuIzra_un_parametara_zdenca = QtWidgets.QMenu(self.menubar)
        self.menuIzra_un_parametara_zdenca.setObjectName("menuIzra_un_parametara_zdenca")
        Program.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Program)
        self.statusbar.setObjectName("statusbar")
        Program.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(Program)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(Program)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionOpen = QtWidgets.QAction(Program)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Program)
        self.actionClose.setObjectName("actionClose")
        self.menuIzra_un_parametara_zdenca.addSeparator()
        self.menuIzra_un_parametara_zdenca.addAction(self.actionSave)
        self.menuIzra_un_parametara_zdenca.addAction(self.actionSave_as)
        self.menuIzra_un_parametara_zdenca.addAction(self.actionOpen)
        self.menuIzra_un_parametara_zdenca.addAction(self.actionClose)
        self.menubar.addAction(self.menuIzra_un_parametara_zdenca.menuAction())

        self.retranslateUi(Program)
        self.Moduli.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Program)
        Program.setTabOrder(self.u_l, self.u_fi)
        Program.setTabOrder(self.u_fi, self.u_n)
        Program.setTabOrder(self.u_n, self.u_vm)
        Program.setTabOrder(self.u_vm, self.Q_gumb)
        Program.setTabOrder(self.Q_gumb, self.Izlaz)

    def retranslateUi(self, Program):
        _translate = QtCore.QCoreApplication.translate
        Program.setWindowTitle(_translate("Program", "MainWindow"))
        self.Q_gumb.setText(_translate("Program", "Izračun"))
        self.label.setText(_translate("Program", "Duljina filtra [m]"))
        self.u_l.setToolTip(_translate("Program", "<html><head/><body><p>Unesi duljinu filtra u metrima (npr. 10)</p></body></html>"))
        self.label_2.setText(_translate("Program", "Promjer filtra [m]"))
        self.u_fi.setToolTip(_translate("Program", "<html><head/><body><p>Unesi promjer filtra u metrima (npr. 0.125) KORISTI DECIMALNU TOČKU!</p></body></html>"))
        self.label_3.setText(_translate("Program", "Propusnost filtra [%]"))
        self.u_n.setToolTip(_translate("Program", "<html><head/><body><p>Unesi propusnost filtra (npr. 0.25) KORISTI DECIMALNU TOČKU!</p></body></html>"))
        self.label_4.setText(_translate("Program", "Maks. ulazna brzina (0,01 - 0,06 m/s)"))
        self.u_vm.setToolTip(_translate("Program", "<html><head/><body><p>Unesi maksimalnu ulaznu brzinu u m/s (npr. 0.03) KORISTI DECIMALNU TOČKU!</p></body></html>"))
        self.label_5.setText(_translate("Program", "Rezultat:"))
        self.Moduli.setTabText(self.Moduli.indexOf(self.tab), _translate("Program", "Izračun količine crpljenja"))
        self.tablica_volumen.setToolTip(_translate("Program", "<html><head/><body><p>Unesi podatke o bušenju i ugradnji u metrima.</p><p>KORISTI DECIMALNU TOČKU!</p></body></html>"))
        self.tablica_volumen.setSortingEnabled(False)
        item = self.tablica_volumen.horizontalHeaderItem(0)
        item.setText(_translate("Program", "Ø bušenja"))
        item = self.tablica_volumen.horizontalHeaderItem(1)
        item.setText(_translate("Program", "Dubina bušenja"))
        item = self.tablica_volumen.horizontalHeaderItem(2)
        item.setText(_translate("Program", "Ø ugradnje"))
        item = self.tablica_volumen.horizontalHeaderItem(3)
        item.setText(_translate("Program", "Dubina ugradnje"))
        self.vol_novi_profil.setText(_translate("Program", "Dodaj novi profil"))
        self.vol_racun_gumb.setText(_translate("Program", "Izračun"))
        self.label_11.setText(_translate("Program", "Rezultat:"))
        self.Moduli.setTabText(self.Moduli.indexOf(self.tab_2), _translate("Program", "Izračun volumena"))
        self.menuIzra_un_parametara_zdenca.setTitle(_translate("Program", "Fi&le"))
        self.actionSave.setText(_translate("Program", "&Save"))
        self.actionSave_as.setText(_translate("Program", "Sa&ve as"))
        self.actionOpen.setText(_translate("Program", "&Open"))
        self.actionClose.setText(_translate("Program", "&Close"))
