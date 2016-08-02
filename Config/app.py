"""
File: app.py
Author: Zachary King

Demonstrates the use of configparser with the 
settings.config file found in this directory.
"""

import configparser 
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

config = configparser.ConfigParser()
config.read('settings.config')

app = QApplication(sys.argv)

color = config['DEFAULT']['FontColor']
size = config['DEFAULT']['FontSize']
msg = config['DEFAULT']['Message']
splash = config.getboolean('DEFAULT', 'SplashScreen')

label = QLabel('<font color={0} size={1}>{2}</font>'.format(color, size, msg))
if splash:
    label.setWindowFlags(Qt.SplashScreen)
label.show()



QTimer.singleShot(5000, app.quit) # 5 seconds 
app.exec_()