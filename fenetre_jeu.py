# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM_principale.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os   

class image(object):
    def setup_image(self):
        
        self.dir="./image/" #Dossier ou se trouve les images
        list_file=os.listdir(self.dir)
        filename=[]
        for file in list_file:
            if file.endswith('.jpg'):
                # image=Image.open(dir+file) 
                filename.append(self.dir+file)
        self.n=0
        self.filename=filename.copy()
        self.file=self.filename[self.n]
    
    def next_image(self):
        self.n+=1
        self.file=self.filename[self.n]
        
        
class joueur(object):
    def __init__(self):
        self.name=[]
        self.score=[]
        self.total=[]
        
    def Total(self):
        self.total=sum(self.score)
        
    def naming(self,name):
        self.name = name
    
    def add_score(self,point):
        self.score.append(point)
        self.Total()
        
        
    
class Tableau_score(object):
    def __init__(self):
        self.nb_joueur=4
        self.jactif=0
        self.joueurs=[joueur()]*self.nb_joueur
    
    def iniTab(self,nb_joueur):
        self.nb_joueur=nb_joueur
        self.joueurs=[]
        for i in range(self.nb_joueur):
            jt=joueur()
            jt.name="j"+str(i+1)
            self.joueurs.append(jt)
        #test initialisation
        
            
    def fin_tab(self):
        i=1
        for j in self.joueurs:
            j.name="j"+str(i)
            for s in range(15):
                j.add_score(s*i)
            j.Total()
            i+=1
    
    def next(self):
        # Permet d'ajouter le score calculer et de passer à l'autre joueurs
        self.joueurs[self.jactif].add_score(5)    
        self.jactif=(self.jactif+1)%self.nb_joueur #ajouter le modulo nb joueur


    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        im=image()
        im.setup_image()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 980)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 690, 111, 61))
        self.pushButton.setObjectName("Joueur suivant")
    
        tab=Tableau_score()
        tab.iniTab(4)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(780, 120, 300, 300))
        self.table.setObjectName("tableView")
        self.table.setColumnCount(tab.nb_joueur)
        self.table.setRowCount(len(tab.joueurs[0].score))
        my_array=[]
        jname=[]
        for j in tab.joueurs:
            my_array.append(j.score)
            jname.append(j.name)
        
        self.table.setHorizontalHeaderLabels(jname)
        self.table.resizeColumnsToContents()
        
        self.total =QtWidgets.QTableWidget(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(780, 120+300, 300, 75))
        self.total.setObjectName("totalView")
        self.total.setColumnCount(tab.nb_joueur)
        self.total.setRowCount(1)
        self.total.setHorizontalHeaderLabels(jname)
        self.total.setVerticalHeaderLabels(["Total"])
        self.total.resizeColumnsToContents()

        self.photo =QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(20,20,480,480))
        self.photo.setText("photo")
        self.photo.setPixmap(QtGui.QPixmap())
        self.photo.setScaledContents(True)
        self.photo.setObjectName("image partie")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(20, 60, 101, 21))
        # self.label.setObjectName("label")
        
        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(400, 670, 256, 192))
        # self.graphilcsView.setObjectName("graphicsView")
        
        # self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()
        self.pushButton.clicked.connect(lambda: self.show_next(im,tab))
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Joueur suivant"))
        # self.label.setText(_translate("MainWindow", "Image de la partie"))

    def show_next(self,im,tab):
        im.next_image()
        self.photo.setPixmap(QtGui.QPixmap(im.file))
        j=tab.jactif
        tab.next()
        i=len(tab.joueurs[j].score)-1
        # print(j,i)
        self.table.setRowCount(len(tab.joueurs[0].score))
        self.table.setItem(i,j,QtWidgets.QTableWidgetItem(str(tab.joueurs[j].score[i])))
        self.total.setItem(0,j,QtWidgets.QTableWidgetItem(str(tab.joueurs[j].total)))
        
        self.table.resizeColumnsToContents()
        self.total.resizeColumnsToContents()
        # print(tab.joueurs[j].score)
        
        
        
if __name__ == "__main__":
    import sys
    from PIL import Image
    import os   
    import time
    
    
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    sys.exit(app.exec_())
    
