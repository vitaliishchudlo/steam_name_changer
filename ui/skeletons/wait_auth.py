# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_forms/wait_auth.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WaitAuthWindow(object):
    def setupUi(self, WaitAuthWindow):
        WaitAuthWindow.setObjectName('WaitAuthWindow')
        WaitAuthWindow.resize(406, 136)
        WaitAuthWindow.setStyleSheet('')
        self.centralwidget = QtWidgets.QWidget(WaitAuthWindow)
        self.centralwidget.setStyleSheet('')
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.title_bar = QtWidgets.QFrame(self.centralwidget)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title_bar.setStyleSheet('QFrame {\n'
                                     '    border:none;\n'
                                     '    \n'
                                     '    background-color: rgb(85, 87, 83);\n'
                                     '}\n'
                                     '')
        self.title_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_bar.setObjectName('title_bar')
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.frame_title = QtWidgets.QFrame(self.title_bar)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName('frame_title')
        self.gridLayout = QtWidgets.QGridLayout(self.frame_title)
        self.gridLayout.setObjectName('gridLayout')
        self.window_name = QtWidgets.QLabel(self.frame_title)
        self.window_name.setStyleSheet("font: 75 11pt \"Ubuntu Mono\";")
        self.window_name.setObjectName('window_name')
        self.gridLayout.addWidget(
            self.window_name, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.frame_title)
        self.frame_btns = QtWidgets.QFrame(self.title_bar)
        self.frame_btns.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName('frame_btns')
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.btn_close = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_close.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_close.setStyleSheet('QPushButton {\n'
                                     '    border: none;\n'
                                     '    border-radius: 10px;\n'
                                     '    background-color: rgb(204, 0, 0);\n'
                                     '    border-style: solid;\n'
                                     '    border-color: rgb(0, 0, 0);\n'
                                     '    border-width: 1px;\n'
                                     '}\n'
                                     'QPushButton:hover {\n'
                                     '    background-color: rgb(164, 0, 0);\n'
                                     '}')
        self.btn_close.setText('')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ':/custom/custom/icons8-close.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setObjectName('btn_close')
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.horizontalLayout_2.addWidget(self.frame_btns)
        self.verticalLayout.addWidget(self.title_bar)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setStyleSheet('QFrame {\n'
                                '    border:none;\n'
                                '    background-color: rgb(186, 189, 182);\n'
                                '}\n'
                                '')
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName('body')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.title = QtWidgets.QFrame(self.body)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName('title')
        self.gridLayout_2 = QtWidgets.QGridLayout(self.title)
        self.gridLayout_2.setObjectName('gridLayout_2')
        self.label_title = QtWidgets.QLabel(self.title)
        self.label_title.setObjectName('label_title')
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.title)
        self.status = QtWidgets.QFrame(self.body)
        self.status.setStyleSheet('QFrame {\n'
                                  '    border:none;\n'
                                  '}\n'
                                  '')
        self.status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status.setObjectName('status')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.status)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.text = QtWidgets.QFrame(self.status)
        self.text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text.setObjectName('text')
        self.horizontalLayout.addWidget(self.text)
        self.gif = QtWidgets.QFrame(self.status)
        self.gif.setStyleSheet('QFrame {\n'
                               '    border:none;\n'
                               '\n'
                               '}\n'
                               '')
        self.gif.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gif.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gif.setObjectName('gif')
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gif)
        self.gridLayout_3.setObjectName('gridLayout_3')
        self.label_gif = QtWidgets.QLabel(self.gif)
        self.label_gif.setScaledContents(True)
        self.label_gif.setObjectName('label_gif')
        self.gridLayout_3.addWidget(
            self.label_gif, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.gif)
        self.right = QtWidgets.QFrame(self.status)
        self.right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName('right')
        self.horizontalLayout.addWidget(self.right)
        self.verticalLayout_2.addWidget(self.status)
        self.verticalLayout.addWidget(self.body)
        WaitAuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WaitAuthWindow)
        QtCore.QMetaObject.connectSlotsByName(WaitAuthWindow)

    def retranslateUi(self, WaitAuthWindow):
        _translate = QtCore.QCoreApplication.translate
        WaitAuthWindow.setWindowTitle(
            _translate('WaitAuthWindow', 'MainWindow'))
        self.window_name.setText(_translate(
            'WaitAuthWindow', "<html><head/><body><p><span style=\" font-weight:600;\">Authorization</span></p></body></html>"))
        self.label_title.setText(_translate(
            'WaitAuthWindow', "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">You need to log in to your steam account</span></p></body></html>"))
        self.label_gif.setText(_translate('WaitAuthWindow', '.'))
