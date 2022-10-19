

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

class Ui_Calk(object):
    def setupUi(self, Calk):
        if Calk.objectName():
            Calk.setObjectName(u"Calk")
        Calk.resize(250, 395)
        self.pushButton_1 = QPushButton(Calk)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(10, 70, 51, 51))
        self.pushButton_1.setFlat(False)
        self.pushButton_2 = QPushButton(Calk)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 70, 51, 51))
        self.pushButton_3 = QPushButton(Calk)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(130, 70, 51, 51))
        self.pushButton_4 = QPushButton(Calk)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 130, 51, 51))
        self.pushButton_5 = QPushButton(Calk)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(70, 130, 51, 51))
        self.pushButton_6 = QPushButton(Calk)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(130, 130, 51, 51))
        self.pushButton_7 = QPushButton(Calk)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 190, 51, 51))
        self.pushButton_8 = QPushButton(Calk)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(70, 190, 51, 51))
        self.pushButton_9 = QPushButton(Calk)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(130, 190, 51, 51))
        self.pushButton_CLR = QPushButton(Calk)
        self.pushButton_CLR.setObjectName(u"pushButton_CLR")
        self.pushButton_CLR.setGeometry(QRect(10, 250, 51, 51))
        self.pushButton_0 = QPushButton(Calk)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setGeometry(QRect(70, 250, 51, 51))
        self.pushButton_ENT = QPushButton(Calk)
        self.pushButton_ENT.setObjectName(u"pushButton_ENT")
        self.pushButton_ENT.setGeometry(QRect(130, 250, 51, 51))
        self.pushButton_mult = QPushButton(Calk)
        self.pushButton_mult.setObjectName(u"pushButton_mult")
        self.pushButton_mult.setGeometry(QRect(190, 190, 51, 51))
        self.pushButton_div = QPushButton(Calk)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.pushButton_div.setGeometry(QRect(190, 250, 51, 51))
        self.pushButton_sub = QPushButton(Calk)
        self.pushButton_sub.setObjectName(u"pushButton_sub")
        self.pushButton_sub.setGeometry(QRect(190, 130, 51, 51))
        self.pushButton_add = QPushButton(Calk)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setGeometry(QRect(190, 70, 51, 51))
        self.line = QFrame(Calk)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 320, 241, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(Calk)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 350, 171, 20))


        self.lineEdit = QLineEdit(Calk)
        self.lineEdit.setReadOnly(1)



        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 231, 41))

        self.retranslateUi(Calk)

        QMetaObject.connectSlotsByName(Calk)
    # setupUi

    def retranslateUi(self, Calk):
        Calk.setWindowTitle(QCoreApplication.translate("Calk", u"Bills Calculator", None))
        self.pushButton_1.setText(QCoreApplication.translate("Calk", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calk", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calk", u"3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calk", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Calk", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calk", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Calk", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calk", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Calk", u"9", None))
        self.pushButton_CLR.setText(QCoreApplication.translate("Calk", u"CLR", None))
        self.pushButton_0.setText(QCoreApplication.translate("Calk", u"0", None))
        self.pushButton_ENT.setText(QCoreApplication.translate("Calk", u"ENT", None))
        self.pushButton_mult.setText(QCoreApplication.translate("Calk", u"x", None))
        self.pushButton_div.setText(QCoreApplication.translate("Calk", u"/", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Calk", u"-", None))
        self.pushButton_add.setText(QCoreApplication.translate("Calk", u"+", None))
        self.label.setText(QCoreApplication.translate("Calk", u"Copyrite 1982 Billy Gates ltd", None))
    # retranslateUi

