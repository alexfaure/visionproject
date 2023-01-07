# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IHM_principale.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from game_ui_class import *

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
