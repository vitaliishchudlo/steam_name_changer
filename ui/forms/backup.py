import os
import time

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from selenium.webdriver.common.by import By

from ui.forms.main_window import MainWindow
from ui.forms.popup_window import PopUp
from ui.skeletons.auth import Ui_StartWindow
from web.driver.browser import Browser


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.sign_in_btn.setDisabled(True)
        self.label_error.hide()

        self.refresh_combo_box()

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())
        self.sign_in_btn.clicked.connect(self.authorize)

        self.combo_username.currentIndexChanged.connect(self.combo_check)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def open_main_window(self):
        self.waitauth_popup.hide()
        self.hide()
        self.main = MainWindow(self.browser)
        self.main.show()

    def sign_up(self):
        while self.browser.driver.current_url == 'https://store.steampowered.com/login/':
            print('Waiting authorization...')
            time.sleep(1)
        self.label_title_settext('Checking your account...')
        if not self.browser.driver.current_url == 'https://store.steampowered.com/':
            print('User entered other page')
            return self.waitauth_popup.close()
        print('Trying to check that user is logged in')
        if self.browser.auth_status():
            self.waitauth_popup.label_title_settext('Successfully authorized')
            self.waitauth_popup.label_gif.setPixmap(
                QtGui.QPixmap('ui/icons/custom/done.png'))
            return True
        else:
            self.waitauth_popup.label_title_settext('ERROR When signing up')
            self.waitauth_popup.label_gif.setPixmap(QtGui.QPixmap(
                'ui/icons/custom/icons8-close.svg'))
            time.sleep(1.5)
            return False

    def authorize(self):
        self.setDisabled(True)
        self.waitauth_popup = PopUp()
        self.waitauth_popup.show()
        # Sign up
        if self.combo_username.currentText() == 'Add a new account...':
            self.browser = Browser()
            self.browser.get_steam()
            if not self.sign_up():
                return self.waitauth_popup.close()
            account_name = self.browser.driver.find_element(
                By.CLASS_NAME, 'pageheader.youraccount_pageheader').text
            account_name = account_name[account_name.find(' ') + 1:].lower()
            self.browser.save_cookies(account_name)
            self.browser.driver.close()
            self.label_title_settext('Please, wait....')
            if not self.sign_in(account_name):
                self.browser.driver.close()
                self.label_error.setText(
                    f'Can`t sign in to account {account_name}')
                return self.close_wait_auth()
            return self.open_main_window()
        else:
            # Sign in
            pass

        self.wait_user_sign_in()

    def close_wait_auth(self):
        self.browser.quit()
        self.setDisabled(False)
        self.waitauth_popup.hide()

    def combo_check(self):
        if self.combo_username.currentText() == '':
            return self.sign_in_btn.setDisabled(True)
        return self.sign_in_btn.setDisabled(False)

    def refresh_combo_box(self):
        pklfiles = []
        for file in os.listdir('web/cookies'):
            pklfiles.append(file[:-4])
        for pklfile in pklfiles:
            self.combo_username.addItem(pklfile)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# import threading
# import time
#
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QMovie
# from selenium.webdriver.common.by import By
#
# from ui.forms.main_window import MainWindow
# from ui.skeletons.wait_auth import Ui_WaitAuthWindow
# from web.driver.browser import Browser
#
#
# class PopUp(QtWidgets.QMainWindow, Ui_WaitAuthWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.center()
#
#         # self.setWindowFlags(Qt.FramelessWindowHint)
#         # self.previous_window = previous_window
#         #
#         # self.btn_close.clicked.connect(self.close)
#         #
#         # self.label_gif.setMinimumSize(QtCore.QSize(25, 25))
#         # self.label_gif.setMaximumSize(QtCore.QSize(25, 25))
#         # self.label_gif.setScaledContents(True)
#         #
#         # self.loading = QMovie('ui/gifs/loading.gif')
#         # self.label_gif.setMovie(self.loading)
#         #
#         # self.startAnimation()
#         #
#         # def moveWindow(event):
#         #     if event.buttons() == Qt.LeftButton:
#         #         self.move(self.pos() + event.globalPos() - self.dragPos)
#         #         self.dragPos = event.globalPos()
#         #         self.setCursor(Qt.ArrowCursor)
#         #
#         # self.title_bar.mouseMoveEvent = moveWindow
#
#     #
#     #
#     #
#     # def sign_in(self, account_name):
#     #     self.browser = Browser(hide=True)
#     #     self.browser.get_steam()
#     #     self.browser.load_cookies(account_name)
#     #     self.browser.refresh()
#     #     return bool(self.browser.auth_status())
#     #
#     # def sign_up(self):
#     #     while self.browser.driver.current_url == 'https://store.steampowered.com/login/':
#     #         print('Waiting authorization...')
#     #         time.sleep(1)
#     #     self.label_title_settext('Checking your account...')
#     #     if not self.browser.driver.current_url == 'https://store.steampowered.com/':
#     #         print('User entered other page')
#     #         return self.close()
#     #     print('Trying to check that user is logged in')
#     #     if self.browser.auth_status():
#     #         self.label_title_settext('Successfully authorized')
#     #         self.label_gif.setPixmap(
#     #             QtGui.QPixmap('ui/icons/custom/done.png'))
#     #         return True
#     #     else:
#     #         self.label_title_settext('ERROR')
#     #         self.label_gif.setPixmap(QtGui.QPixmap(
#     #             'ui/icons/custom/icons8-close.svg'))
#     #         time.sleep(3)
#     #         return False
#     #
#     # def check_authorization(self):
#     #     # If it is sign up
#     #     if self.previous_window.combo_username.currentText() == 'Add a new account...':
#     #         self.browser = Browser()
#     #         self.browser.get_steam()
#     #         if not self.sign_up():
#     #             return self.close()
#     #         account_name = self.browser.driver.find_element(
#     #             By.CLASS_NAME, 'pageheader.youraccount_pageheader').text
#     #         account_name = account_name[account_name.find(' ') + 1:].lower()
#     #         self.browser.save_cookies(account_name)
#     #         self.browser.driver.close()
#     #         self.label_title_settext('Please, wait....')
#     #         if not self.sign_in(account_name):
#     #             self.browser.driver.close()
#     #             self.previous_window.label_error.setText(
#     #                 f'Can`t sign in to account {account_name}')
#     #             return self.close()
#     #         return self.next_window()
#     #     # If it is sign in
#     #     account_name = self.previous_window.combo_username.currentText()
#     #     self.label_title_settext(
#     #         f'Authorization in the {account_name} account...')
#     #     self.browser = Browser(hide=True)
#     #     self.browser.get_steam()
#     #     self.browser.load_cookies(account_name)
#     #     self.browser.refresh()
#     #     if not self.browser.auth_status():
#     #         self.browser.driver.close()
#     #         self.browser = Browser()
#     #         self.browser.get_steam()
#     #         if not self.sign_up():
#     #             self.browser.driver.close()
#     #             self.previous_window.label_error.setText(
#     #                 f'Can`t sign in to account {account_name}')
#     #             return self.close()
#     #         self.browser.save_cookies(account_name)
#     #         self.browser.driver.close()
#     #         self.check_authorization()
#     #     return self.next_window()
#     #
#     # def startAnimation(self):
#     #     self.loading.start()
#     #
#     # def mousePressEvent(self, event):
#     #     self.dragPos = event.globalPos()
#     #
#     # def next_window(self):
#     #     self.previous_window.hide()
#     #     self.main = MainWindow(self.browser)
#     #     self.main.show()
#     #     self.hide()
#     #
#     # def close(self):
#     #     self.browser.quit()
#     #     self.previous_window.setDisabled(False)
#     #     self.hide()
#     #
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QtWidgets.QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#     def label_title_settext(self, message):
#         self._translate = QtCore.QCoreApplication.translate
#         self.label_title.setText(self._translate('WaitAuthWindow',
#                                                  f"""<html><head/><body><p align=\"center\"><span style=\"
#                                                  font-size:14pt; font-weight:600;\">{message}
#                                                  </span></p></body></html>"""))
