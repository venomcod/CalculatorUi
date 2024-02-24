# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/round_calculate_black_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color:white;\n"
"    background-color: #121212;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lb_temp = QLabel(self.centralwidget)
        self.lb_temp.setObjectName(u"lb_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_temp.sizePolicy().hasHeightForWidth())
        self.lb_temp.setSizePolicy(sizePolicy)
        self.lb_temp.setStyleSheet(u"color: #888;")
        self.lb_temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lb_temp)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none; ")
        self.le_entry.setMaxLength(10)
        self.le_entry.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.layout_btn = QGridLayout()
        self.layout_btn.setObjectName(u"layout_btn")
        self.bt_suc = QPushButton(self.centralwidget)
        self.bt_suc.setObjectName(u"bt_suc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_suc.sizePolicy().hasHeightForWidth())
        self.bt_suc.setSizePolicy(sizePolicy2)
        self.bt_suc.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_suc, 4, 3, 1, 1)

        self.bt_4 = QPushButton(self.centralwidget)
        self.bt_4.setObjectName(u"bt_4")
        sizePolicy2.setHeightForWidth(self.bt_4.sizePolicy().hasHeightForWidth())
        self.bt_4.setSizePolicy(sizePolicy2)
        self.bt_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_4.setMouseTracking(True)

        self.layout_btn.addWidget(self.bt_4, 2, 0, 1, 1)

        self.bt_shdel = QPushButton(self.centralwidget)
        self.bt_shdel.setObjectName(u"bt_shdel")
        sizePolicy2.setHeightForWidth(self.bt_shdel.sizePolicy().hasHeightForWidth())
        self.bt_shdel.setSizePolicy(sizePolicy2)
        self.bt_shdel.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/round_backspace_white_24dp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_shdel.setIcon(icon1)
        self.bt_shdel.setIconSize(QSize(24, 24))

        self.layout_btn.addWidget(self.bt_shdel, 0, 2, 1, 1)

        self.bt_6 = QPushButton(self.centralwidget)
        self.bt_6.setObjectName(u"bt_6")
        sizePolicy2.setHeightForWidth(self.bt_6.sizePolicy().hasHeightForWidth())
        self.bt_6.setSizePolicy(sizePolicy2)
        self.bt_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_6, 2, 2, 1, 1)

        self.bt_minus = QPushButton(self.centralwidget)
        self.bt_minus.setObjectName(u"bt_minus")
        sizePolicy2.setHeightForWidth(self.bt_minus.sizePolicy().hasHeightForWidth())
        self.bt_minus.setSizePolicy(sizePolicy2)
        self.bt_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_minus, 2, 3, 1, 1)

        self.bt_cath = QPushButton(self.centralwidget)
        self.bt_cath.setObjectName(u"bt_cath")
        sizePolicy2.setHeightForWidth(self.bt_cath.sizePolicy().hasHeightForWidth())
        self.bt_cath.setSizePolicy(sizePolicy2)
        self.bt_cath.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_cath, 0, 3, 1, 1)

        self.bt_proz = QPushButton(self.centralwidget)
        self.bt_proz.setObjectName(u"bt_proz")
        sizePolicy2.setHeightForWidth(self.bt_proz.sizePolicy().hasHeightForWidth())
        self.bt_proz.setSizePolicy(sizePolicy2)
        self.bt_proz.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_proz, 1, 3, 1, 1)

        self.bt_7 = QPushButton(self.centralwidget)
        self.bt_7.setObjectName(u"bt_7")
        sizePolicy2.setHeightForWidth(self.bt_7.sizePolicy().hasHeightForWidth())
        self.bt_7.setSizePolicy(sizePolicy2)
        self.bt_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_7, 1, 0, 1, 1)

        self.bt_ce = QPushButton(self.centralwidget)
        self.bt_ce.setObjectName(u"bt_ce")
        sizePolicy2.setHeightForWidth(self.bt_ce.sizePolicy().hasHeightForWidth())
        self.bt_ce.setSizePolicy(sizePolicy2)
        self.bt_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_ce, 0, 1, 1, 1)

        self.bt_9 = QPushButton(self.centralwidget)
        self.bt_9.setObjectName(u"bt_9")
        sizePolicy2.setHeightForWidth(self.bt_9.sizePolicy().hasHeightForWidth())
        self.bt_9.setSizePolicy(sizePolicy2)
        self.bt_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_9, 1, 2, 1, 1)

        self.bt_3 = QPushButton(self.centralwidget)
        self.bt_3.setObjectName(u"bt_3")
        sizePolicy2.setHeightForWidth(self.bt_3.sizePolicy().hasHeightForWidth())
        self.bt_3.setSizePolicy(sizePolicy2)
        self.bt_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_3, 3, 2, 1, 1)

        self.bt_c = QPushButton(self.centralwidget)
        self.bt_c.setObjectName(u"bt_c")
        sizePolicy2.setHeightForWidth(self.bt_c.sizePolicy().hasHeightForWidth())
        self.bt_c.setSizePolicy(sizePolicy2)
        self.bt_c.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_c, 0, 0, 1, 1)

        self.bt_5 = QPushButton(self.centralwidget)
        self.bt_5.setObjectName(u"bt_5")
        sizePolicy2.setHeightForWidth(self.bt_5.sizePolicy().hasHeightForWidth())
        self.bt_5.setSizePolicy(sizePolicy2)
        self.bt_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_5, 2, 1, 1, 1)

        self.bt_point = QPushButton(self.centralwidget)
        self.bt_point.setObjectName(u"bt_point")
        sizePolicy2.setHeightForWidth(self.bt_point.sizePolicy().hasHeightForWidth())
        self.bt_point.setSizePolicy(sizePolicy2)
        self.bt_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_point, 4, 2, 1, 1)

        self.bt_false = QPushButton(self.centralwidget)
        self.bt_false.setObjectName(u"bt_false")
        sizePolicy2.setHeightForWidth(self.bt_false.sizePolicy().hasHeightForWidth())
        self.bt_false.setSizePolicy(sizePolicy2)
        self.bt_false.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_false, 4, 0, 1, 1)

        self.bt_1 = QPushButton(self.centralwidget)
        self.bt_1.setObjectName(u"bt_1")
        sizePolicy2.setHeightForWidth(self.bt_1.sizePolicy().hasHeightForWidth())
        self.bt_1.setSizePolicy(sizePolicy2)
        self.bt_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_1, 3, 0, 1, 1)

        self.bt_plus = QPushButton(self.centralwidget)
        self.bt_plus.setObjectName(u"bt_plus")
        sizePolicy2.setHeightForWidth(self.bt_plus.sizePolicy().hasHeightForWidth())
        self.bt_plus.setSizePolicy(sizePolicy2)
        self.bt_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_plus, 3, 3, 1, 1)

        self.bt_2 = QPushButton(self.centralwidget)
        self.bt_2.setObjectName(u"bt_2")
        sizePolicy2.setHeightForWidth(self.bt_2.sizePolicy().hasHeightForWidth())
        self.bt_2.setSizePolicy(sizePolicy2)
        self.bt_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_2, 3, 1, 1, 1)

        self.bt_8 = QPushButton(self.centralwidget)
        self.bt_8.setObjectName(u"bt_8")
        sizePolicy2.setHeightForWidth(self.bt_8.sizePolicy().hasHeightForWidth())
        self.bt_8.setSizePolicy(sizePolicy2)
        self.bt_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_8, 1, 1, 1, 1)

        self.bt_0 = QPushButton(self.centralwidget)
        self.bt_0.setObjectName(u"bt_0")
        sizePolicy2.setHeightForWidth(self.bt_0.sizePolicy().hasHeightForWidth())
        self.bt_0.setSizePolicy(sizePolicy2)
        self.bt_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_btn.addWidget(self.bt_0, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.layout_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator by DaNk", None))
        self.lb_temp.setText("")
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bt_suc.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.bt_suc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.bt_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.bt_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.bt_shdel.setText("")
#if QT_CONFIG(shortcut)
        self.bt_shdel.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.bt_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.bt_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.bt_minus.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
#if QT_CONFIG(shortcut)
        self.bt_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.bt_cath.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.bt_cath.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.bt_proz.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.bt_proz.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.bt_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.bt_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.bt_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
#if QT_CONFIG(shortcut)
        self.bt_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.bt_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.bt_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.bt_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.bt_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.bt_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.bt_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.bt_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.bt_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.bt_point.setShortcut(QCoreApplication.translate("MainWindow", u"\u042e, .", None))
#endif // QT_CONFIG(shortcut)
        self.bt_false.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.bt_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.bt_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.bt_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.bt_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.bt_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.bt_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.bt_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.bt_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.bt_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.bt_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

