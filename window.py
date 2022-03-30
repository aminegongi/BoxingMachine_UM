# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
import serial
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import random
raw = serial.Serial(port='COM11', baudrate=9600, timeout=.1)
start = 0
stop = 0
values= [0]

def readSerial():
    cc=str(raw.readline())
    return cc[2:][:-5]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.setStyleSheet("background-color: black;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(10, 10))
        self.label.setObjectName("label")
        self.label.setFont(QFont('Arial', 500))
        self.label.setStyleSheet("QLabel{color:white;}")
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(0)
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.value = 0
        self.retranslateUi(MainWindow)
        self.maxValue = 0
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start = 0
        self.stop = 0
        self.values = []
        self.timerValue = 0
        self.maxRender = 999
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
      
    def readMaxValue(self):
            value_serial = readSerial()
            if(value_serial != ''):
                v = abs(float(value_serial))
                print(v)
                if (v < 5):
                    try:
                        val = max(self.values)
                        #print("{} max".format(val))
                        self.values = []
                        self.start = 1
                        raw.write(b'x') # isaker le capteur
                        self.maxValue = val
                        if self.maxValue >= self.maxRender:
                            self.maxValue = self.maxRender - random.randint(20, 100)
                        return val
                    except:
                        pass
                if (v > 5):
                    self.stop = 0
                    self.value=0
                    self.values.append(math.trunc(v*10))
                    return 0
            return 0


    def handleTimer(self):
        val = 0
        if self.start == 0:
            val = self.readMaxValue()
            #print(val)
        elif self.start ==1:
            if self.value < self.maxValue:
                #print(self.maxValue)
                self.start = 1
                #time.sleep(0.1)
                self.value += 1
                #print(self.value)
                self.label.setText(str(self.value))
                if self.value> self.maxValue*0.9:
                    time.sleep(self.timerValue)
                    self.timerValue += 0.0005
                    time.sleep(self.timerValue)
                    #self.label.setStyleSheet("QLabel{color:red;}")
            elif self.value == self.maxValue:
                if self.value > 900:
                    print("You Win")
                raw.write(b'c') # i7el le capteur
                self.value = 0
                self.maxValue = 0
                self.start = 0
                self.timerValue = 0
            

