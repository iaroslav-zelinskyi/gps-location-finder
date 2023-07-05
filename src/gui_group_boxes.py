#PyQt5 GUI lib
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import (QSize, pyqtSignal, Qt)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class TopGroupBox(QGroupBox):

    def __init__(self, parent):
        super(TopGroupBox, self).__init__(parent)

        # Create a form layout for the label and line edit
        self.setTitle("Input:")
        self.inputLayout = QFormLayout()

        self.home_address = 'Newtonstraße 14, 12489 Berlin'

        self.addr_line_edit = QLineEdit(self.home_address)

        self.inputLayout.addRow('Address:', self.addr_line_edit)
        self.inputLayout.addRow('', QLabel())
        self.setLayout(self.inputLayout)

    def getAddress(self):
        return self.addr_line_edit.text()


class CenterGroupBox(QGroupBox):

    def __init__(self, parent):
        super(CenterGroupBox, self).__init__(parent)

        self.setTitle("GPC location:")
        self.centerGridLayout = QGridLayout()
        self.labelLatitude = QLabel("Latitude (N):")
        labelGrad = QLabel("°")
        labelMinutes = QLabel("'")
        labelSeconds = QLabel("\"")

        # create QLCDNumber object Latitudes
        self.lcdLatGrad = QLCDNumber()
        self.lcdLatMinutes = QLCDNumber()
        self.lcdLatSeconds = QLCDNumber()

        # create QLCDNumber object Longitudes
        self.lcdLongGrad = QLCDNumber()
        self.lcdLongMinutes = QLCDNumber()
        self.lcdLongSeconds = QLCDNumber()

        self.labelFormat = QLabel("Format DMS:")
        labelLongitude = QLabel("Longitude (E):")
        self.centerGridLayout.addWidget(self.labelFormat, 0, 0)

        self.centerGridLayout.addWidget(self.labelLatitude, 1, 0)
        self.centerGridLayout.addWidget(self.lcdLatGrad, 1, 1)
        self.centerGridLayout.addWidget(labelGrad, 1, 2)
        self.centerGridLayout.addWidget(self.lcdLatMinutes, 1, 3)
        self.centerGridLayout.addWidget(labelMinutes, 1, 4)
        self.centerGridLayout.addWidget(self.lcdLatSeconds, 1, 5)
        self.centerGridLayout.addWidget(labelSeconds, 1, 6)

        self.centerGridLayout.addWidget(labelLongitude, 2, 0)
        self.centerGridLayout.addWidget(self.lcdLongGrad, 2, 1)
        self.centerGridLayout.addWidget(labelGrad, 2, 2)
        self.centerGridLayout.addWidget(self.lcdLongMinutes, 2, 3)
        self.centerGridLayout.addWidget(labelMinutes, 2, 4)
        self.centerGridLayout.addWidget(self.lcdLongSeconds, 2, 5)
        self.centerGridLayout.addWidget(labelSeconds, 2, 6)

        self.setLayout(self.centerGridLayout)

    def setLatitude(self, point, format = 'Format DMS'):
        if format == 'Format DMS':
            point = point[0].split(" ")

            self.lcdLatGrad.display(point[0])
            self.lcdLatMinutes.display(point[1])
            self.lcdLatSeconds.display(point[2][0:5])
        else:
            self.lcdLongGrad.display(point[0])

    def setLongitude(self, point, format = 'Format DMS'):
        if format == 'Format DMS':
            point = point[1].split(" ")

            self.lcdLongGrad.display(point[1])
            self.lcdLongMinutes.display(point[2])
            self.lcdLongSeconds.display(point[3][0:5])
        else:
            self.lcdLongGrad.display(point[1])

    def clearLCD(self):
        self.lcdLatGrad.display(0)
        self.lcdLatMinutes.display(0)
        self.lcdLatSeconds.display(0)

        self.lcdLongGrad.display(0)
        self.lcdLongMinutes.display(0)
        self.lcdLongSeconds.display(0)

    def serFormat(self, format = "Format DD"):
        if format == "Format DD":
            self.labelFormat.setText("Format DD:")
            self.lcdLatMinutes.setEnabled(False)
            self.lcdLatSeconds.setEnabled(False)
            self.lcdLongMinutes.setEnabled(False)
            self.lcdLongSeconds.setEnabled(False)

        else:
            self.labelFormat.setText("Format DMS:")
            self.lcdLatMinutes.setEnabled(True)
            self.lcdLatSeconds.setEnabled(True)
            self.lcdLongMinutes.setEnabled(True)
            self.lcdLongSeconds.setEnabled(True)



class ButtomGroupBox(QGroupBox):

    def __init__(self, parent):
        super(ButtomGroupBox, self).__init__(parent)

        self.setTitle("Controls:")
        controlBtnLayout = QHBoxLayout()

        self.updateBtn = QPushButton("Update")
        controlBtnLayout.addWidget(self.updateBtn)

        self.clearBtn = QPushButton("Clear")
        controlBtnLayout.addWidget(self.clearBtn)

        self.exitBtn = QPushButton("Exit")
        self.exitBtn.clicked.connect(lambda: self.onExitButtonClicked())
        controlBtnLayout.addWidget(self.exitBtn)

        self.radioButtonDMS = QRadioButton("Format DMS")
        self.radioButtonDMS.country = "Format DMS"

        self.radioButtonDMS.flag = True
        self.radioButtonDMS.toggled.connect(self.onClicked)
        self.radioButtonDMS.setChecked(self.radioButtonDMS.flag)

        controlBtnLayout.addWidget(self.radioButtonDMS)
        controlBtnLayout.addWidget(self.radioButtonDMS)

        self.radioButtonDD = QRadioButton("Format DD")
        self.radioButtonDD.country = "Format DD"
        self.radioButtonDD.flag = False
        self.radioButtonDD.toggled.connect(self.onClicked)

        controlBtnLayout.addWidget(self.radioButtonDD)

        controlBtnLayout.addStretch(1)
        self.setLayout(controlBtnLayout)

    def onClicked(self):
        radioButton = self.sender()
        # self.labelLatitude.setEnabled(radioButton.flag)
        # self.lcdGrad.setEnabled(radioButton.flag)
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))
            # self.labelFormat.setText(radioButton.country)
            # self.labelLatitude.setDisabled(radioButton.flag)
            # self.lcdGrad.setDisabled(radioButton.flag)

    def updateLayout(self):
        self.centerGridLayout.setEnabled(False)

    def onExitButtonClicked(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Application quit")
        msgBox.setText("Would you like to quit?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            app.exit()

