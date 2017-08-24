# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:44:40 2017

@author: til-05
"""

import sys
import vrep
import time
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Textbox example @pythonspot.com')
 
# Set window size.
w.resize(320, 150)

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(280,40)
 

 
# Create a button in the window
button = QPushButton('Click me', w)
button.move(20,80)
 
# Create the actions
@pyqtSlot()
def on_click():
    textbox.setText("Button clicked.")
 
# connect the signals to the slots
button.clicked.connect(on_click)
 
 
 
 
 
 
 
 
# V-Rep start Subroutine
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Could not connect')
    sys.exit('Could not Connect')

left_joint_name='Pioneer_p3dx_leftMotor#'
right_joint_name='Pioneer_p3dx_rightMotor#'

left_motor_handle_list=[]
right_motor_handle_list=[]    
left_motor_name_list=[]
right_motor_name_list=[]  

num_of_bots=int(input("Number of Bots:"))
num_of_bots=num_of_bots+1


for x in range(0,num_of_bots):
    errorCode,left_motor_handle=vrep.simxGetObjectHandle(clientID,left_joint_name+str(x),vrep.simx_opmode_blocking) 
    errorCode,right_motor_handle=vrep.simxGetObjectHandle(clientID,right_joint_name+str(x),vrep.simx_opmode_blocking) 
    left_motor_handle_list.append(left_motor_handle)
    right_motor_handle_list.append(right_motor_handle)

for x in range(0,num_of_bots):
    errorCode=vrep.simxSetJointTargetVelocity(clientID,left_motor_handle_list[x],0.2,vrep.simx_opmode_streaming)
    errorCode=vrep.simxSetJointTargetVelocity(clientID,right_motor_handle_list[x],0.2,vrep.simx_opmode_streaming)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
# Show the window and run the app
w.show()
app.exec_()


