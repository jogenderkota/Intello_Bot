import sys
import time
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot
from __main__ import window
import threading
from PyQt4.QtCore import QThread
from random import randint


class RandomWalk(threading.Thread):
    """Thread that executes a task every N seconds"""

    def __init__(self):
        threading.Thread.__init__(self)
        self._finished = threading.Event()
        self._interval = 5.0

    def setInterval(self, interval):
        """Set the number of seconds we sleep between executing our task"""
        self._interval = interval

    def shutdown(self):
        """Stop this thread"""
        self._finished.set()

    def run(self):
        while 1:
            if self._finished.isSet(): return
            self.task()

            # sleep for interval or until shutdown
            self._finished.wait(self._interval)

    def task(self):
        lr=randint(0,8)
        rr=randint(0,8)
        bot_count=int(window.lineEdit_3.text())
        cr=randint(0,bot_count-1)
        window.comboBox.setCurrentIndex(cr)
        window.lineEdit.setText(str(lr-4))
        window.lineEdit_2.setText(str(rr-4))
        print(bot_count)
        pass



RandomWalk().start()
