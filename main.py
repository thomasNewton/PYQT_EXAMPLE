from PySide6.QtCore import *
from PySide6.QtWidgets import *
from Ui_Form import *
from PySide6.QtGui import *
from PySide6 import QtWidgets
import sys
import Ui_Form


def link_it():
    uiform.pushButton_1.clicked.connect(b1_clicked)
    uiform.pushButton_2.clicked.connect(b2_clicked)
    uiform.pushButton_3.clicked.connect(b3_clicked)
    uiform.pushButton_4.clicked.connect(b4_clicked)
    uiform.pushButton_5.clicked.connect(b5_clicked)
    uiform.pushButton_6.clicked.connect(b6_clicked)
    uiform.pushButton_7.clicked.connect(b7_clicked)
    uiform.pushButton_8.clicked.connect(b8_clicked)
    uiform.pushButton_9.clicked.connect(b9_clicked)
    uiform.pushButton_0.clicked.connect(b0_clicked)
    uiform.pushButton_add.clicked.connect(badd_clicked)
    uiform.pushButton_sub.clicked.connect(bsub_clicked)
    uiform.pushButton_mult.clicked.connect(bmult_clicked)
    uiform.pushButton_div.clicked.connect(bdiv_clicked)
    uiform.pushButton_CLR.clicked.connect(bCLR_clicked)
    uiform.pushButton_ENT.clicked.connect(bENT_clicked)


def b1_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "1")


def b2_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "2")


def b3_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "3")


def b4_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "4")


def b5_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "5")


def b6_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "6")


def b7_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "7")


def b8_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "8")


def b9_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "9")


def b0_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + "0")


def bCLR_clicked(): uiform.lineEdit.clear()


def badd_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + " + ")


def bsub_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + " - ")


def bmult_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + " * ")


def bdiv_clicked(): uiform.lineEdit.setText(uiform.lineEdit.text() + " / ")


def bENT_clicked():
    print( uiform.lineEdit.text()  )
    uiform.lineEdit.clear()

print(int("10"+ "10"))
app = QApplication([])
uiform = Ui_Calk()
window = QWidget()
window.setGeometry(QRect(200, 100, 800, 800))
uiform.setupUi(window)
uiform.retranslateUi(window)
link_it()
window.show()
sys.exit(app.exec())
