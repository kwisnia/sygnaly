# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 1020)
        self.actiondystans = QAction(MainWindow)
        self.actiondystans.setObjectName(u"actiondystans")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.generujFrame = QFrame(self.centralwidget)
        self.generujFrame.setObjectName(u"generujFrame")
        self.generujFrame.setGeometry(QRect(5, 5, 371, 431))
        self.generujFrame.setFrameShape(QFrame.Panel)
        self.generujFrame.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget = QWidget(self.generujFrame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 331, 24))
        self.typSygnalLayout = QFormLayout(self.formLayoutWidget)
        self.typSygnalLayout.setObjectName(u"typSygnalLayout")
        self.typSygnalLayout.setVerticalSpacing(20)
        self.typSygnalLayout.setContentsMargins(0, 0, 0, 0)
        self.typSygnaluLabel = QLabel(self.formLayoutWidget)
        self.typSygnaluLabel.setObjectName(u"typSygnaluLabel")

        self.typSygnalLayout.setWidget(0, QFormLayout.LabelRole, self.typSygnaluLabel)

        self.typSygnaluComboBox = QComboBox(self.formLayoutWidget)
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.addItem("")
        self.typSygnaluComboBox.setObjectName(u"typSygnaluComboBox")

        self.typSygnalLayout.setWidget(0, QFormLayout.FieldRole, self.typSygnaluComboBox)

        self.horizontalLayoutWidget = QWidget(self.generujFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 299, 351, 51))
        self.generujLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.generujLayout.setObjectName(u"generujLayout")
        self.generujLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generujLayout.addItem(self.horizontalSpacer_2)

        self.generujLewy = QPushButton(self.horizontalLayoutWidget)
        self.generujLewy.setObjectName(u"generujLewy")

        self.generujLayout.addWidget(self.generujLewy)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generujLayout.addItem(self.horizontalSpacer)

        self.generujPrawy = QPushButton(self.horizontalLayoutWidget)
        self.generujPrawy.setObjectName(u"generujPrawy")

        self.generujLayout.addWidget(self.generujPrawy)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.generujLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayoutWidget_2 = QWidget(self.generujFrame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 349, 351, 31))
        self.zapiszLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.zapiszLayout.setObjectName(u"zapiszLayout")
        self.zapiszLayout.setContentsMargins(0, 0, 0, 0)
        self.zapiszDoPlikuComboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.zapiszDoPlikuComboBox.addItem("")
        self.zapiszDoPlikuComboBox.addItem("")
        self.zapiszDoPlikuComboBox.addItem("")
        self.zapiszDoPlikuComboBox.setObjectName(u"zapiszDoPlikuComboBox")

        self.zapiszLayout.addWidget(self.zapiszDoPlikuComboBox)

        self.zapiszButton = QPushButton(self.horizontalLayoutWidget_2)
        self.zapiszButton.setObjectName(u"zapiszButton")

        self.zapiszLayout.addWidget(self.zapiszButton)

        self.horizontalLayoutWidget_3 = QWidget(self.generujFrame)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(9, 379, 351, 41))
        self.wczytajLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.wczytajLayout.setObjectName(u"wczytajLayout")
        self.wczytajLayout.setContentsMargins(0, 0, 0, 0)
        self.wczytajZPlikuComboBox = QComboBox(self.horizontalLayoutWidget_3)
        self.wczytajZPlikuComboBox.addItem("")
        self.wczytajZPlikuComboBox.addItem("")
        self.wczytajZPlikuComboBox.addItem("")
        self.wczytajZPlikuComboBox.setObjectName(u"wczytajZPlikuComboBox")

        self.wczytajLayout.addWidget(self.wczytajZPlikuComboBox)

        self.wczytajButton = QPushButton(self.horizontalLayoutWidget_3)
        self.wczytajButton.setObjectName(u"wczytajButton")

        self.wczytajLayout.addWidget(self.wczytajButton)

        self.generujStackedWidget = QStackedWidget(self.generujFrame)
        self.generujStackedWidget.setObjectName(u"generujStackedWidget")
        self.generujStackedWidget.setGeometry(QRect(20, 50, 331, 241))
        self.szumGaussowski = QWidget()
        self.szumGaussowski.setObjectName(u"szumGaussowski")
        self.formLayoutWidget_5 = QWidget(self.szumGaussowski)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(0, 20, 331, 221))
        self.szumGaussowskiLayout = QFormLayout(self.formLayoutWidget_5)
        self.szumGaussowskiLayout.setObjectName(u"szumGaussowskiLayout")
        self.szumGaussowskiLayout.setVerticalSpacing(12)
        self.szumGaussowskiLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_1 = QLabel(self.formLayoutWidget_5)
        self.poczatekSygnaluLabel_1.setObjectName(u"poczatekSygnaluLabel_1")

        self.szumGaussowskiLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_1)

        self.poczatekSygnaluDoubleSpinBox_1 = QDoubleSpinBox(self.formLayoutWidget_5)
        self.poczatekSygnaluDoubleSpinBox_1.setObjectName(u"poczatekSygnaluDoubleSpinBox_1")
        self.poczatekSygnaluDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.szumGaussowskiLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_1)

        self.dlugoscSygnaluLabel_1 = QLabel(self.formLayoutWidget_5)
        self.dlugoscSygnaluLabel_1.setObjectName(u"dlugoscSygnaluLabel_1")

        self.szumGaussowskiLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_1)

        self.dlugoscSygnaluDoubleSpinBox_1 = QDoubleSpinBox(self.formLayoutWidget_5)
        self.dlugoscSygnaluDoubleSpinBox_1.setObjectName(u"dlugoscSygnaluDoubleSpinBox_1")
        self.dlugoscSygnaluDoubleSpinBox_1.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_1.setValue(10.000000000000000)

        self.szumGaussowskiLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_1)

        self.generujStackedWidget.addWidget(self.szumGaussowski)
        self.szumJednostajny = QWidget()
        self.szumJednostajny.setObjectName(u"szumJednostajny")
        self.formLayoutWidget_4 = QWidget(self.szumJednostajny)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(0, 20, 331, 221))
        self.szumJednostajnyLayout = QFormLayout(self.formLayoutWidget_4)
        self.szumJednostajnyLayout.setObjectName(u"szumJednostajnyLayout")
        self.szumJednostajnyLayout.setVerticalSpacing(12)
        self.szumJednostajnyLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_2 = QLabel(self.formLayoutWidget_4)
        self.poczatekSygnaluLabel_2.setObjectName(u"poczatekSygnaluLabel_2")

        self.szumJednostajnyLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_2)

        self.poczatekSygnaluDoubleSpinBox_2 = QDoubleSpinBox(self.formLayoutWidget_4)
        self.poczatekSygnaluDoubleSpinBox_2.setObjectName(u"poczatekSygnaluDoubleSpinBox_2")
        self.poczatekSygnaluDoubleSpinBox_2.setMaximum(100000.000000000000000)

        self.szumJednostajnyLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_2)

        self.dlugoscSygnaluLabel_2 = QLabel(self.formLayoutWidget_4)
        self.dlugoscSygnaluLabel_2.setObjectName(u"dlugoscSygnaluLabel_2")

        self.szumJednostajnyLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_2)

        self.dlugoscSygnaluDoubleSpinBox_2 = QDoubleSpinBox(self.formLayoutWidget_4)
        self.dlugoscSygnaluDoubleSpinBox_2.setObjectName(u"dlugoscSygnaluDoubleSpinBox_2")
        self.dlugoscSygnaluDoubleSpinBox_2.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_2.setValue(10.000000000000000)

        self.szumJednostajnyLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_2)

        self.amplitudaLabel_2 = QLabel(self.formLayoutWidget_4)
        self.amplitudaLabel_2.setObjectName(u"amplitudaLabel_2")

        self.szumJednostajnyLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_2)

        self.amplitudaDoubleSpinBox_2 = QDoubleSpinBox(self.formLayoutWidget_4)
        self.amplitudaDoubleSpinBox_2.setObjectName(u"amplitudaDoubleSpinBox_2")
        self.amplitudaDoubleSpinBox_2.setMaximum(100000.000000000000000)

        self.szumJednostajnyLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_2)

        self.generujStackedWidget.addWidget(self.szumJednostajny)
        self.sinus = QWidget()
        self.sinus.setObjectName(u"sinus")
        self.formLayoutWidget_6 = QWidget(self.sinus)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(0, 20, 331, 221))
        self.sinusLayout = QFormLayout(self.formLayoutWidget_6)
        self.sinusLayout.setObjectName(u"sinusLayout")
        self.sinusLayout.setVerticalSpacing(12)
        self.sinusLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_3 = QLabel(self.formLayoutWidget_6)
        self.poczatekSygnaluLabel_3.setObjectName(u"poczatekSygnaluLabel_3")

        self.sinusLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_3)

        self.poczatekSygnaluDoubleSpinBox_3 = QDoubleSpinBox(self.formLayoutWidget_6)
        self.poczatekSygnaluDoubleSpinBox_3.setObjectName(u"poczatekSygnaluDoubleSpinBox_3")
        self.poczatekSygnaluDoubleSpinBox_3.setMaximum(100000.000000000000000)

        self.sinusLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_3)

        self.dlugoscSygnaluLabel_3 = QLabel(self.formLayoutWidget_6)
        self.dlugoscSygnaluLabel_3.setObjectName(u"dlugoscSygnaluLabel_3")

        self.sinusLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_3)

        self.dlugoscSygnaluDoubleSpinBox_3 = QDoubleSpinBox(self.formLayoutWidget_6)
        self.dlugoscSygnaluDoubleSpinBox_3.setObjectName(u"dlugoscSygnaluDoubleSpinBox_3")
        self.dlugoscSygnaluDoubleSpinBox_3.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_3.setValue(10.000000000000000)

        self.sinusLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_3)

        self.amplitudaLabel_3 = QLabel(self.formLayoutWidget_6)
        self.amplitudaLabel_3.setObjectName(u"amplitudaLabel_3")

        self.sinusLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_3)

        self.amplitudaDoubleSpinBox_3 = QDoubleSpinBox(self.formLayoutWidget_6)
        self.amplitudaDoubleSpinBox_3.setObjectName(u"amplitudaDoubleSpinBox_3")
        self.amplitudaDoubleSpinBox_3.setMaximum(100000.000000000000000)

        self.sinusLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_3)

        self.czestotliwoscLabel_3 = QLabel(self.formLayoutWidget_6)
        self.czestotliwoscLabel_3.setObjectName(u"czestotliwoscLabel_3")

        self.sinusLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_3)

        self.czestotliwoscDoubleSpinBox_3 = QDoubleSpinBox(self.formLayoutWidget_6)
        self.czestotliwoscDoubleSpinBox_3.setObjectName(u"czestotliwoscDoubleSpinBox_3")
        self.czestotliwoscDoubleSpinBox_3.setMaximum(100000.000000000000000)

        self.sinusLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_3)

        self.generujStackedWidget.addWidget(self.sinus)
        self.sinusJedno = QWidget()
        self.sinusJedno.setObjectName(u"sinusJedno")
        self.formLayoutWidget_7 = QWidget(self.sinusJedno)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(0, 20, 331, 221))
        self.sinusJednoLayout = QFormLayout(self.formLayoutWidget_7)
        self.sinusJednoLayout.setObjectName(u"sinusJednoLayout")
        self.sinusJednoLayout.setVerticalSpacing(12)
        self.sinusJednoLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_4 = QLabel(self.formLayoutWidget_7)
        self.poczatekSygnaluLabel_4.setObjectName(u"poczatekSygnaluLabel_4")

        self.sinusJednoLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_4)

        self.poczatekSygnaluDoubleSpinBox_4 = QDoubleSpinBox(self.formLayoutWidget_7)
        self.poczatekSygnaluDoubleSpinBox_4.setObjectName(u"poczatekSygnaluDoubleSpinBox_4")
        self.poczatekSygnaluDoubleSpinBox_4.setMaximum(100000.000000000000000)

        self.sinusJednoLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_4)

        self.dlugoscSygnaluLabel_4 = QLabel(self.formLayoutWidget_7)
        self.dlugoscSygnaluLabel_4.setObjectName(u"dlugoscSygnaluLabel_4")

        self.sinusJednoLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_4)

        self.dlugoscSygnaluDoubleSpinBox_4 = QDoubleSpinBox(self.formLayoutWidget_7)
        self.dlugoscSygnaluDoubleSpinBox_4.setObjectName(u"dlugoscSygnaluDoubleSpinBox_4")
        self.dlugoscSygnaluDoubleSpinBox_4.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_4.setValue(10.000000000000000)

        self.sinusJednoLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_4)

        self.amplitudaLabel_4 = QLabel(self.formLayoutWidget_7)
        self.amplitudaLabel_4.setObjectName(u"amplitudaLabel_4")

        self.sinusJednoLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_4)

        self.amplitudaDoubleSpinBox_4 = QDoubleSpinBox(self.formLayoutWidget_7)
        self.amplitudaDoubleSpinBox_4.setObjectName(u"amplitudaDoubleSpinBox_4")
        self.amplitudaDoubleSpinBox_4.setMaximum(100000.000000000000000)

        self.sinusJednoLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_4)

        self.czestotliwoscLabel_4 = QLabel(self.formLayoutWidget_7)
        self.czestotliwoscLabel_4.setObjectName(u"czestotliwoscLabel_4")

        self.sinusJednoLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_4)

        self.czestotliwoscDoubleSpinBox_4 = QDoubleSpinBox(self.formLayoutWidget_7)
        self.czestotliwoscDoubleSpinBox_4.setObjectName(u"czestotliwoscDoubleSpinBox_4")
        self.czestotliwoscDoubleSpinBox_4.setMaximum(100000.000000000000000)

        self.sinusJednoLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_4)

        self.generujStackedWidget.addWidget(self.sinusJedno)
        self.sinusDwu = QWidget()
        self.sinusDwu.setObjectName(u"sinusDwu")
        self.formLayoutWidget_8 = QWidget(self.sinusDwu)
        self.formLayoutWidget_8.setObjectName(u"formLayoutWidget_8")
        self.formLayoutWidget_8.setGeometry(QRect(0, 20, 331, 221))
        self.sinusDwuLayout = QFormLayout(self.formLayoutWidget_8)
        self.sinusDwuLayout.setObjectName(u"sinusDwuLayout")
        self.sinusDwuLayout.setVerticalSpacing(12)
        self.sinusDwuLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_5 = QLabel(self.formLayoutWidget_8)
        self.poczatekSygnaluLabel_5.setObjectName(u"poczatekSygnaluLabel_5")

        self.sinusDwuLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_5)

        self.poczatekSygnaluDoubleSpinBox_5 = QDoubleSpinBox(self.formLayoutWidget_8)
        self.poczatekSygnaluDoubleSpinBox_5.setObjectName(u"poczatekSygnaluDoubleSpinBox_5")
        self.poczatekSygnaluDoubleSpinBox_5.setMaximum(100000.000000000000000)

        self.sinusDwuLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_5)

        self.dlugoscSygnaluLabel_5 = QLabel(self.formLayoutWidget_8)
        self.dlugoscSygnaluLabel_5.setObjectName(u"dlugoscSygnaluLabel_5")

        self.sinusDwuLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_5)

        self.dlugoscSygnaluDoubleSpinBox_5 = QDoubleSpinBox(self.formLayoutWidget_8)
        self.dlugoscSygnaluDoubleSpinBox_5.setObjectName(u"dlugoscSygnaluDoubleSpinBox_5")
        self.dlugoscSygnaluDoubleSpinBox_5.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_5.setValue(10.000000000000000)

        self.sinusDwuLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_5)

        self.amplitudaLabel_5 = QLabel(self.formLayoutWidget_8)
        self.amplitudaLabel_5.setObjectName(u"amplitudaLabel_5")

        self.sinusDwuLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_5)

        self.amplitudaDoubleSpinBox_5 = QDoubleSpinBox(self.formLayoutWidget_8)
        self.amplitudaDoubleSpinBox_5.setObjectName(u"amplitudaDoubleSpinBox_5")
        self.amplitudaDoubleSpinBox_5.setMaximum(100000.000000000000000)

        self.sinusDwuLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_5)

        self.czestotliwoscLabel_5 = QLabel(self.formLayoutWidget_8)
        self.czestotliwoscLabel_5.setObjectName(u"czestotliwoscLabel_5")

        self.sinusDwuLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_5)

        self.czestotliwoscDoubleSpinBox_5 = QDoubleSpinBox(self.formLayoutWidget_8)
        self.czestotliwoscDoubleSpinBox_5.setObjectName(u"czestotliwoscDoubleSpinBox_5")
        self.czestotliwoscDoubleSpinBox_5.setMaximum(100000.000000000000000)

        self.sinusDwuLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_5)

        self.generujStackedWidget.addWidget(self.sinusDwu)
        self.prostokat = QWidget()
        self.prostokat.setObjectName(u"prostokat")
        self.formLayoutWidget_9 = QWidget(self.prostokat)
        self.formLayoutWidget_9.setObjectName(u"formLayoutWidget_9")
        self.formLayoutWidget_9.setGeometry(QRect(0, 20, 331, 221))
        self.prostokatLayout = QFormLayout(self.formLayoutWidget_9)
        self.prostokatLayout.setObjectName(u"prostokatLayout")
        self.prostokatLayout.setVerticalSpacing(12)
        self.prostokatLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_6 = QLabel(self.formLayoutWidget_9)
        self.poczatekSygnaluLabel_6.setObjectName(u"poczatekSygnaluLabel_6")

        self.prostokatLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_6)

        self.poczatekSygnaluDoubleSpinBox_6 = QDoubleSpinBox(self.formLayoutWidget_9)
        self.poczatekSygnaluDoubleSpinBox_6.setObjectName(u"poczatekSygnaluDoubleSpinBox_6")
        self.poczatekSygnaluDoubleSpinBox_6.setMaximum(100000.000000000000000)

        self.prostokatLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_6)

        self.dlugoscSygnaluLabel_6 = QLabel(self.formLayoutWidget_9)
        self.dlugoscSygnaluLabel_6.setObjectName(u"dlugoscSygnaluLabel_6")

        self.prostokatLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_6)

        self.dlugoscSygnaluDoubleSpinBox_6 = QDoubleSpinBox(self.formLayoutWidget_9)
        self.dlugoscSygnaluDoubleSpinBox_6.setObjectName(u"dlugoscSygnaluDoubleSpinBox_6")
        self.dlugoscSygnaluDoubleSpinBox_6.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_6.setValue(10.000000000000000)

        self.prostokatLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_6)

        self.amplitudaLabel_6 = QLabel(self.formLayoutWidget_9)
        self.amplitudaLabel_6.setObjectName(u"amplitudaLabel_6")

        self.prostokatLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_6)

        self.amplitudaDoubleSpinBox_6 = QDoubleSpinBox(self.formLayoutWidget_9)
        self.amplitudaDoubleSpinBox_6.setObjectName(u"amplitudaDoubleSpinBox_6")
        self.amplitudaDoubleSpinBox_6.setMaximum(100000.000000000000000)

        self.prostokatLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_6)

        self.czestotliwoscLabel_6 = QLabel(self.formLayoutWidget_9)
        self.czestotliwoscLabel_6.setObjectName(u"czestotliwoscLabel_6")

        self.prostokatLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_6)

        self.czestotliwoscDoubleSpinBox_6 = QDoubleSpinBox(self.formLayoutWidget_9)
        self.czestotliwoscDoubleSpinBox_6.setObjectName(u"czestotliwoscDoubleSpinBox_6")
        self.czestotliwoscDoubleSpinBox_6.setMaximum(100000.000000000000000)

        self.prostokatLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_6)

        self.wspolczynnikWypelnieniaLabel_6 = QLabel(self.formLayoutWidget_9)
        self.wspolczynnikWypelnieniaLabel_6.setObjectName(u"wspolczynnikWypelnieniaLabel_6")

        self.prostokatLayout.setWidget(4, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_6)

        self.wspolczynnikWypelnieniaDoubleSpinBox_6 = QDoubleSpinBox(self.formLayoutWidget_9)
        self.wspolczynnikWypelnieniaDoubleSpinBox_6.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_6")
        self.wspolczynnikWypelnieniaDoubleSpinBox_6.setMaximum(100000.000000000000000)

        self.prostokatLayout.setWidget(4, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_6)

        self.generujStackedWidget.addWidget(self.prostokat)
        self.prostokatSymetryczny = QWidget()
        self.prostokatSymetryczny.setObjectName(u"prostokatSymetryczny")
        self.formLayoutWidget_10 = QWidget(self.prostokatSymetryczny)
        self.formLayoutWidget_10.setObjectName(u"formLayoutWidget_10")
        self.formLayoutWidget_10.setGeometry(QRect(0, 20, 331, 221))
        self.prostokatSymetrycznyLayout = QFormLayout(self.formLayoutWidget_10)
        self.prostokatSymetrycznyLayout.setObjectName(u"prostokatSymetrycznyLayout")
        self.prostokatSymetrycznyLayout.setVerticalSpacing(12)
        self.prostokatSymetrycznyLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_7 = QLabel(self.formLayoutWidget_10)
        self.poczatekSygnaluLabel_7.setObjectName(u"poczatekSygnaluLabel_7")

        self.prostokatSymetrycznyLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_7)

        self.poczatekSygnaluDoubleSpinBox_7 = QDoubleSpinBox(self.formLayoutWidget_10)
        self.poczatekSygnaluDoubleSpinBox_7.setObjectName(u"poczatekSygnaluDoubleSpinBox_7")
        self.poczatekSygnaluDoubleSpinBox_7.setMaximum(100000.000000000000000)

        self.prostokatSymetrycznyLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_7)

        self.dlugoscSygnaluLabel_7 = QLabel(self.formLayoutWidget_10)
        self.dlugoscSygnaluLabel_7.setObjectName(u"dlugoscSygnaluLabel_7")

        self.prostokatSymetrycznyLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_7)

        self.dlugoscSygnaluDoubleSpinBox_7 = QDoubleSpinBox(self.formLayoutWidget_10)
        self.dlugoscSygnaluDoubleSpinBox_7.setObjectName(u"dlugoscSygnaluDoubleSpinBox_7")
        self.dlugoscSygnaluDoubleSpinBox_7.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_7.setValue(10.000000000000000)

        self.prostokatSymetrycznyLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_7)

        self.amplitudaLabel_7 = QLabel(self.formLayoutWidget_10)
        self.amplitudaLabel_7.setObjectName(u"amplitudaLabel_7")

        self.prostokatSymetrycznyLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_7)

        self.amplitudaDoubleSpinBox_7 = QDoubleSpinBox(self.formLayoutWidget_10)
        self.amplitudaDoubleSpinBox_7.setObjectName(u"amplitudaDoubleSpinBox_7")
        self.amplitudaDoubleSpinBox_7.setMaximum(100000.000000000000000)

        self.prostokatSymetrycznyLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_7)

        self.czestotliwoscLabel_7 = QLabel(self.formLayoutWidget_10)
        self.czestotliwoscLabel_7.setObjectName(u"czestotliwoscLabel_7")

        self.prostokatSymetrycznyLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_7)

        self.czestotliwoscDoubleSpinBox_7 = QDoubleSpinBox(self.formLayoutWidget_10)
        self.czestotliwoscDoubleSpinBox_7.setObjectName(u"czestotliwoscDoubleSpinBox_7")
        self.czestotliwoscDoubleSpinBox_7.setMaximum(100000.000000000000000)

        self.prostokatSymetrycznyLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_7)

        self.wspolczynnikWypelnieniaLabel_7 = QLabel(self.formLayoutWidget_10)
        self.wspolczynnikWypelnieniaLabel_7.setObjectName(u"wspolczynnikWypelnieniaLabel_7")

        self.prostokatSymetrycznyLayout.setWidget(4, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_7)

        self.wspolczynnikWypelnieniaDoubleSpinBox_7 = QDoubleSpinBox(self.formLayoutWidget_10)
        self.wspolczynnikWypelnieniaDoubleSpinBox_7.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_7")
        self.wspolczynnikWypelnieniaDoubleSpinBox_7.setMaximum(100000.000000000000000)

        self.prostokatSymetrycznyLayout.setWidget(4, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_7)

        self.generujStackedWidget.addWidget(self.prostokatSymetryczny)
        self.trojkat = QWidget()
        self.trojkat.setObjectName(u"trojkat")
        self.formLayoutWidget_11 = QWidget(self.trojkat)
        self.formLayoutWidget_11.setObjectName(u"formLayoutWidget_11")
        self.formLayoutWidget_11.setGeometry(QRect(0, 20, 331, 221))
        self.trojkatLayout = QFormLayout(self.formLayoutWidget_11)
        self.trojkatLayout.setObjectName(u"trojkatLayout")
        self.trojkatLayout.setVerticalSpacing(12)
        self.trojkatLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_8 = QLabel(self.formLayoutWidget_11)
        self.poczatekSygnaluLabel_8.setObjectName(u"poczatekSygnaluLabel_8")

        self.trojkatLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_8)

        self.poczatekSygnaluDoubleSpinBox_8 = QDoubleSpinBox(self.formLayoutWidget_11)
        self.poczatekSygnaluDoubleSpinBox_8.setObjectName(u"poczatekSygnaluDoubleSpinBox_8")
        self.poczatekSygnaluDoubleSpinBox_8.setMaximum(100000.000000000000000)

        self.trojkatLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_8)

        self.dlugoscSygnaluLabel_8 = QLabel(self.formLayoutWidget_11)
        self.dlugoscSygnaluLabel_8.setObjectName(u"dlugoscSygnaluLabel_8")

        self.trojkatLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_8)

        self.dlugoscSygnaluDoubleSpinBox_8 = QDoubleSpinBox(self.formLayoutWidget_11)
        self.dlugoscSygnaluDoubleSpinBox_8.setObjectName(u"dlugoscSygnaluDoubleSpinBox_8")
        self.dlugoscSygnaluDoubleSpinBox_8.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_8.setValue(10.000000000000000)

        self.trojkatLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_8)

        self.amplitudaLabel_8 = QLabel(self.formLayoutWidget_11)
        self.amplitudaLabel_8.setObjectName(u"amplitudaLabel_8")

        self.trojkatLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_8)

        self.amplitudaDoubleSpinBox_8 = QDoubleSpinBox(self.formLayoutWidget_11)
        self.amplitudaDoubleSpinBox_8.setObjectName(u"amplitudaDoubleSpinBox_8")
        self.amplitudaDoubleSpinBox_8.setMaximum(100000.000000000000000)

        self.trojkatLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_8)

        self.czestotliwoscLabel_8 = QLabel(self.formLayoutWidget_11)
        self.czestotliwoscLabel_8.setObjectName(u"czestotliwoscLabel_8")

        self.trojkatLayout.setWidget(3, QFormLayout.LabelRole, self.czestotliwoscLabel_8)

        self.czestotliwoscDoubleSpinBox_8 = QDoubleSpinBox(self.formLayoutWidget_11)
        self.czestotliwoscDoubleSpinBox_8.setObjectName(u"czestotliwoscDoubleSpinBox_8")
        self.czestotliwoscDoubleSpinBox_8.setMaximum(100000.000000000000000)

        self.trojkatLayout.setWidget(3, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_8)

        self.wspolczynnikWypelnieniaLabel_8 = QLabel(self.formLayoutWidget_11)
        self.wspolczynnikWypelnieniaLabel_8.setObjectName(u"wspolczynnikWypelnieniaLabel_8")

        self.trojkatLayout.setWidget(4, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_8)

        self.wspolczynnikWypelnieniaDoubleSpinBox_8 = QDoubleSpinBox(self.formLayoutWidget_11)
        self.wspolczynnikWypelnieniaDoubleSpinBox_8.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_8")
        self.wspolczynnikWypelnieniaDoubleSpinBox_8.setMaximum(100000.000000000000000)

        self.trojkatLayout.setWidget(4, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_8)

        self.generujStackedWidget.addWidget(self.trojkat)
        self.skokJednostkowy = QWidget()
        self.skokJednostkowy.setObjectName(u"skokJednostkowy")
        self.formLayoutWidget_12 = QWidget(self.skokJednostkowy)
        self.formLayoutWidget_12.setObjectName(u"formLayoutWidget_12")
        self.formLayoutWidget_12.setGeometry(QRect(0, 20, 331, 221))
        self.skokJednostkowyLayout = QFormLayout(self.formLayoutWidget_12)
        self.skokJednostkowyLayout.setObjectName(u"skokJednostkowyLayout")
        self.skokJednostkowyLayout.setVerticalSpacing(12)
        self.skokJednostkowyLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_9 = QLabel(self.formLayoutWidget_12)
        self.poczatekSygnaluLabel_9.setObjectName(u"poczatekSygnaluLabel_9")

        self.skokJednostkowyLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_9)

        self.poczatekSygnaluDoubleSpinBox_9 = QDoubleSpinBox(self.formLayoutWidget_12)
        self.poczatekSygnaluDoubleSpinBox_9.setObjectName(u"poczatekSygnaluDoubleSpinBox_9")
        self.poczatekSygnaluDoubleSpinBox_9.setMaximum(100000.000000000000000)

        self.skokJednostkowyLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_9)

        self.dlugoscSygnaluLabel_9 = QLabel(self.formLayoutWidget_12)
        self.dlugoscSygnaluLabel_9.setObjectName(u"dlugoscSygnaluLabel_9")

        self.skokJednostkowyLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_9)

        self.dlugoscSygnaluDoubleSpinBox_9 = QDoubleSpinBox(self.formLayoutWidget_12)
        self.dlugoscSygnaluDoubleSpinBox_9.setObjectName(u"dlugoscSygnaluDoubleSpinBox_9")
        self.dlugoscSygnaluDoubleSpinBox_9.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_9.setValue(10.000000000000000)

        self.skokJednostkowyLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_9)

        self.amplitudaLabel_9 = QLabel(self.formLayoutWidget_12)
        self.amplitudaLabel_9.setObjectName(u"amplitudaLabel_9")

        self.skokJednostkowyLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_9)

        self.amplitudaDoubleSpinBox_9 = QDoubleSpinBox(self.formLayoutWidget_12)
        self.amplitudaDoubleSpinBox_9.setObjectName(u"amplitudaDoubleSpinBox_9")
        self.amplitudaDoubleSpinBox_9.setMaximum(100000.000000000000000)

        self.skokJednostkowyLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_9)

        self.wspolczynnikWypelnieniaLabel_9 = QLabel(self.formLayoutWidget_12)
        self.wspolczynnikWypelnieniaLabel_9.setObjectName(u"wspolczynnikWypelnieniaLabel_9")

        self.skokJednostkowyLayout.setWidget(3, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_9)

        self.wspolczynnikWypelnieniaDoubleSpinBox_9 = QDoubleSpinBox(self.formLayoutWidget_12)
        self.wspolczynnikWypelnieniaDoubleSpinBox_9.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_9")
        self.wspolczynnikWypelnieniaDoubleSpinBox_9.setMaximum(100000.000000000000000)

        self.skokJednostkowyLayout.setWidget(3, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_9)

        self.generujStackedWidget.addWidget(self.skokJednostkowy)
        self.impulsJednostkowy = QWidget()
        self.impulsJednostkowy.setObjectName(u"impulsJednostkowy")
        self.formLayoutWidget_13 = QWidget(self.impulsJednostkowy)
        self.formLayoutWidget_13.setObjectName(u"formLayoutWidget_13")
        self.formLayoutWidget_13.setGeometry(QRect(0, 20, 331, 221))
        self.impulsJednostkowyLayout = QFormLayout(self.formLayoutWidget_13)
        self.impulsJednostkowyLayout.setObjectName(u"impulsJednostkowyLayout")
        self.impulsJednostkowyLayout.setVerticalSpacing(12)
        self.impulsJednostkowyLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_10 = QLabel(self.formLayoutWidget_13)
        self.poczatekSygnaluLabel_10.setObjectName(u"poczatekSygnaluLabel_10")

        self.impulsJednostkowyLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_10)

        self.poczatekSygnaluDoubleSpinBox_10 = QDoubleSpinBox(self.formLayoutWidget_13)
        self.poczatekSygnaluDoubleSpinBox_10.setObjectName(u"poczatekSygnaluDoubleSpinBox_10")
        self.poczatekSygnaluDoubleSpinBox_10.setMaximum(100000.000000000000000)

        self.impulsJednostkowyLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_10)

        self.dlugoscSygnaluLabel_10 = QLabel(self.formLayoutWidget_13)
        self.dlugoscSygnaluLabel_10.setObjectName(u"dlugoscSygnaluLabel_10")

        self.impulsJednostkowyLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_10)

        self.dlugoscSygnaluDoubleSpinBox_10 = QDoubleSpinBox(self.formLayoutWidget_13)
        self.dlugoscSygnaluDoubleSpinBox_10.setObjectName(u"dlugoscSygnaluDoubleSpinBox_10")
        self.dlugoscSygnaluDoubleSpinBox_10.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_10.setValue(10.000000000000000)

        self.impulsJednostkowyLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_10)

        self.amplitudaLabel_10 = QLabel(self.formLayoutWidget_13)
        self.amplitudaLabel_10.setObjectName(u"amplitudaLabel_10")

        self.impulsJednostkowyLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_10)

        self.amplitudaDoubleSpinBox_10 = QDoubleSpinBox(self.formLayoutWidget_13)
        self.amplitudaDoubleSpinBox_10.setObjectName(u"amplitudaDoubleSpinBox_10")
        self.amplitudaDoubleSpinBox_10.setMaximum(100000.000000000000000)

        self.impulsJednostkowyLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_10)

        self.wspolczynnikWypelnieniaLabel_10 = QLabel(self.formLayoutWidget_13)
        self.wspolczynnikWypelnieniaLabel_10.setObjectName(u"wspolczynnikWypelnieniaLabel_10")

        self.impulsJednostkowyLayout.setWidget(3, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_10)

        self.wspolczynnikWypelnieniaDoubleSpinBox_10 = QSpinBox(self.formLayoutWidget_13)
        self.wspolczynnikWypelnieniaDoubleSpinBox_10.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_10")

        self.impulsJednostkowyLayout.setWidget(3, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_10)

        self.czestotliwoscProbkowaniaLabel_10 = QLabel(self.formLayoutWidget_13)
        self.czestotliwoscProbkowaniaLabel_10.setObjectName(u"czestotliwoscProbkowaniaLabel_10")

        self.impulsJednostkowyLayout.setWidget(4, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel_10)

        self.czestotliwoscProbkowaniaDoubleSpinBox_10 = QDoubleSpinBox(self.formLayoutWidget_13)
        self.czestotliwoscProbkowaniaDoubleSpinBox_10.setObjectName(u"czestotliwoscProbkowaniaDoubleSpinBox_10")
        self.czestotliwoscProbkowaniaDoubleSpinBox_10.setMaximum(100000.000000000000000)

        self.impulsJednostkowyLayout.setWidget(4, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox_10)

        self.generujStackedWidget.addWidget(self.impulsJednostkowy)
        self.szumImpulsowy = QWidget()
        self.szumImpulsowy.setObjectName(u"szumImpulsowy")
        self.formLayoutWidget_14 = QWidget(self.szumImpulsowy)
        self.formLayoutWidget_14.setObjectName(u"formLayoutWidget_14")
        self.formLayoutWidget_14.setGeometry(QRect(0, 20, 331, 221))
        self.szumImpulsowyLayout = QFormLayout(self.formLayoutWidget_14)
        self.szumImpulsowyLayout.setObjectName(u"szumImpulsowyLayout")
        self.szumImpulsowyLayout.setVerticalSpacing(12)
        self.szumImpulsowyLayout.setContentsMargins(0, 0, 0, 0)
        self.poczatekSygnaluLabel_11 = QLabel(self.formLayoutWidget_14)
        self.poczatekSygnaluLabel_11.setObjectName(u"poczatekSygnaluLabel_11")

        self.szumImpulsowyLayout.setWidget(0, QFormLayout.LabelRole, self.poczatekSygnaluLabel_11)

        self.poczatekSygnaluDoubleSpinBox_11 = QDoubleSpinBox(self.formLayoutWidget_14)
        self.poczatekSygnaluDoubleSpinBox_11.setObjectName(u"poczatekSygnaluDoubleSpinBox_11")
        self.poczatekSygnaluDoubleSpinBox_11.setMaximum(100000.000000000000000)

        self.szumImpulsowyLayout.setWidget(0, QFormLayout.FieldRole, self.poczatekSygnaluDoubleSpinBox_11)

        self.dlugoscSygnaluLabel_11 = QLabel(self.formLayoutWidget_14)
        self.dlugoscSygnaluLabel_11.setObjectName(u"dlugoscSygnaluLabel_11")

        self.szumImpulsowyLayout.setWidget(1, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_11)

        self.dlugoscSygnaluDoubleSpinBox_11 = QDoubleSpinBox(self.formLayoutWidget_14)
        self.dlugoscSygnaluDoubleSpinBox_11.setObjectName(u"dlugoscSygnaluDoubleSpinBox_11")
        self.dlugoscSygnaluDoubleSpinBox_11.setMaximum(100000.000000000000000)
        self.dlugoscSygnaluDoubleSpinBox_11.setValue(10.000000000000000)

        self.szumImpulsowyLayout.setWidget(1, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_11)

        self.amplitudaLabel_11 = QLabel(self.formLayoutWidget_14)
        self.amplitudaLabel_11.setObjectName(u"amplitudaLabel_11")

        self.szumImpulsowyLayout.setWidget(2, QFormLayout.LabelRole, self.amplitudaLabel_11)

        self.amplitudaDoubleSpinBox_11 = QDoubleSpinBox(self.formLayoutWidget_14)
        self.amplitudaDoubleSpinBox_11.setObjectName(u"amplitudaDoubleSpinBox_11")
        self.amplitudaDoubleSpinBox_11.setMaximum(100000.000000000000000)

        self.szumImpulsowyLayout.setWidget(2, QFormLayout.FieldRole, self.amplitudaDoubleSpinBox_11)

        self.wspolczynnikWypelnieniaLabel_11 = QLabel(self.formLayoutWidget_14)
        self.wspolczynnikWypelnieniaLabel_11.setObjectName(u"wspolczynnikWypelnieniaLabel_11")

        self.szumImpulsowyLayout.setWidget(3, QFormLayout.LabelRole, self.wspolczynnikWypelnieniaLabel_11)

        self.wspolczynnikWypelnieniaDoubleSpinBox_11 = QDoubleSpinBox(self.formLayoutWidget_14)
        self.wspolczynnikWypelnieniaDoubleSpinBox_11.setObjectName(u"wspolczynnikWypelnieniaDoubleSpinBox_11")
        self.wspolczynnikWypelnieniaDoubleSpinBox_11.setMaximum(100000.000000000000000)

        self.szumImpulsowyLayout.setWidget(3, QFormLayout.FieldRole, self.wspolczynnikWypelnieniaDoubleSpinBox_11)

        self.czestotliwoscProbkowaniaLabel_11 = QLabel(self.formLayoutWidget_14)
        self.czestotliwoscProbkowaniaLabel_11.setObjectName(u"czestotliwoscProbkowaniaLabel_11")

        self.szumImpulsowyLayout.setWidget(4, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel_11)

        self.czestotliwoscProbkowaniaDoubleSpinBox_11 = QDoubleSpinBox(self.formLayoutWidget_14)
        self.czestotliwoscProbkowaniaDoubleSpinBox_11.setObjectName(u"czestotliwoscProbkowaniaDoubleSpinBox_11")
        self.czestotliwoscProbkowaniaDoubleSpinBox_11.setMaximum(100000.000000000000000)

        self.szumImpulsowyLayout.setWidget(4, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox_11)

        self.generujStackedWidget.addWidget(self.szumImpulsowy)
        self.filtrDolnoprzepustowy = QWidget()
        self.filtrDolnoprzepustowy.setObjectName(u"filtrDolnoprzepustowy")
        self.formLayoutWidget_15 = QWidget(self.filtrDolnoprzepustowy)
        self.formLayoutWidget_15.setObjectName(u"formLayoutWidget_15")
        self.formLayoutWidget_15.setGeometry(QRect(0, 20, 331, 221))
        self.filtrDolnoprzepustowyLayout = QFormLayout(self.formLayoutWidget_15)
        self.filtrDolnoprzepustowyLayout.setObjectName(u"filtrDolnoprzepustowyLayout")
        self.filtrDolnoprzepustowyLayout.setVerticalSpacing(12)
        self.filtrDolnoprzepustowyLayout.setContentsMargins(0, 0, 0, 0)
        self.dlugoscSygnaluLabel_12 = QLabel(self.formLayoutWidget_15)
        self.dlugoscSygnaluLabel_12.setObjectName(u"dlugoscSygnaluLabel_12")

        self.filtrDolnoprzepustowyLayout.setWidget(0, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_12)

        self.dlugoscSygnaluDoubleSpinBox_12 = QSpinBox(self.formLayoutWidget_15)
        self.dlugoscSygnaluDoubleSpinBox_12.setObjectName(u"dlugoscSygnaluDoubleSpinBox_12")

        self.filtrDolnoprzepustowyLayout.setWidget(0, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_12)

        self.czestotliwoscLabel_12 = QLabel(self.formLayoutWidget_15)
        self.czestotliwoscLabel_12.setObjectName(u"czestotliwoscLabel_12")

        self.filtrDolnoprzepustowyLayout.setWidget(1, QFormLayout.LabelRole, self.czestotliwoscLabel_12)

        self.czestotliwoscDoubleSpinBox_12 = QDoubleSpinBox(self.formLayoutWidget_15)
        self.czestotliwoscDoubleSpinBox_12.setObjectName(u"czestotliwoscDoubleSpinBox_12")
        self.czestotliwoscDoubleSpinBox_12.setMaximum(100000.000000000000000)

        self.filtrDolnoprzepustowyLayout.setWidget(1, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_12)

        self.czestotliwoscProbkowaniaLabel_12 = QLabel(self.formLayoutWidget_15)
        self.czestotliwoscProbkowaniaLabel_12.setObjectName(u"czestotliwoscProbkowaniaLabel_12")

        self.filtrDolnoprzepustowyLayout.setWidget(2, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel_12)

        self.czestotliwoscProbkowaniaDoubleSpinBox_12 = QDoubleSpinBox(self.formLayoutWidget_15)
        self.czestotliwoscProbkowaniaDoubleSpinBox_12.setObjectName(u"czestotliwoscProbkowaniaDoubleSpinBox_12")
        self.czestotliwoscProbkowaniaDoubleSpinBox_12.setMaximum(100000.000000000000000)

        self.filtrDolnoprzepustowyLayout.setWidget(2, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox_12)

        self.typOknaLabel_12 = QLabel(self.formLayoutWidget_15)
        self.typOknaLabel_12.setObjectName(u"typOknaLabel_12")

        self.filtrDolnoprzepustowyLayout.setWidget(3, QFormLayout.LabelRole, self.typOknaLabel_12)

        self.typOknaComboBox_12 = QComboBox(self.formLayoutWidget_15)
        self.typOknaComboBox_12.addItem("")
        self.typOknaComboBox_12.addItem("")
        self.typOknaComboBox_12.setObjectName(u"typOknaComboBox_12")

        self.filtrDolnoprzepustowyLayout.setWidget(3, QFormLayout.FieldRole, self.typOknaComboBox_12)

        self.generujStackedWidget.addWidget(self.filtrDolnoprzepustowy)
        self.filtrGornoprzepustowy = QWidget()
        self.filtrGornoprzepustowy.setObjectName(u"filtrGornoprzepustowy")
        self.formLayoutWidget_16 = QWidget(self.filtrGornoprzepustowy)
        self.formLayoutWidget_16.setObjectName(u"formLayoutWidget_16")
        self.formLayoutWidget_16.setGeometry(QRect(0, 20, 331, 221))
        self.filtrGornoprzepustowyLayout = QFormLayout(self.formLayoutWidget_16)
        self.filtrGornoprzepustowyLayout.setObjectName(u"filtrGornoprzepustowyLayout")
        self.filtrGornoprzepustowyLayout.setVerticalSpacing(12)
        self.filtrGornoprzepustowyLayout.setContentsMargins(0, 0, 0, 0)
        self.dlugoscSygnaluLabel_13 = QLabel(self.formLayoutWidget_16)
        self.dlugoscSygnaluLabel_13.setObjectName(u"dlugoscSygnaluLabel_13")

        self.filtrGornoprzepustowyLayout.setWidget(0, QFormLayout.LabelRole, self.dlugoscSygnaluLabel_13)

        self.dlugoscSygnaluDoubleSpinBox_13 = QSpinBox(self.formLayoutWidget_16)
        self.dlugoscSygnaluDoubleSpinBox_13.setObjectName(u"dlugoscSygnaluDoubleSpinBox_13")

        self.filtrGornoprzepustowyLayout.setWidget(0, QFormLayout.FieldRole, self.dlugoscSygnaluDoubleSpinBox_13)

        self.czestotliwoscLabel_13 = QLabel(self.formLayoutWidget_16)
        self.czestotliwoscLabel_13.setObjectName(u"czestotliwoscLabel_13")

        self.filtrGornoprzepustowyLayout.setWidget(1, QFormLayout.LabelRole, self.czestotliwoscLabel_13)

        self.czestotliwoscDoubleSpinBox_13 = QDoubleSpinBox(self.formLayoutWidget_16)
        self.czestotliwoscDoubleSpinBox_13.setObjectName(u"czestotliwoscDoubleSpinBox_13")

        self.filtrGornoprzepustowyLayout.setWidget(1, QFormLayout.FieldRole, self.czestotliwoscDoubleSpinBox_13)

        self.czestotliwoscProbkowaniaLabel_13 = QLabel(self.formLayoutWidget_16)
        self.czestotliwoscProbkowaniaLabel_13.setObjectName(u"czestotliwoscProbkowaniaLabel_13")

        self.filtrGornoprzepustowyLayout.setWidget(2, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel_13)

        self.czestotliwoscProbkowaniaDoubleSpinBox_13 = QDoubleSpinBox(self.formLayoutWidget_16)
        self.czestotliwoscProbkowaniaDoubleSpinBox_13.setObjectName(u"czestotliwoscProbkowaniaDoubleSpinBox_13")
        self.czestotliwoscProbkowaniaDoubleSpinBox_13.setMaximum(100000.000000000000000)

        self.filtrGornoprzepustowyLayout.setWidget(2, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox_13)

        self.typOknaLabel_13 = QLabel(self.formLayoutWidget_16)
        self.typOknaLabel_13.setObjectName(u"typOknaLabel_13")

        self.filtrGornoprzepustowyLayout.setWidget(3, QFormLayout.LabelRole, self.typOknaLabel_13)

        self.typOknaComboBox_13 = QComboBox(self.formLayoutWidget_16)
        self.typOknaComboBox_13.addItem("")
        self.typOknaComboBox_13.addItem("")
        self.typOknaComboBox_13.setObjectName(u"typOknaComboBox_13")

        self.filtrGornoprzepustowyLayout.setWidget(3, QFormLayout.FieldRole, self.typOknaComboBox_13)

        self.generujStackedWidget.addWidget(self.filtrGornoprzepustowy)
        self.wygenerowaneGroupBox = QGroupBox(self.centralwidget)
        self.wygenerowaneGroupBox.setObjectName(u"wygenerowaneGroupBox")
        self.wygenerowaneGroupBox.setGeometry(QRect(10, 620, 1181, 381))
        self.gridLayoutWidget = QWidget(self.wygenerowaneGroupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 20, 1161, 351))
        self.wygenerowaneLayout = QGridLayout(self.gridLayoutWidget)
        self.wygenerowaneLayout.setObjectName(u"wygenerowaneLayout")
        self.wygenerowaneLayout.setContentsMargins(0, 0, 0, 0)
        self.prawyWygenerowaneTab = QTabWidget(self.gridLayoutWidget)
        self.prawyWygenerowaneTab.setObjectName(u"prawyWygenerowaneTab")
        self.wykresPrawyWygenerowaneTab = QWidget()
        self.wykresPrawyWygenerowaneTab.setObjectName(u"wykresPrawyWygenerowaneTab")
        self.verticalLayoutWidget_8 = QWidget(self.wykresPrawyWygenerowaneTab)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 10, 551, 311))
        self.wykresPrawyLayout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.wykresPrawyLayout.setObjectName(u"wykresPrawyLayout")
        self.wykresPrawyLayout.setContentsMargins(0, 0, 0, 0)
        self.prawyWygenerowaneTab.addTab(self.wykresPrawyWygenerowaneTab, "")
        self.histogramPrawyWygenerowaneTab = QWidget()
        self.histogramPrawyWygenerowaneTab.setObjectName(u"histogramPrawyWygenerowaneTab")
        self.verticalLayoutWidget_7 = QWidget(self.histogramPrawyWygenerowaneTab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 551, 351))
        self.histogramPrawyLayout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.histogramPrawyLayout.setObjectName(u"histogramPrawyLayout")
        self.histogramPrawyLayout.setContentsMargins(0, 0, 0, 0)
        self.prawyWygenerowaneTab.addTab(self.histogramPrawyWygenerowaneTab, "")
        self.statystykiPrawyWygenerowaneTab = QWidget()
        self.statystykiPrawyWygenerowaneTab.setObjectName(u"statystykiPrawyWygenerowaneTab")
        self.verticalLayoutWidget_10 = QWidget(self.statystykiPrawyWygenerowaneTab)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(80, 50, 421, 181))
        self.statystykiPrawyLayout = QVBoxLayout(self.verticalLayoutWidget_10)
        self.statystykiPrawyLayout.setObjectName(u"statystykiPrawyLayout")
        self.statystykiPrawyLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiPrawyWidget = QTableWidget(self.verticalLayoutWidget_10)
        if (self.statystykiPrawyWidget.columnCount() < 1):
            self.statystykiPrawyWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.statystykiPrawyWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.statystykiPrawyWidget.rowCount() < 5):
            self.statystykiPrawyWidget.setRowCount(5)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.statystykiPrawyWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.statystykiPrawyWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.statystykiPrawyWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.statystykiPrawyWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.statystykiPrawyWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.statystykiPrawyWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.statystykiPrawyWidget.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.statystykiPrawyWidget.setItem(2, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.statystykiPrawyWidget.setItem(3, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.statystykiPrawyWidget.setItem(4, 0, __qtablewidgetitem10)
        self.statystykiPrawyWidget.setObjectName(u"statystykiPrawyWidget")

        self.statystykiPrawyLayout.addWidget(self.statystykiPrawyWidget)

        self.prawyWygenerowaneTab.addTab(self.statystykiPrawyWygenerowaneTab, "")

        self.wygenerowaneLayout.addWidget(self.prawyWygenerowaneTab, 0, 2, 1, 1)

        self.lewyWygenerowaneTab = QTabWidget(self.gridLayoutWidget)
        self.lewyWygenerowaneTab.setObjectName(u"lewyWygenerowaneTab")
        self.wykresLewyWygenerowaneTab = QWidget()
        self.wykresLewyWygenerowaneTab.setObjectName(u"wykresLewyWygenerowaneTab")
        self.gridLayoutWidget_2 = QWidget(self.wykresLewyWygenerowaneTab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 551, 311))
        self.wykresLewyLayout = QGridLayout(self.gridLayoutWidget_2)
        self.wykresLewyLayout.setSpacing(0)
        self.wykresLewyLayout.setObjectName(u"wykresLewyLayout")
        self.wykresLewyLayout.setContentsMargins(0, 0, 0, 0)
        self.lewyWygenerowaneTab.addTab(self.wykresLewyWygenerowaneTab, "")
        self.histogramLewyWygenerowaneTab = QWidget()
        self.histogramLewyWygenerowaneTab.setObjectName(u"histogramLewyWygenerowaneTab")
        self.verticalLayoutWidget_5 = QWidget(self.histogramLewyWygenerowaneTab)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 551, 351))
        self.histogramLewyLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.histogramLewyLayout.setObjectName(u"histogramLewyLayout")
        self.histogramLewyLayout.setContentsMargins(0, 0, 0, 0)
        self.lewyWygenerowaneTab.addTab(self.histogramLewyWygenerowaneTab, "")
        self.statystykiLewyWygenerowaneTab = QWidget()
        self.statystykiLewyWygenerowaneTab.setObjectName(u"statystykiLewyWygenerowaneTab")
        self.verticalLayoutWidget_6 = QWidget(self.statystykiLewyWygenerowaneTab)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(70, 50, 421, 181))
        self.statystykiLewyLayout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.statystykiLewyLayout.setObjectName(u"statystykiLewyLayout")
        self.statystykiLewyLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiLewyWidget = QTableWidget(self.verticalLayoutWidget_6)
        if (self.statystykiLewyWidget.columnCount() < 1):
            self.statystykiLewyWidget.setColumnCount(1)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.statystykiLewyWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        if (self.statystykiLewyWidget.rowCount() < 5):
            self.statystykiLewyWidget.setRowCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.statystykiLewyWidget.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.statystykiLewyWidget.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.statystykiLewyWidget.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.statystykiLewyWidget.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.statystykiLewyWidget.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.statystykiLewyWidget.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.statystykiLewyWidget.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.statystykiLewyWidget.setItem(2, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.statystykiLewyWidget.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.statystykiLewyWidget.setItem(4, 0, __qtablewidgetitem21)
        self.statystykiLewyWidget.setObjectName(u"statystykiLewyWidget")

        self.statystykiLewyLayout.addWidget(self.statystykiLewyWidget)

        self.lewyWygenerowaneTab.addTab(self.statystykiLewyWygenerowaneTab, "")

        self.wygenerowaneLayout.addWidget(self.lewyWygenerowaneTab, 0, 1, 1, 1)

        self.dzialaniaGroupBox = QGroupBox(self.centralwidget)
        self.dzialaniaGroupBox.setObjectName(u"dzialaniaGroupBox")
        self.dzialaniaGroupBox.setGeometry(QRect(380, 10, 811, 611))
        self.wynikowyTab = QTabWidget(self.dzialaniaGroupBox)
        self.wynikowyTab.setObjectName(u"wynikowyTab")
        self.wynikowyTab.setGeometry(QRect(250, 10, 551, 601))
        self.wykresWynikowyTab = QWidget()
        self.wykresWynikowyTab.setObjectName(u"wykresWynikowyTab")
        self.verticalLayoutWidget_3 = QWidget(self.wykresWynikowyTab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 531, 481))
        self.wykresWynikowyLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.wykresWynikowyLayout.setObjectName(u"wykresWynikowyLayout")
        self.wykresWynikowyLayout.setContentsMargins(0, 0, 0, 0)
        self.wynikowyTab.addTab(self.wykresWynikowyTab, "")
        self.histogramWynikowyTab = QWidget()
        self.histogramWynikowyTab.setObjectName(u"histogramWynikowyTab")
        self.verticalLayoutWidget_9 = QWidget(self.histogramWynikowyTab)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 531, 481))
        self.histogramWynikowyLayout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.histogramWynikowyLayout.setObjectName(u"histogramWynikowyLayout")
        self.histogramWynikowyLayout.setContentsMargins(0, 0, 0, 0)
        self.wynikowyTab.addTab(self.histogramWynikowyTab, "")
        self.statystykiWynikowyTab = QWidget()
        self.statystykiWynikowyTab.setObjectName(u"statystykiWynikowyTab")
        self.verticalLayoutWidget_11 = QWidget(self.statystykiWynikowyTab)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(60, 10, 421, 181))
        self.statystykiWynikowyLayout = QVBoxLayout(self.verticalLayoutWidget_11)
        self.statystykiWynikowyLayout.setObjectName(u"statystykiWynikowyLayout")
        self.statystykiWynikowyLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiWynikowyWidget = QTableWidget(self.verticalLayoutWidget_11)
        if (self.statystykiWynikowyWidget.columnCount() < 1):
            self.statystykiWynikowyWidget.setColumnCount(1)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        if (self.statystykiWynikowyWidget.rowCount() < 5):
            self.statystykiWynikowyWidget.setRowCount(5)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setVerticalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setVerticalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setVerticalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setItem(0, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setItem(2, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setItem(3, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.statystykiWynikowyWidget.setItem(4, 0, __qtablewidgetitem32)
        self.statystykiWynikowyWidget.setObjectName(u"statystykiWynikowyWidget")

        self.statystykiWynikowyLayout.addWidget(self.statystykiWynikowyWidget)

        self.verticalLayoutWidget_12 = QWidget(self.statystykiWynikowyTab)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(140, 190, 251, 151))
        self.statystykiWynikowyExtraLayout = QVBoxLayout(self.verticalLayoutWidget_12)
        self.statystykiWynikowyExtraLayout.setObjectName(u"statystykiWynikowyExtraLayout")
        self.statystykiWynikowyExtraLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiWynikowyExtraWidget = QTableWidget(self.verticalLayoutWidget_12)
        if (self.statystykiWynikowyExtraWidget.columnCount() < 1):
            self.statystykiWynikowyExtraWidget.setColumnCount(1)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        if (self.statystykiWynikowyExtraWidget.rowCount() < 4):
            self.statystykiWynikowyExtraWidget.setRowCount(4)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setVerticalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setVerticalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setVerticalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setVerticalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setItem(0, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setItem(2, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.statystykiWynikowyExtraWidget.setItem(3, 0, __qtablewidgetitem41)
        self.statystykiWynikowyExtraWidget.setObjectName(u"statystykiWynikowyExtraWidget")

        self.statystykiWynikowyExtraLayout.addWidget(self.statystykiWynikowyExtraWidget)

        self.wynikowyTab.addTab(self.statystykiWynikowyTab, "")
        self.wykresW1Tab = QWidget()
        self.wykresW1Tab.setObjectName(u"wykresW1Tab")
        self.verticalLayoutWidget_16 = QWidget(self.wykresW1Tab)
        self.verticalLayoutWidget_16.setObjectName(u"verticalLayoutWidget_16")
        self.verticalLayoutWidget_16.setGeometry(QRect(0, 0, 541, 281))
        self.wykresW1LayoutUpper = QVBoxLayout(self.verticalLayoutWidget_16)
        self.wykresW1LayoutUpper.setObjectName(u"wykresW1LayoutUpper")
        self.wykresW1LayoutUpper.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.verticalLayoutWidget_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.wykresW1LayoutUpper.addWidget(self.label_5)

        self.label = QLabel(self.verticalLayoutWidget_16)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.wykresW1LayoutUpper.addWidget(self.label)

        self.verticalLayoutWidget_18 = QWidget(self.wykresW1Tab)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(0, 290, 541, 281))
        self.wykresW1LayoutLower = QVBoxLayout(self.verticalLayoutWidget_18)
        self.wykresW1LayoutLower.setObjectName(u"wykresW1LayoutLower")
        self.wykresW1LayoutLower.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_18)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.wykresW1LayoutLower.addWidget(self.label_6)

        self.label_2 = QLabel(self.verticalLayoutWidget_18)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.wykresW1LayoutLower.addWidget(self.label_2)

        self.wynikowyTab.addTab(self.wykresW1Tab, "")
        self.wykresW2Tab = QWidget()
        self.wykresW2Tab.setObjectName(u"wykresW2Tab")
        self.verticalLayoutWidget_17 = QWidget(self.wykresW2Tab)
        self.verticalLayoutWidget_17.setObjectName(u"verticalLayoutWidget_17")
        self.verticalLayoutWidget_17.setGeometry(QRect(0, 0, 541, 281))
        self.wykresW2LayoutUpper = QVBoxLayout(self.verticalLayoutWidget_17)
        self.wykresW2LayoutUpper.setObjectName(u"wykresW2LayoutUpper")
        self.wykresW2LayoutUpper.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_17)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.wykresW2LayoutUpper.addWidget(self.label_7)

        self.label_3 = QLabel(self.verticalLayoutWidget_17)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.wykresW2LayoutUpper.addWidget(self.label_3)

        self.verticalLayoutWidget_19 = QWidget(self.wykresW2Tab)
        self.verticalLayoutWidget_19.setObjectName(u"verticalLayoutWidget_19")
        self.verticalLayoutWidget_19.setGeometry(QRect(0, 290, 541, 281))
        self.wykresW2LayoutLower = QVBoxLayout(self.verticalLayoutWidget_19)
        self.wykresW2LayoutLower.setObjectName(u"wykresW2LayoutLower")
        self.wykresW2LayoutLower.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_19)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.wykresW2LayoutLower.addWidget(self.label_8)

        self.label_4 = QLabel(self.verticalLayoutWidget_19)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.wykresW2LayoutLower.addWidget(self.label_4)

        self.wynikowyTab.addTab(self.wykresW2Tab, "")
        self.dzialaniaTab = QTabWidget(self.dzialaniaGroupBox)
        self.dzialaniaTab.setObjectName(u"dzialaniaTab")
        self.dzialaniaTab.setGeometry(QRect(10, 20, 231, 391))
        self.dzialaniaJednoSygnaloweTab = QWidget()
        self.dzialaniaJednoSygnaloweTab.setObjectName(u"dzialaniaJednoSygnaloweTab")
        self.formLayoutWidget_2 = QWidget(self.dzialaniaJednoSygnaloweTab)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 10, 194, 172))
        self.dzialaniaJednoLayout = QFormLayout(self.formLayoutWidget_2)
        self.dzialaniaJednoLayout.setObjectName(u"dzialaniaJednoLayout")
        self.dzialaniaJednoLayout.setVerticalSpacing(15)
        self.dzialaniaJednoLayout.setContentsMargins(0, 0, 0, 0)
        self.operacjaJednoLabel = QLabel(self.formLayoutWidget_2)
        self.operacjaJednoLabel.setObjectName(u"operacjaJednoLabel")

        self.dzialaniaJednoLayout.setWidget(0, QFormLayout.LabelRole, self.operacjaJednoLabel)

        self.operacjaJednoComboBox = QComboBox(self.formLayoutWidget_2)
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.addItem("")
        self.operacjaJednoComboBox.setObjectName(u"operacjaJednoComboBox")

        self.dzialaniaJednoLayout.setWidget(0, QFormLayout.FieldRole, self.operacjaJednoComboBox)

        self.jednoCzestotliwoscProbkowaniaLabel = QLabel(self.formLayoutWidget_2)
        self.jednoCzestotliwoscProbkowaniaLabel.setObjectName(u"jednoCzestotliwoscProbkowaniaLabel")

        self.dzialaniaJednoLayout.setWidget(1, QFormLayout.LabelRole, self.jednoCzestotliwoscProbkowaniaLabel)

        self.jednoCzestotliwoscProbkowaniaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.jednoCzestotliwoscProbkowaniaDoubleSpinBox.setObjectName(u"jednoCzestotliwoscProbkowaniaDoubleSpinBox")
        self.jednoCzestotliwoscProbkowaniaDoubleSpinBox.setMaximum(100000.000000000000000)

        self.dzialaniaJednoLayout.setWidget(1, QFormLayout.FieldRole, self.jednoCzestotliwoscProbkowaniaDoubleSpinBox)

        self.bityKwantyzacjiLabel = QLabel(self.formLayoutWidget_2)
        self.bityKwantyzacjiLabel.setObjectName(u"bityKwantyzacjiLabel")

        self.dzialaniaJednoLayout.setWidget(2, QFormLayout.LabelRole, self.bityKwantyzacjiLabel)

        self.bityKwantyzacjiDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.bityKwantyzacjiDoubleSpinBox.setObjectName(u"bityKwantyzacjiDoubleSpinBox")
        self.bityKwantyzacjiDoubleSpinBox.setMaximum(100000.000000000000000)

        self.dzialaniaJednoLayout.setWidget(2, QFormLayout.FieldRole, self.bityKwantyzacjiDoubleSpinBox)

        self.typRekonstrukcjiLabel = QLabel(self.formLayoutWidget_2)
        self.typRekonstrukcjiLabel.setObjectName(u"typRekonstrukcjiLabel")

        self.dzialaniaJednoLayout.setWidget(3, QFormLayout.LabelRole, self.typRekonstrukcjiLabel)

        self.typRekonstrukcjiComboBox = QComboBox(self.formLayoutWidget_2)
        self.typRekonstrukcjiComboBox.addItem("")
        self.typRekonstrukcjiComboBox.addItem("")
        self.typRekonstrukcjiComboBox.addItem("")
        self.typRekonstrukcjiComboBox.setObjectName(u"typRekonstrukcjiComboBox")

        self.dzialaniaJednoLayout.setWidget(3, QFormLayout.FieldRole, self.typRekonstrukcjiComboBox)

        self.sygnalLabel = QLabel(self.formLayoutWidget_2)
        self.sygnalLabel.setObjectName(u"sygnalLabel")

        self.dzialaniaJednoLayout.setWidget(4, QFormLayout.LabelRole, self.sygnalLabel)

        self.sygnalComboBox = QComboBox(self.formLayoutWidget_2)
        self.sygnalComboBox.addItem("")
        self.sygnalComboBox.addItem("")
        self.sygnalComboBox.addItem("")
        self.sygnalComboBox.setObjectName(u"sygnalComboBox")

        self.dzialaniaJednoLayout.setWidget(4, QFormLayout.FieldRole, self.sygnalComboBox)

        self.verticalLayoutWidget_2 = QWidget(self.dzialaniaJednoSygnaloweTab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 180, 191, 31))
        self.dzialaniaJednoWykonajLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.dzialaniaJednoWykonajLayout.setObjectName(u"dzialaniaJednoWykonajLayout")
        self.dzialaniaJednoWykonajLayout.setContentsMargins(0, 0, 0, 0)
        self.dzialaniaJednoWykonajButton = QPushButton(self.verticalLayoutWidget_2)
        self.dzialaniaJednoWykonajButton.setObjectName(u"dzialaniaJednoWykonajButton")

        self.dzialaniaJednoWykonajLayout.addWidget(self.dzialaniaJednoWykonajButton)

        self.dzialaniaTab.addTab(self.dzialaniaJednoSygnaloweTab, "")
        self.dzialaniaDwuSygnaloweTab = QWidget()
        self.dzialaniaDwuSygnaloweTab.setObjectName(u"dzialaniaDwuSygnaloweTab")
        self.verticalLayoutWidget = QWidget(self.dzialaniaDwuSygnaloweTab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 110, 201, 31))
        self.dzialaniaDwuWykonajLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.dzialaniaDwuWykonajLayout.setObjectName(u"dzialaniaDwuWykonajLayout")
        self.dzialaniaDwuWykonajLayout.setContentsMargins(0, 0, 0, 0)
        self.dzialaniaDwuWykonajButton = QPushButton(self.verticalLayoutWidget)
        self.dzialaniaDwuWykonajButton.setObjectName(u"dzialaniaDwuWykonajButton")

        self.dzialaniaDwuWykonajLayout.addWidget(self.dzialaniaDwuWykonajButton)

        self.formLayoutWidget_3 = QWidget(self.dzialaniaDwuSygnaloweTab)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 10, 201, 101))
        self.dzialaniaDwuLayout = QFormLayout(self.formLayoutWidget_3)
        self.dzialaniaDwuLayout.setObjectName(u"dzialaniaDwuLayout")
        self.dzialaniaDwuLayout.setVerticalSpacing(14)
        self.dzialaniaDwuLayout.setContentsMargins(0, 0, 0, 0)
        self.sygnal1DwuLabel = QLabel(self.formLayoutWidget_3)
        self.sygnal1DwuLabel.setObjectName(u"sygnal1DwuLabel")

        self.dzialaniaDwuLayout.setWidget(0, QFormLayout.LabelRole, self.sygnal1DwuLabel)

        self.sygnal1DwuComboBox = QComboBox(self.formLayoutWidget_3)
        self.sygnal1DwuComboBox.addItem("")
        self.sygnal1DwuComboBox.addItem("")
        self.sygnal1DwuComboBox.addItem("")
        self.sygnal1DwuComboBox.setObjectName(u"sygnal1DwuComboBox")

        self.dzialaniaDwuLayout.setWidget(0, QFormLayout.FieldRole, self.sygnal1DwuComboBox)

        self.sygnal2DwuLabel = QLabel(self.formLayoutWidget_3)
        self.sygnal2DwuLabel.setObjectName(u"sygnal2DwuLabel")

        self.dzialaniaDwuLayout.setWidget(1, QFormLayout.LabelRole, self.sygnal2DwuLabel)

        self.sygnal2DwuComboBox = QComboBox(self.formLayoutWidget_3)
        self.sygnal2DwuComboBox.addItem("")
        self.sygnal2DwuComboBox.addItem("")
        self.sygnal2DwuComboBox.addItem("")
        self.sygnal2DwuComboBox.setObjectName(u"sygnal2DwuComboBox")

        self.dzialaniaDwuLayout.setWidget(1, QFormLayout.FieldRole, self.sygnal2DwuComboBox)

        self.operacjaDwuLabel = QLabel(self.formLayoutWidget_3)
        self.operacjaDwuLabel.setObjectName(u"operacjaDwuLabel")

        self.dzialaniaDwuLayout.setWidget(2, QFormLayout.LabelRole, self.operacjaDwuLabel)

        self.operacjaDwuComboBox = QComboBox(self.formLayoutWidget_3)
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.addItem("")
        self.operacjaDwuComboBox.setObjectName(u"operacjaDwuComboBox")

        self.dzialaniaDwuLayout.setWidget(2, QFormLayout.FieldRole, self.operacjaDwuComboBox)

        self.dzialaniaTab.addTab(self.dzialaniaDwuSygnaloweTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1200, 21))
        self.menustandard = QMenu(self.menuBar)
        self.menustandard.setObjectName(u"menustandard")
        MainWindow.setMenuBar(self.menuBar)
#if QT_CONFIG(shortcut)
        self.typSygnaluLabel.setBuddy(self.typSygnaluComboBox)
        self.operacjaJednoLabel.setBuddy(self.operacjaJednoComboBox)
        self.jednoCzestotliwoscProbkowaniaLabel.setBuddy(self.jednoCzestotliwoscProbkowaniaDoubleSpinBox)
        self.bityKwantyzacjiLabel.setBuddy(self.bityKwantyzacjiDoubleSpinBox)
        self.typRekonstrukcjiLabel.setBuddy(self.typRekonstrukcjiComboBox)
        self.sygnalLabel.setBuddy(self.sygnalComboBox)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menustandard.menuAction())
        self.menustandard.addSeparator()
        self.menustandard.addAction(self.actiondystans)

        self.retranslateUi(MainWindow)
        self.typSygnaluComboBox.currentIndexChanged.connect(self.generujStackedWidget.setCurrentIndex)

        self.generujStackedWidget.setCurrentIndex(0)
        self.prawyWygenerowaneTab.setCurrentIndex(0)
        self.lewyWygenerowaneTab.setCurrentIndex(0)
        self.wynikowyTab.setCurrentIndex(0)
        self.dzialaniaTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actiondystans.setText(QCoreApplication.translate("MainWindow", u"dystans", None))
        self.typSygnaluLabel.setText(QCoreApplication.translate("MainWindow", u"Typ sygnalu: ", None))
        self.typSygnaluComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"szum gaussowski", None))
        self.typSygnaluComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"szum jednostajny", None))
        self.typSygnaluComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"sinus", None))
        self.typSygnaluComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"sinus jednopolowkowy", None))
        self.typSygnaluComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"sinus dwupolowkowy", None))
        self.typSygnaluComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"prostokat", None))
        self.typSygnaluComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"prostokat symetryczny", None))
        self.typSygnaluComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"trojkat", None))
        self.typSygnaluComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"skok jednostkowy", None))
        self.typSygnaluComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"impuls jednostkowy", None))
        self.typSygnaluComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"szum impulsowy", None))
        self.typSygnaluComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"filtr dolnoprzepustowy", None))
        self.typSygnaluComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"filtr g\u00f3rnoprzepustowy", None))

        self.generujLewy.setText(QCoreApplication.translate("MainWindow", u"generuj lewy", None))
        self.generujPrawy.setText(QCoreApplication.translate("MainWindow", u"generuj prawy", None))
        self.zapiszDoPlikuComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"lewy", None))
        self.zapiszDoPlikuComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"prawy", None))
        self.zapiszDoPlikuComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wynikowy", None))

        self.zapiszButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz do pliku", None))
        self.wczytajZPlikuComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"lewy", None))
        self.wczytajZPlikuComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"prawy", None))
        self.wczytajZPlikuComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wynikowy", None))

        self.wczytajButton.setText(QCoreApplication.translate("MainWindow", u"Wczytaj z pliku", None))
        self.poczatekSygnaluLabel_1.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_1.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.poczatekSygnaluLabel_2.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_2.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_2.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.poczatekSygnaluLabel_3.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_3.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_3.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_3.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.poczatekSygnaluLabel_4.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_4.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_4.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_4.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.poczatekSygnaluLabel_5.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_5.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_5.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_5.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.poczatekSygnaluLabel_6.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_6.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_6.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_6.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.wspolczynnikWypelnieniaLabel_6.setText(QCoreApplication.translate("MainWindow", u"Wspolczynnik wypelnienia", None))
        self.poczatekSygnaluLabel_7.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_7.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_7.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_7.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.wspolczynnikWypelnieniaLabel_7.setText(QCoreApplication.translate("MainWindow", u"Wspolczynnik wypelnienia", None))
        self.poczatekSygnaluLabel_8.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_8.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_8.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.czestotliwoscLabel_8.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.wspolczynnikWypelnieniaLabel_8.setText(QCoreApplication.translate("MainWindow", u"Wspolczynnik wypelnienia", None))
        self.poczatekSygnaluLabel_9.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_9.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_9.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.wspolczynnikWypelnieniaLabel_9.setText(QCoreApplication.translate("MainWindow", u"Czas skoku", None))
        self.poczatekSygnaluLabel_10.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_10.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_10.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.wspolczynnikWypelnieniaLabel_10.setText(QCoreApplication.translate("MainWindow", u"Numer probki ze skokiem", None))
        self.czestotliwoscProbkowaniaLabel_10.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc probkowania", None))
        self.poczatekSygnaluLabel_11.setText(QCoreApplication.translate("MainWindow", u"Poczatek sygnalu", None))
        self.dlugoscSygnaluLabel_11.setText(QCoreApplication.translate("MainWindow", u"Dlugosc sygnalu", None))
        self.amplitudaLabel_11.setText(QCoreApplication.translate("MainWindow", u"Amplituda", None))
        self.wspolczynnikWypelnieniaLabel_11.setText(QCoreApplication.translate("MainWindow", u"Prawdopodobienstwo skoku", None))
        self.czestotliwoscProbkowaniaLabel_11.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc probkowania", None))
        self.dlugoscSygnaluLabel_12.setText(QCoreApplication.translate("MainWindow", u"Rzad filtru", None))
        self.czestotliwoscLabel_12.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc odciecia", None))
        self.czestotliwoscProbkowaniaLabel_12.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc probkowania", None))
        self.typOknaLabel_12.setText(QCoreApplication.translate("MainWindow", u"Typ okna", None))
        self.typOknaComboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"prostokatny", None))
        self.typOknaComboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Blackmana", None))

        self.dlugoscSygnaluLabel_13.setText(QCoreApplication.translate("MainWindow", u"Rzad filtru", None))
        self.czestotliwoscLabel_13.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc odciecia", None))
        self.czestotliwoscProbkowaniaLabel_13.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc probkowania", None))
        self.typOknaLabel_13.setText(QCoreApplication.translate("MainWindow", u"Typ okna", None))
        self.typOknaComboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"prostokatny", None))
        self.typOknaComboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"Blackmana", None))

        self.wygenerowaneGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Wygenerowane sygna\u0142y", None))
        self.prawyWygenerowaneTab.setTabText(self.prawyWygenerowaneTab.indexOf(self.wykresPrawyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Wykres", None))
        self.prawyWygenerowaneTab.setTabText(self.prawyWygenerowaneTab.indexOf(self.histogramPrawyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Histogram", None))
        ___qtablewidgetitem = self.statystykiPrawyWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem1 = self.statystykiPrawyWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem2 = self.statystykiPrawyWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia bezwzgl\u0119dna sygna\u0142u", None));
        ___qtablewidgetitem3 = self.statystykiPrawyWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Moc \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem4 = self.statystykiPrawyWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Wariancja sygna\u0142u w przedziale wok\u00f3\u0142 warto\u015bci \u015bredniej", None));
        ___qtablewidgetitem5 = self.statystykiPrawyWidget.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 skuteczna sygna\u0142u", None));

        __sortingEnabled = self.statystykiPrawyWidget.isSortingEnabled()
        self.statystykiPrawyWidget.setSortingEnabled(False)
        self.statystykiPrawyWidget.setSortingEnabled(__sortingEnabled)

        self.prawyWygenerowaneTab.setTabText(self.prawyWygenerowaneTab.indexOf(self.statystykiPrawyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Statystyki", None))
        self.lewyWygenerowaneTab.setTabText(self.lewyWygenerowaneTab.indexOf(self.wykresLewyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Wykres", None))
        self.lewyWygenerowaneTab.setTabText(self.lewyWygenerowaneTab.indexOf(self.histogramLewyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Histogram", None))
        ___qtablewidgetitem6 = self.statystykiLewyWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem7 = self.statystykiLewyWidget.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem8 = self.statystykiLewyWidget.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia bezwzgl\u0119dna sygna\u0142u", None));
        ___qtablewidgetitem9 = self.statystykiLewyWidget.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Moc \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem10 = self.statystykiLewyWidget.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Wariancja sygna\u0142u w przedziale wok\u00f3\u0142 warto\u015bci \u015bredniej", None));
        ___qtablewidgetitem11 = self.statystykiLewyWidget.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 skuteczna sygna\u0142u", None));

        __sortingEnabled1 = self.statystykiLewyWidget.isSortingEnabled()
        self.statystykiLewyWidget.setSortingEnabled(False)
        self.statystykiLewyWidget.setSortingEnabled(__sortingEnabled1)

        self.lewyWygenerowaneTab.setTabText(self.lewyWygenerowaneTab.indexOf(self.statystykiLewyWygenerowaneTab), QCoreApplication.translate("MainWindow", u"Statystyki", None))
        self.dzialaniaGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dzia\u0142ania", None))
        self.wynikowyTab.setTabText(self.wynikowyTab.indexOf(self.wykresWynikowyTab), QCoreApplication.translate("MainWindow", u"Wykres", None))
        self.wynikowyTab.setTabText(self.wynikowyTab.indexOf(self.histogramWynikowyTab), QCoreApplication.translate("MainWindow", u"Histogram", None))
        ___qtablewidgetitem12 = self.statystykiWynikowyWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem13 = self.statystykiWynikowyWidget.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem14 = self.statystykiWynikowyWidget.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 \u015brednia bezwzgl\u0119dna sygna\u0142u", None));
        ___qtablewidgetitem15 = self.statystykiWynikowyWidget.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Moc \u015brednia sygna\u0142u", None));
        ___qtablewidgetitem16 = self.statystykiWynikowyWidget.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Wariancja sygna\u0142u w przedziale wok\u00f3\u0142 warto\u015bci \u015bredniej", None));
        ___qtablewidgetitem17 = self.statystykiWynikowyWidget.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107 skuteczna sygna\u0142u", None));

        __sortingEnabled2 = self.statystykiWynikowyWidget.isSortingEnabled()
        self.statystykiWynikowyWidget.setSortingEnabled(False)
        self.statystykiWynikowyWidget.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem18 = self.statystykiWynikowyExtraWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem19 = self.statystykiWynikowyExtraWidget.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"MSE", None));
        ___qtablewidgetitem20 = self.statystykiWynikowyExtraWidget.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Signal to noise ratio", None));
        ___qtablewidgetitem21 = self.statystykiWynikowyExtraWidget.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Peak signal to noise ratio", None));
        ___qtablewidgetitem22 = self.statystykiWynikowyExtraWidget.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Maksymalna r\u00f3\u017cnica", None));

        __sortingEnabled3 = self.statystykiWynikowyExtraWidget.isSortingEnabled()
        self.statystykiWynikowyExtraWidget.setSortingEnabled(False)
        self.statystykiWynikowyExtraWidget.setSortingEnabled(__sortingEnabled3)

        self.wynikowyTab.setTabText(self.wynikowyTab.indexOf(self.statystykiWynikowyTab), QCoreApplication.translate("MainWindow", u"Statystyki", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Wykres cz\u0119\u015bci rzeczywistej funkcji cz\u0119stotliwo\u015bci", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119stotliwo\u015b\u0107 [Hz]", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wykres cz\u0119\u015bci urojonej funkcji cz\u0119stotliwo\u015bci", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119stotliwo\u015b\u0107 [Hz]", None))
        self.wynikowyTab.setTabText(self.wynikowyTab.indexOf(self.wykresW1Tab), QCoreApplication.translate("MainWindow", u"W1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Modu\u0142 funkcji cz\u0119stotliwo\u015bci", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119stotliwo\u015b\u0107 [Hz]", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Argument funkcji cz\u0119stotliow\u015bci", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cz\u0119stotliwo\u015b\u0107 [Hz]", None))
        self.wynikowyTab.setTabText(self.wynikowyTab.indexOf(self.wykresW2Tab), QCoreApplication.translate("MainWindow", u"W2", None))
        self.operacjaJednoLabel.setText(QCoreApplication.translate("MainWindow", u"Operacja", None))
        self.operacjaJednoComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"pr\u00f3bkowanie", None))
        self.operacjaJednoComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"kwantyzacja", None))
        self.operacjaJednoComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"rekonstrukcja", None))
        self.operacjaJednoComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"DFT", None))
        self.operacjaJednoComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Inv DFT", None))
        self.operacjaJednoComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"FFT", None))
        self.operacjaJednoComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Inv FFT", None))
        self.operacjaJednoComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"FCT", None))
        self.operacjaJednoComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Inv FCT", None))
        self.operacjaJednoComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"WHT", None))
        self.operacjaJednoComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Inv WHT", None))

        self.jednoCzestotliwoscProbkowaniaLabel.setText(QCoreApplication.translate("MainWindow", u"Czestotliwosc", None))
        self.bityKwantyzacjiLabel.setText(QCoreApplication.translate("MainWindow", u"Bity kwantyzacji", None))
        self.typRekonstrukcjiLabel.setText(QCoreApplication.translate("MainWindow", u"Typ rekonstrukcji", None))
        self.typRekonstrukcjiComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"zero order", None))
        self.typRekonstrukcjiComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"first order", None))
        self.typRekonstrukcjiComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"sinc", None))

        self.sygnalLabel.setText(QCoreApplication.translate("MainWindow", u"Sygnal", None))
        self.sygnalComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"lewy", None))
        self.sygnalComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"prawy", None))
        self.sygnalComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wynikowy", None))

        self.dzialaniaJednoWykonajButton.setText(QCoreApplication.translate("MainWindow", u"wykonaj", None))
        self.dzialaniaTab.setTabText(self.dzialaniaTab.indexOf(self.dzialaniaJednoSygnaloweTab), QCoreApplication.translate("MainWindow", u"jedno-sygnalowe", None))
        self.dzialaniaDwuWykonajButton.setText(QCoreApplication.translate("MainWindow", u"wykonaj", None))
        self.sygnal1DwuLabel.setText(QCoreApplication.translate("MainWindow", u"Sygnal 1", None))
        self.sygnal1DwuComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"lewy", None))
        self.sygnal1DwuComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"prawy", None))
        self.sygnal1DwuComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wynikowy", None))

        self.sygnal2DwuLabel.setText(QCoreApplication.translate("MainWindow", u"Sygnal 2", None))
        self.sygnal2DwuComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"lewy", None))
        self.sygnal2DwuComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"prawy", None))
        self.sygnal2DwuComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"wynikowy", None))

        self.operacjaDwuLabel.setText(QCoreApplication.translate("MainWindow", u"Operacja", None))
        self.operacjaDwuComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"dodawanie", None))
        self.operacjaDwuComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"odejmowanie", None))
        self.operacjaDwuComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"mno\u017cenie", None))
        self.operacjaDwuComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"dzielenie", None))
        self.operacjaDwuComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"splot", None))
        self.operacjaDwuComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"korelacja", None))

        self.dzialaniaTab.setTabText(self.dzialaniaTab.indexOf(self.dzialaniaDwuSygnaloweTab), QCoreApplication.translate("MainWindow", u"dwu-sygnalowe", None))
        self.menustandard.setTitle(QCoreApplication.translate("MainWindow", u"okno", None))
    # retranslateUi

