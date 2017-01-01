#-*- coding: UTF-8 -*-
__author__ = 'AllenG_G'

import time,sys
from PySide import QtGui
from PySide import QtCore

class MainUI(QtGui.QDialog):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setWindowTitle('BoringGame')

        self.mainLayout = QtGui.QVBoxLayout(self)

        self.propertyLayout = QtGui.QVBoxLayout()

        self.propertyLine1 = QtGui.QHBoxLayout()
        self.label_name = QtGui.QLabel(u'名字')
        self.parameter_name = QtGui.QLabel('X')
        self.propertyLine1.addWidget(self.label_name)
        self.propertyLine1.addWidget(self.parameter_name)
        self.propertyLayout.addLayout(self.propertyLine1)

        self.propertyLine2 = QtGui.QHBoxLayout()
        self.label_age = QtGui.QLabel(u'年龄')
        self.parameter_age = QtGui.QLabel('10')
        self.propertyLine2.addWidget(self.label_age)
        self.propertyLine2.addWidget(self.parameter_age)
        self.propertyLayout.addLayout(self.propertyLine2)

        self.propertyLine3 = QtCore.QHBoxLayout()
        self.label_level = QtCore.QLabel()
        self.parameter_level = QtCore.QLabel()

        self.mainLayout.addLayout(self.propertyLayout)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainApp = MainUI()
    MainApp.show()
    sys.exit(app.exec_())
