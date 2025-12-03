# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frontendNjLRsG.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(773, 623)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 779, 601))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ImageWidget = QWidget(self.horizontalLayoutWidget)
        self.ImageWidget.setObjectName(u"ImageWidget")
        self.ImageWidget.setMinimumSize(QSize(512, 512))

        self.horizontalLayout.addWidget(self.ImageWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.comboComport = QComboBox(self.horizontalLayoutWidget)
        self.comboComport.setObjectName(u"comboComport")

        self.verticalLayout_2.addWidget(self.comboComport)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonRefresh = QPushButton(self.horizontalLayoutWidget)
        self.buttonRefresh.setObjectName(u"buttonRefresh")

        self.horizontalLayout_2.addWidget(self.buttonRefresh)

        self.buttonConnect = QPushButton(self.horizontalLayoutWidget)
        self.buttonConnect.setObjectName(u"buttonConnect")

        self.horizontalLayout_2.addWidget(self.buttonConnect)

        self.buttonDisconnect = QPushButton(self.horizontalLayoutWidget)
        self.buttonDisconnect.setObjectName(u"buttonDisconnect")

        self.horizontalLayout_2.addWidget(self.buttonDisconnect)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.comboPixFormat = QComboBox(self.horizontalLayoutWidget)
        self.comboPixFormat.addItem("")
        self.comboPixFormat.addItem("")
        self.comboPixFormat.addItem("")
        self.comboPixFormat.setObjectName(u"comboPixFormat")

        self.verticalLayout_2.addWidget(self.comboPixFormat)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboFramesize = QComboBox(self.horizontalLayoutWidget)
        self.comboFramesize.addItem("")
        self.comboFramesize.setObjectName(u"comboFramesize")

        self.verticalLayout_2.addWidget(self.comboFramesize)

        self.PixelData = QLabel(self.horizontalLayoutWidget)
        self.PixelData.setObjectName(u"PixelData")

        self.verticalLayout_2.addWidget(self.PixelData)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.editFilename = QLineEdit(self.horizontalLayoutWidget)
        self.editFilename.setObjectName(u"editFilename")

        self.verticalLayout_2.addWidget(self.editFilename)

        self.buttonSnapshot = QPushButton(self.horizontalLayoutWidget)
        self.buttonSnapshot.setObjectName(u"buttonSnapshot")

        self.verticalLayout_2.addWidget(self.buttonSnapshot)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"rawImageViewer", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"Comport", None))
        self.buttonRefresh.setText(QCoreApplication.translate("mainWindow", u"Refresh", None))
        self.buttonConnect.setText(QCoreApplication.translate("mainWindow", u"Connect", None))
        self.buttonDisconnect.setText(QCoreApplication.translate("mainWindow", u"Disconnect", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Pixel Format", None))
        self.comboPixFormat.setItemText(0, QCoreApplication.translate("mainWindow", u"PIXFORMAT_RGB565", None))
        self.comboPixFormat.setItemText(1, QCoreApplication.translate("mainWindow", u"PIXFORMAT_GRAYSCALE", None))
        self.comboPixFormat.setItemText(2, QCoreApplication.translate("mainWindow", u"PIXFORMAT_YUV422", None))

        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Framesize", None))
        self.comboFramesize.setItemText(0, QCoreApplication.translate("mainWindow", u"FRAMESIZE_96X96", None))

        self.PixelData.setText("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"Folder", None))
        self.buttonSnapshot.setText(QCoreApplication.translate("mainWindow", u"Snapshot", None))
    # retranslateUi

