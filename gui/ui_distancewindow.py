# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dystans_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_DystansWidget(object):
    def setupUi(self, DystansWidget):
        if not DystansWidget.objectName():
            DystansWidget.setObjectName("DystansWidget")
        DystansWidget.resize(800, 880)
        self.czujnikGroupBox = QGroupBox(DystansWidget)
        self.czujnikGroupBox.setObjectName("czujnikGroupBox")
        self.czujnikGroupBox.setGeometry(QRect(10, 10, 211, 151))
        self.formLayoutWidget_2 = QWidget(self.czujnikGroupBox)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 19, 191, 118))
        self.czujnikLayout = QFormLayout(self.formLayoutWidget_2)
        self.czujnikLayout.setObjectName("czujnikLayout")
        self.czujnikLayout.setVerticalSpacing(12)
        self.czujnikLayout.setContentsMargins(0, 0, 0, 0)
        self.okresSygnaluLabel = QLabel(self.formLayoutWidget_2)
        self.okresSygnaluLabel.setObjectName("okresSygnaluLabel")

        self.czujnikLayout.setWidget(0, QFormLayout.LabelRole, self.okresSygnaluLabel)

        self.okresSygnaluDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.okresSygnaluDoubleSpinBox.setObjectName("okresSygnaluDoubleSpinBox")

        self.czujnikLayout.setWidget(
            0, QFormLayout.FieldRole, self.okresSygnaluDoubleSpinBox
        )

        self.czestotliwoscProbkowaniaLabel = QLabel(self.formLayoutWidget_2)
        self.czestotliwoscProbkowaniaLabel.setObjectName(
            "czestotliwoscProbkowaniaLabel"
        )

        self.czujnikLayout.setWidget(
            1, QFormLayout.LabelRole, self.czestotliwoscProbkowaniaLabel
        )

        self.czestotliwoscProbkowaniaDoubleSpinBox = QDoubleSpinBox(
            self.formLayoutWidget_2
        )
        self.czestotliwoscProbkowaniaDoubleSpinBox.setObjectName(
            "czestotliwoscProbkowaniaDoubleSpinBox"
        )

        self.czujnikLayout.setWidget(
            1, QFormLayout.FieldRole, self.czestotliwoscProbkowaniaDoubleSpinBox
        )

        self.dlugoscBuforuLabel = QLabel(self.formLayoutWidget_2)
        self.dlugoscBuforuLabel.setObjectName("dlugoscBuforuLabel")

        self.czujnikLayout.setWidget(2, QFormLayout.LabelRole, self.dlugoscBuforuLabel)

        self.dlugoscBuforuDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.dlugoscBuforuDoubleSpinBox.setObjectName("dlugoscBuforuDoubleSpinBox")

        self.czujnikLayout.setWidget(
            2, QFormLayout.FieldRole, self.dlugoscBuforuDoubleSpinBox
        )

        self.okresRaportowaniaLabel = QLabel(self.formLayoutWidget_2)
        self.okresRaportowaniaLabel.setObjectName("okresRaportowaniaLabel")

        self.czujnikLayout.setWidget(
            3, QFormLayout.LabelRole, self.okresRaportowaniaLabel
        )

        self.okresRaportowaniaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget_2)
        self.okresRaportowaniaDoubleSpinBox.setObjectName(
            "okresRaportowaniaDoubleSpinBox"
        )

        self.czujnikLayout.setWidget(
            3, QFormLayout.FieldRole, self.okresRaportowaniaDoubleSpinBox
        )

        self.obiektGroupBox = QGroupBox(DystansWidget)
        self.obiektGroupBox.setObjectName("obiektGroupBox")
        self.obiektGroupBox.setGeometry(QRect(230, 10, 181, 151))
        self.formLayoutWidget = QWidget(self.obiektGroupBox)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 166, 118))
        self.obiektLayout = QFormLayout(self.formLayoutWidget)
        self.obiektLayout.setObjectName("obiektLayout")
        self.obiektLayout.setVerticalSpacing(12)
        self.obiektLayout.setContentsMargins(0, 0, 0, 0)
        self.jednostkaCzasuLabel = QLabel(self.formLayoutWidget)
        self.jednostkaCzasuLabel.setObjectName("jednostkaCzasuLabel")

        self.obiektLayout.setWidget(0, QFormLayout.LabelRole, self.jednostkaCzasuLabel)

        self.jednostkaCzasuDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.jednostkaCzasuDoubleSpinBox.setObjectName("jednostkaCzasuDoubleSpinBox")

        self.obiektLayout.setWidget(
            0, QFormLayout.FieldRole, self.jednostkaCzasuDoubleSpinBox
        )

        self.rzeczywistaPredkoscLabel = QLabel(self.formLayoutWidget)
        self.rzeczywistaPredkoscLabel.setObjectName("rzeczywistaPredkoscLabel")

        self.obiektLayout.setWidget(
            1, QFormLayout.LabelRole, self.rzeczywistaPredkoscLabel
        )

        self.rzeczywistaPredkoscDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.rzeczywistaPredkoscDoubleSpinBox.setObjectName(
            "rzeczywistaPredkoscDoubleSpinBox"
        )

        self.obiektLayout.setWidget(
            1, QFormLayout.FieldRole, self.rzeczywistaPredkoscDoubleSpinBox
        )

        self.predkoscSygnaluLabel = QLabel(self.formLayoutWidget)
        self.predkoscSygnaluLabel.setObjectName("predkoscSygnaluLabel")

        self.obiektLayout.setWidget(2, QFormLayout.LabelRole, self.predkoscSygnaluLabel)

        self.predkoscSygnaluDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.predkoscSygnaluDoubleSpinBox.setObjectName("predkoscSygnaluDoubleSpinBox")

        self.obiektLayout.setWidget(
            2, QFormLayout.FieldRole, self.predkoscSygnaluDoubleSpinBox
        )

        self.dystansOdCzujnikaLabel = QLabel(self.formLayoutWidget)
        self.dystansOdCzujnikaLabel.setObjectName("dystansOdCzujnikaLabel")

        self.obiektLayout.setWidget(
            3, QFormLayout.LabelRole, self.dystansOdCzujnikaLabel
        )

        self.dystansOdCzujnikaDoubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.dystansOdCzujnikaDoubleSpinBox.setObjectName(
            "dystansOdCzujnikaDoubleSpinBox"
        )

        self.obiektLayout.setWidget(
            3, QFormLayout.FieldRole, self.dystansOdCzujnikaDoubleSpinBox
        )

        self.statystykiGroupBox = QGroupBox(DystansWidget)
        self.statystykiGroupBox.setObjectName("statystykiGroupBox")
        self.statystykiGroupBox.setGeometry(QRect(420, 10, 251, 151))
        self.verticalLayoutWidget = QWidget(self.statystykiGroupBox)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 231, 121))
        self.statystykiLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.statystykiLayout.setObjectName("statystykiLayout")
        self.statystykiLayout.setContentsMargins(0, 0, 0, 0)
        self.statystykiWidget = QTableWidget(self.verticalLayoutWidget)
        if self.statystykiWidget.columnCount() < 1:
            self.statystykiWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.statystykiWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if self.statystykiWidget.rowCount() < 3:
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
        self.statystykiWidget.setObjectName("statystykiWidget")

        self.statystykiLayout.addWidget(self.statystykiWidget)

        self.wykresyGroupBox = QGroupBox(DystansWidget)
        self.wykresyGroupBox.setObjectName("wykresyGroupBox")
        self.wykresyGroupBox.setGeometry(QRect(10, 170, 781, 711))
        self.verticalLayoutWidget_2 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 781, 241))
        self.wykresy1Layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.wykresy1Layout.setObjectName("wykresy1Layout")
        self.wykresy1Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 240, 781, 241))
        self.wykresy2Layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.wykresy2Layout.setObjectName("wykresy2Layout")
        self.wykresy2Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4 = QWidget(self.wykresyGroupBox)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 480, 781, 231))
        self.wykresy3Layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.wykresy3Layout.setObjectName("wykresy3Layout")
        self.wykresy3Layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(DystansWidget)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(690, 119, 91, 41))
        self.startButtonLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.startButtonLayout.setObjectName("startButtonLayout")
        self.startButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.startButton = QPushButton(self.verticalLayoutWidget_5)
        self.startButton.setObjectName("startButton")

        self.startButtonLayout.addWidget(self.startButton)

        self.retranslateUi(DystansWidget)

        QMetaObject.connectSlotsByName(DystansWidget)

    # setupUi

    def retranslateUi(self, DystansWidget):
        DystansWidget.setWindowTitle(
            QCoreApplication.translate("DystansWidget", "Form", None)
        )
        self.czujnikGroupBox.setTitle(
            QCoreApplication.translate("DystansWidget", "Czujnik", None)
        )
        self.okresSygnaluLabel.setText(
            QCoreApplication.translate("DystansWidget", "Okres sygnalu", None)
        )
        self.czestotliwoscProbkowaniaLabel.setText(
            QCoreApplication.translate(
                "DystansWidget", "Czestotliwosc probkowania", None
            )
        )
        self.dlugoscBuforuLabel.setText(
            QCoreApplication.translate("DystansWidget", "Dlugosc buforu", None)
        )
        self.okresRaportowaniaLabel.setText(
            QCoreApplication.translate("DystansWidget", "Okres raportowania", None)
        )
        self.obiektGroupBox.setTitle(
            QCoreApplication.translate("DystansWidget", "\u015aledzony obiekt", None)
        )
        self.jednostkaCzasuLabel.setText(
            QCoreApplication.translate("DystansWidget", "Jednostka czasu", None)
        )
        self.rzeczywistaPredkoscLabel.setText(
            QCoreApplication.translate("DystansWidget", "Rzeczywista predkosc", None)
        )
        self.predkoscSygnaluLabel.setText(
            QCoreApplication.translate("DystansWidget", "Predkosc sygnalu", None)
        )
        self.dystansOdCzujnikaLabel.setText(
            QCoreApplication.translate("DystansWidget", "Dystans od czujnika", None)
        )
        self.statystykiGroupBox.setTitle(
            QCoreApplication.translate("DystansWidget", "Statystyki", None)
        )
        ___qtablewidgetitem = self.statystykiWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("DystansWidget", "Warto\u015b\u0107", None)
        )
        ___qtablewidgetitem1 = self.statystykiWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("DystansWidget", "Czas", None)
        )
        ___qtablewidgetitem2 = self.statystykiWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("DystansWidget", "Rzeczywisty dystans", None)
        )
        ___qtablewidgetitem3 = self.statystykiWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("DystansWidget", "Obliczony dystans", None)
        )

        __sortingEnabled = self.statystykiWidget.isSortingEnabled()
        self.statystykiWidget.setSortingEnabled(False)
        self.statystykiWidget.setSortingEnabled(__sortingEnabled)

        self.wykresyGroupBox.setTitle(
            QCoreApplication.translate("DystansWidget", "Wykresy", None)
        )
        self.startButton.setText(
            QCoreApplication.translate("DystansWidget", "START", None)
        )

    # retranslateUi
