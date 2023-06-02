# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'button.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QMetaObject, QCoreApplication, QRect

from PySide2.QtWidgets import QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(904, 659)
        self.SEND = QPushButton(Form)
        self.SEND.setObjectName(u"SEND")
        self.SEND.setGeometry(QRect(240, 160, 89, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.SEND.setText(QCoreApplication.translate("Form", u"SEND", None))
    # retranslateUi
