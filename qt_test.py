# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:32:00 2017

@author: til-05
"""

import sys
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
 
# Show the window and run the app
w.show()
app.exec_()
