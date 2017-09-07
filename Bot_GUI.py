# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:47:05 2017

@author: til-05
"""
import vrep
import sys
import time
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot


vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Could not connect')
    sys.exit('Could not Connect')
list1=[]
leftmotor=[]
rightmotor=[]
left_motor_handle=[]
right_motor_handle=[]
sp2=0
global botname_l
global botname_r
botname_l='Pioneer_p3dx_leftMotor#'
botname_r='Pioneer_p3dx_rightMotor#'
global bot_num
bot_num=0
global bot_count
bot_count=3
global scale
scale=2


for x in range(0,bot_count):
    leftmotor.append(botname_l+str(x))
    rightmotor.append(botname_r+str(x))
for x in range(0,bot_count):
    errorCode,leftmotorhandle=vrep.simxGetObjectHandle(clientID,leftmotor[x],vrep.simx_opmode_blocking)
    errorCode,rightmotorhandle=vrep.simxGetObjectHandle(clientID,rightmotor[x],vrep.simx_opmode_blocking)
    left_motor_handle.append(leftmotorhandle)


qtCreatorFile = "multi_bot.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ShowText)
        self.horizontalSlider.valueChanged.connect(self.ShowText2)
        self.horizontalSlider_2.valueChanged.connect(self.ShowText3)
        self.comboBox.currentIndexChanged.connect(self.Select)
        self.lineEdit.textChanged.connect(self.TxtChange1)
        self.lineEdit_2.textChanged.connect(self.TxtChange2)
        self.lineEdit_3.setText(str(bot_count))
        for x in range(0,bot_count):
            self.comboBox.addItem(str(x+1))

#    def globe(self):
#        sp2=0

    def ShowText(self):
        self.lineEdit_3.setText(str(bot_count))
    def ShowText2(self):
        sp=self.horizontalSlider.value()/scale
        vrep.simxSetJointTargetVelocity(clientID,left_motor_handle[bot_num],sp,vrep.simx_opmode_streaming)
        self.lineEdit.setText(str(sp))
        # print('sp=',sp)
        # print('sp2=',bot_num)
    def ShowText3(self):
        sp1=self.horizontalSlider_2.value()/scale
        vrep.simxSetJointTargetVelocity(clientID,right_motor_handle[bot_num],sp1,vrep.simx_opmode_streaming)
        # print('sp1=',sp1)
        # print('sp2=',bot_num)
        self.lineEdit_2.setText(str(sp1))
    def Select(self):
        global bot_num
        bot_num = self.comboBox.currentIndex()
    def TxtChange1(self):
        text_temp=int(self.lineEdit.text())
        self.horizontalSlider.setValue(text_temp)
    def TxtChange2(self):
        text_temp2=int(self.lineEdit_2.text())
        self.horizontalSlider_2.setValue(text_temp2)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    import algorithm
    sys.exit(app.exec_())
