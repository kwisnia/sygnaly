# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dystans_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DystansWidget(object):
    def setupUi(self, DystansWidget):
        if not DystansWidget.objectName():
            DystansWidget.setObjectName(u"DystansWidget")
        DystansWidget.resize(800, 880)
        self.czujnikGroupBox = QGroupBox(DystansWidget)
        self.czujnikGroupBox.setObjectName(u"czujnikGroupBox")
        self.czujnikGroupBox.setGeometry(QRect(10, 10, 231, 151))
        self.formLayoutWidget_2 = QWidget(self.czujnikGroupBox)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 19, 214, 118))
        self.czujnikLayout = QFormLayout(self.formLayoutWidget_2)
        self.czujnikLayout.setObjectName(u"czujnikLayout")
        self.czujnikLayout.setVerticalSpacing(12)
        self.czujnikLayout.setContentsMargins(0, 0, 0, 0)
        self.okresSygnaluLabel = QLabel(self.formLayoutWidget_2)
        self.okresSygnaluLabel.setObjectName(u"okresSygnaluLabel")

        self.czujnikLayout.setWidget(0, QFormLayout.LabelRole, self.okresSygnaluLabel)

        self.okresSygnaluDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.okresSygnaluDoubleSpinBox.setObjectName(u"okresSygnaluDoubleSpinBox")
        self.okresSygnaluDoubleSpinBox.setMaximum(100000.000000000000000)

        self.czujnikLayout.setWidget(0, QFormLayout.FieldRole, self.okresSygnaluDoubleSpinBox)

        self.czestotliwoscProbkowaniaLabel = QLabel(self.formLayoutWidget_2)
        self.czestotliwoscProbkowaniaLabel.setObjectName(u"czestotliwoscProbkowaniaLabel")

        self.czujnikLayout.setWidget(1, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel)

        self.czestotliwoscProbkowaniaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.czestotliwoscProbkowaniaDoubleSpinBox.setObjectName(u"czestotliwoscProbkowaniaDoubleSpinBox")
        self.czestotliwoscProbkowaniaDoubleSpinBox.setMaximum(100000.000000000000000)

        self.czujnikLayout.setWidget(1, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox)

        self.dlugoscBuforuLabel = QLabel(self.formLayoutWidget_2)
        self.dlugoscBuforuLabel.setObjectName(u"dlugoscBuforuLabel")

        self.czujnikLayout.setWidget(2, QFormLayout.LabelRole, self.dlugoscBuforuLabel)

        self.dlugoscBuforuDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.dlugoscBuforuDoubleSpinBox.setObjectName(u"dlugoscBuforuDoubleSpinBox")
        self.dlugoscBuforuDoubleSpinBox.setMaximum(100000.000000000000000)

        self.czujnikLayout.setWidget(2, QFormLayout.FieldRole, self.dlugoscBuforuDoubleSpinBox)

        self.okresRaportowaniaLabel = QLabel(self.formLayoutWidget_2)
        self.okresRaportowaniaLabel.setObjectName(u"okresRaportowaniaLabel")

        self.czujnikLayout.setWidget(3, QFormLayout.LabelRole, self.okresRaportowaniaLabel)

        self.okresRaportowaniaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.okresRaportowaniaDoubleSpinBox.setObjectName(u"okresRaportowaniaDoubleSpinBox")
        self.okresRaportowaniaDoubleSpinBox.setMaximum(100000.000000000000000)

        self.czujnikLayout.setWidget(3, QFormLayout.FieldRole, self.okresRaportowaniaDoubleSpinBox)

        self.obiektGroupBox = QGroupBox(DystansWidget)
        self.obiektGroupBox.setObjectName(u"obiektGroupBox")
        self.obiektGroupBox.setGeometry(QRect(250, 10, 211, 151))
        self.formLayoutWidget = QWidget(self.obiektGroupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 190, 118))
        self.obiektLayout = QFormLayout(self.formLayoutWidget)
        self.obiektLayout.setObjectName(u"obiektLayout")
        self.obiektLayout.setVerticalSpacing(12)
        self.obiektLayout.setContentsMargins(0, 0, 0, 0)
        self.jednostkaCzasuLabel = QLabel(self.formLayoutWidget)
        self.jednostkaCzasuLabel.setObjectName(u"jednostkaCzasuLabel")

        self.obiektLayout.setWidget(0, QFormLayout.LabelRole, self.jednostkaCzasuLabel)

        self.jednostkaCzasuDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.jednostkaCzasuDoubleSpinBox.setObjectName(u"jednostkaCzasuDoubleSpinBox")
        self.jednostkaCzasuDoubleSpinBox.setMaximum(100000.000000000000000)

        self.obiektLayout.setWidget(0, QFormLayout.FieldRole, self.jednostkaCzasuDoubleSpinBox)

        self.rzeczywistaPredkoscLabel = QLabel(self.formLayoutWidget)
        self.rzeczywistaPredkoscLabel.setObjectName(u"rzeczywistaPredkoscLabel")

        self.obiektLayout.setWidget(1, QFormLayout.LabelRole, self.rzeczywistaPredkoscLabel)

        self.rzeczywistaPredkoscDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.rzeczywistaPredkoscDoubleSpinBox.setObjectName(u"rzeczywistaPredkoscDoubleSpinBox")
        self.rzeczywistaPredkoscDoubleSpinBox.setMaximum(100000.000000000000000)

        self.obiektLayout.setWidget(1, QFormLayout.FieldRole, self.rzeczywistaPredkoscDoubleSpinBox)

        self.predkoscSygnaluLabel = QLabel(self.formLayoutWidget)
        self.predkoscSygnaluLabel.setObjectName(u"predkoscSygnaluLabel")

        self.obiektLayout.setWidget(2, QFormLayout.LabelRole, self.predkoscSygnaluLabel)

        self.predkoscSygnaluDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.predkoscSygnaluDoubleSpinBox.setObjectName(u"predkoscSygnaluDoubleSpinBox")
        self.predkoscSygnaluDoubleSpinBox.setMaximum(100000.000000000000000)

        self.obiektLayout.setWidget(2, QFormLayout.FieldRole, self.predkoscSygnaluDoubleSpinBox)

        self.dystansOdCzujnikaLabel = QLabel(self.formLayoutWidget)
        self.dystansOdCzujnikaLabel.setObjectName(u"dystansOdCzujnikaLabel")

        self.obiektLayout.setWidget(3, QFormLayout.LabelRole, self.dystansOdCzujnikaLabel)

        self.dystansOdCzujnikaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.dystansOdCzujnikaDoubleSpinBox.setObjectName(u"dystansOdCzujnikaDoubleSpinBox")
        self.dystansOdCzujnikaDoubleSpinBox.setMaximum(100000.000000000000000)

        self.obiektLayout.setWidget(3, QFormLayout.FieldRole, self.dystansOdCzujnikaDoubleSpinBox)

        self.statystykiGroupBox = QGroupBox(DystansWidget)
        self.statystykiGroupBox.setObjectName(u"statystykiGroupBox")
        self.statystykiGroupBox.setGeometry(QRect(470, 10, 241, 151))
        self.verticalLayoutWidget = QWidget(self.statystykiGroupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 221, 121))
        self.statystykiLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.statystykiLayout.setObjectName(u"statystykiLayout")
        self.statystykiLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.statystykiWidget.columnCount() < 1):
            self.statystykiWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.statystykiWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.statystykiWidget.rowCount() < 3):
            self.statystykiWidget.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.statystykiWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.statystykiWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.statystykiWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.statystykiWidget.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.statystykiWidget.setItem(1, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.statystykiWidget.setItem(2, 0, __qtablewidgetitem6)
        self.statystykiWidget.setObjectName(u"statystykiWidget")

        self.statystykiLayout.addWidget(self.statystykiWidget)

        self.wykresyGroupBox = QGroupBox(DystansWidget)
        self.wykresyGroupBox.setObjectName(u"wykresyGroupBox")
        self.wykresyGroupBox.setGeometry(QRect(10, 160, 781, 721))
        self.verticalLayoutWidget_2 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 781, 231))
        self.wykresy1Layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.wykresy1Layout.setObjectName(u"wykresy1Layout")
        self.wykresy1Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 250, 781, 241))
        self.wykresy2Layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.wykresy2Layout.setObjectName(u"wykresy2Layout")
        self.wykresy2Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 490, 781, 231))
        self.wykresy3Layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.wykresy3Layout.setObjectName(u"wykresy3Layout")
        self.wykresy3Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(DystansWidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(710, 119, 81, 41))
        self.startButtonLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.startButtonLayout.setObjectName(u"startButtonLayout")
        self.startButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.startButton = QPushButton(self.verticalLayoutWidget_5)
        self.startButton.setObjectName(u"startButton")

        self.startButtonLayout.addWidget(self.startButton)


        self.retranslateUi(DystansWidget)

        QMetaObject.connectSlotsByName(DystansWidget)
    # setupUi

    def retranslateUi(self, DystansWidget):
        DystansWidget.setWindowTitle(QCoreApplication.translate("DystansWidget", u"Form", None))
        self.czujnikGroupBox.setTitle(QCoreApplication.translate("DystansWidget", u"Czujnik", None))
        self.okresSygnaluLabel.setText(QCoreApplication.translate("DystansWidget", u"Okres sygnalu", None))
        self.czestotliwoscProbkowaniaLabel.setText(QCoreApplication.translate("DystansWidget", u"Czestotliwosc probkowania", None))
        self.dlugoscBuforuLabel.setText(QCoreApplication.translate("DystansWidget", u"Dlugosc buforu", None))
        self.okresRaportowaniaLabel.setText(QCoreApplication.translate("DystansWidget", u"Okres raportowania", None))
        self.obiektGroupBox.setTitle(QCoreApplication.translate("DystansWidget", u"\u015aledzony obiekt", None))
        self.jednostkaCzasuLabel.setText(QCoreApplication.translate("DystansWidget", u"Jednostka czasu", None))
        self.rzeczywistaPredkoscLabel.setText(QCoreApplication.translate("DystansWidget", u"Rzeczywista predkosc", None))
        self.predkoscSygnaluLabel.setText(QCoreApplication.translate("DystansWidget", u"Predkosc sygnalu", None))
        self.dystansOdCzujnikaLabel.setText(QCoreApplication.translate("DystansWidget", u"Dystans od czujnika", None))
        self.statystykiGroupBox.setTitle(QCoreApplication.translate("DystansWidget", u"Statystyki", None))
        ___qtablewidgetitem = self.statystykiWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DystansWidget", u"Warto\u015b\u0107", None));
        ___qtablewidgetitem1 = self.statystykiWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DystansWidget", u"Czas", None));
        ___qtablewidgetitem2 = self.statystykiWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DystansWidget", u"Rzeczywisty dystans", None));
        ___qtablewidgetitem3 = self.statystykiWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("DystansWidget", u"Obliczony dystans", None));

        __sortingEnabled = self.statystykiWidget.isSortingEnabled()
        self.statystykiWidget.setSortingEnabled(False)
        self.statystykiWidget.setSortingEnabled(__sortingEnabled)

        self.wykresyGroupBox.setTitle(QCoreApplication.translate("DystansWidget", u"Wykresy", None))
        self.startButton.setText(QCoreApplication.translate("DystansWidget", u"START", None))
    # retranslateUi

