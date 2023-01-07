from PyQt5 import QtCore, QtGui, QtWidgets
import os
from game_logic import *


class image(object):
    def setup_image(self):

        self.dir = "./ressources/"  # Dossier ou se trouve les images
        list_file = os.listdir(self.dir)
        filename = []
        for file in list_file:
            if file.endswith('.jpg'):
                # image=Image.open(dir+file)
                filename.append(self.dir + file)
        self.n = 0
        self.filename = filename.copy()
        self.file = self.filename[self.n]

    def next_image(self):
        self.n += 1
        self.file = self.filename[self.n]


class joueur(object):
    def __init__(self):
        self.name = []
        self.score = []
        self.total = []

    def Total(self):
        self.total = sum(self.score)

    def naming(self, name):
        self.name = name

    def add_score(self, point):
        self.score.append(point)
        self.Total()


class Tableau_score(object):
    def __init__(self):
        self.nb_joueur = 2
        self.jactif = 0
        self.joueurs = [joueur()] * self.nb_joueur

    def iniTab(self, nb_joueur):
        self.nb_joueur = nb_joueur
        self.joueurs = []
        for i in range(self.nb_joueur):
            jt = joueur()
            jt.name = "j" + str(i + 1)
            self.joueurs.append(jt)
        # test initialisation

    def fin_tab(self):
        i = 1
        for j in self.joueurs:
            j.name = "j" + str(i)
            for s in range(15):
                j.add_score(s * i)
            j.Total()
            i += 1

    def next(self,score):
        # Permet d'ajouter le score calculer et de passer à l'autre joueurs
        self.joueurs[self.jactif].add_score(score)
        self.jactif = (self.jactif + 1) % self.nb_joueur  # ajouter le modulo nb joueur


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        im = image()
        im.setup_image()

        self.listLetters = [['A', 1], ['B', 3], ['C', 3], ['D', 2], ['E', 1], ['F', 4], ['G', 2], ['H', 4], ['I', 1],
                            ['J', 8], ['K', 5], ['L', 1], ['M', 3], ['N', 1], ['O', 1], ['P', 3], ['Q', 10], ['R', 1],
                            ['S', 1], ['T', 1], ['U', 1], ['V', 4], ['W', 4], ['X', 8], ['Y', 4], ['Z', 10]]
        self.listWords = open(r"ressources\\ods6.txt").read().splitlines()
        self.nbTours = 0

        self.Listeprecedente = []
        self.Listenouvelle = []
        self.listScore = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 980)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 690, 111, 61))
        self.pushButton.setObjectName("Joueur suivant")

        tab = Tableau_score()
        tab.iniTab(2)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(780, 120, 300, 300))
        self.table.setObjectName("tableView")
        self.table.setColumnCount(tab.nb_joueur)
        self.table.setRowCount(len(tab.joueurs[0].score))
        my_array = []
        jname = []
        for j in tab.joueurs:
            my_array.append(j.score)
            jname.append(j.name)

        self.table.setHorizontalHeaderLabels(jname)
        self.table.resizeColumnsToContents()

        self.total = QtWidgets.QTableWidget(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(780, 120 + 300, 300, 75))
        self.total.setObjectName("totalView")
        self.total.setColumnCount(tab.nb_joueur)
        self.total.setRowCount(1)
        self.total.setHorizontalHeaderLabels(jname)
        self.total.setVerticalHeaderLabels(["Total"])
        self.total.resizeColumnsToContents()

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(20, 20, 480, 480))
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

        print(im.filename)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()
        self.pushButton.clicked.connect(lambda: self.show_next(im, tab))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Joueur suivant"))
        # self.label.setText(_translate("MainWindow", "Image de la partie"))

    def show_next(self, im, tab):
        # Début du traitement de l'image
        img_ = cv2.imread(im.file, cv2.IMREAD_GRAYSCALE)
        print('imhere2', type(img_))
        thresholdedImg_ = traitement_images(img_)
        print('imhere3')
        result_List = detection_mot(thresholdedImg_)
        print("result: ", result_List)
        res, resIndex_ = ajoutdesindicesencommun(result_List)
        for i in resIndex_:
            if i == 0:
                res[i] = demand_letter_after(res[i], res[i + 1])
            elif i == len(res) - 1:
                res[i] = demand_letter_before(res[i], res[i - 1])
            else:
                res[i] = demand_letter_both(res[i], res[i - 1], res[i + 1])
        print(res)
        for j in res:
            score_ = score_mot(self.listLetters, j, self.listWords)
            self.listScore.append(score_)
            print("mot: ", j, "score: ", score_)

        print('old list l181', self.Listeprecedente)
        if self.nbTours > 0:
            self.Listenouvelle = [ele for ele in res]
            for a in self.Listeprecedente:
                if a in res:
                    self.Listenouvelle.remove(a)
        self.Listeprecedente = res
        print('new word in the list l190', self.Listenouvelle)
        print('old list l190', self.Listeprecedente)

        if self.nbTours < 1:
            score = score_mot(self.listLetters, self.Listeprecedente[0], self.listWords)
        else:
            score = score_mot(self.listLetters, self.Listenouvelle[0], self.listWords)
        # ajouter score au tableau pour faire le total des points

        self.photo.setPixmap(QtGui.QPixmap(im.file))
        j = tab.jactif
        tab.next(score)
        i = len(tab.joueurs[j].score) - 1
        # print(j, i)
        self.table.setRowCount(len(tab.joueurs[0].score))
        self.table.setItem(i, j, QtWidgets.QTableWidgetItem(str(tab.joueurs[j].score[i])))
        self.total.setItem(0, j, QtWidgets.QTableWidgetItem(str(tab.joueurs[j].total)))

        self.table.resizeColumnsToContents()
        self.total.resizeColumnsToContents()
        self.nbTours += 1
        # print(tab.joueurs[j].score)
        im.next_image()
