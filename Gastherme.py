from PyQt6.QtWidgets import QWidget, QDial
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6 import uic
#from HeatControlWidget import HeatControlWidget


class Gastherme(QWidget):
    valueVorlauf = pyqtSlot(int)
    valueRuecklauf = pyqtSlot(int)
    valueWarmwasser = pyqtSlot(int)
    valueFrostschutz = pyqtSlot(int)
    valueRuecklaufChanged = pyqtSignal(int)


    def __init__(self, parent=None):
        super(Gastherme, self).__init__(parent)

        uic.loadUi("Gastherme.ui", self)

        self.__maxtemp = 0
        self.__QDialFrostschutz = self.findChild(QDial, "QDialFrostschutz")
        self.__QDialRuecklauf = self.findChild(QDial, "QDialRuecklauf")
        self.__QDialVorlauf = self.findChild(QDial, "QDialVorlauf")
        self.__QDialWarmwasser = self.findChild(QDial, "QDialWarmwasser")

        #self.__QDialVorlauf.valueChanged.connect(self.valueVorlauf)
        self.__QDialRuecklauf.valueChanged.connect(self.valueRuecklauf)
        #self.__QDialWarmwasser.valueChanged.connect(self.valueWarmwasser)
        #self.__QDialFrostschutz.valueChanged.connect(self.valueFrostschutz)
        self.__QDialWarmwasser.setValue(50)
        self.valueRuecklaufChanged.connect(self.valueVorlauf)
        self.__QDialRuecklauf.setDisabled(True)
        self.__QDialVorlauf.setDisabled(True)
        #self.valueRuecklaufChanged.connect(self.changeRuecklauf)

    def valueVorlauf(self, wert):
        self.__maxtemp = wert + 10
        self.__QDialVorlauf.setValue(self.__maxtemp)
        #self.__QDialVorlauf.setMinimum(self.__maxtemp)

    def valueRuecklauf(self, wert):
        self.valueRuecklaufChanged.emit(wert)
        self.__maxtemp = wert

    def changeRuecklauf(self,wert):
        self.__QDialRuecklauf.setValue(wert)


