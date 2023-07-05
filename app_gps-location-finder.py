#PyQt5 GUI lib
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import (QSize, pyqtSignal, Qt)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

#import osmnx as ox
#import geopandas as gpd
#import geopy as gpy
#from geopy.geocoders import Nominatim  # Required to get geo coordinates from the address

import sys

from src.geo_coder import GeoCoder
from src.gui_group_boxes import TopGroupBox, CenterGroupBox, ButtomGroupBox



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setMinimumSize(QSize(700, 700))
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("GPC Location Finder")

        # Main Menu
        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)

        #Create About ection
        aboutAction = QAction(QIcon('about.png'), '&About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('About application')
        aboutAction.triggered.connect(self.onAboutClicked)

        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(aboutAction)

        # Main Layout of app
        mainLayout = QVBoxLayout()

        # Top Group Box
        topGroupBox = TopGroupBox(self)
        topLayout = QVBoxLayout()
        topGroupBox.setLayout(topLayout)

        # Center Group Box
        centerGroupBox = CenterGroupBox(self)
        centerLayout = QVBoxLayout()
        centerGroupBox.setLayout(centerLayout)

        # Buttom Group Box
        buttomGroupBox = ButtomGroupBox(self)
        buttomLayout = QVBoxLayout()
        buttomGroupBox.setLayout(buttomLayout)

        geocoder = GeoCoder()
        buttomGroupBox.updateBtn.clicked.connect(lambda: geocoder.setAddress(topGroupBox.getAddress()))
        buttomGroupBox.updateBtn.clicked.connect(lambda: centerGroupBox.setLatitude(geocoder.getGPSLocation()))
        buttomGroupBox.updateBtn.clicked.connect(lambda: centerGroupBox.setLongitude(geocoder.getGPSLocation()))

        buttomGroupBox.clearBtn.clicked.connect(lambda: centerGroupBox.clearLCD())

        buttomGroupBox.radioButtonDD.toggled.connect(lambda: centerGroupBox.clearLCD())
        buttomGroupBox.radioButtonDD.toggled.connect(lambda: centerGroupBox.serFormat())
        buttomGroupBox.radioButtonDD.toggled.connect(lambda: centerGroupBox.serFormat())
        #buttomGroupBox.radioButtonDD.toggled.connect(lambda:  centerGroupBox.setLatitude(geocoder.getGPSLocation("Format DD:")))
        #buttomGroupBox.radioButtonDD.toggled.connect(lambda:  centerGroupBox.setLongitude(geocoder.getGPSLocation("Format DD:")))


        buttomGroupBox.radioButtonDD.toggled.connect(lambda: centerGroupBox.serFormat)
        buttomGroupBox.radioButtonDMS.toggled.connect(lambda: centerGroupBox.serFormat("Format DMS"))

        mainLayout.addWidget(topGroupBox)
        mainLayout.addWidget(centerGroupBox)
        mainLayout.addWidget(buttomGroupBox)
        self.setLayout(mainLayout)

        # It is a trick to add layer to the main window
        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    def onAboutClicked(self):

        msg =QMessageBox.about(self, "About GPS Location Finder", "<b> GPS Location Finder 0.1</b>"
                                              "<br> </br>"
                                            # "<br> </br>"
                                              "\nAllows to find GPS location by an address\n"
                                            "<br> </br>"
                                              #"\nCreated by: Iaroslav Zelinskyi\n"
                                                #"<br> </br>"
                                              #"\nE-mail: zelinskyi.iaroslav@gmail.com\n"
                                                 "<br> </br>"
                                                "\nDate & Place: Berlin, 2022")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
