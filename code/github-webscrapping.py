#! /usr/bin/python3
#
# GitHub WebScrapping - github-webscrapping
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/github-webscrapping/
#
# - Do not modify if you don't know what you're doing -
#
# -----------------------------------------------------------------------------------


# Import modules:
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import json
import argparse
import webbrowser
import requests
import subprocess
import os
import sys


# Prints the version if the --version argument is passed:
parser = argparse.ArgumentParser()
parser.add_argument('--version', action='store_true', help='Show the version')
args = parser.parse_args()

if args.version:
    print('github-webscrapping 1.0.0')
    sys.exit()
    

# Class MainWindow:
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 726)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 726))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 726))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/github-webscrapping/icons/github-webscrapping.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainpage = QtWidgets.QWidget()
        self.mainpage.setObjectName("mainpage")
        self.label = QtWidgets.QLabel(self.mainpage)
        self.label.setGeometry(QtCore.QRect(320, 10, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.mainpage)
        self.groupBox.setGeometry(QtCore.QRect(660, 110, 331, 281))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 291, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.search_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 2, 1, 1, 1)
        self.profile_line_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.profile_line_edit.setObjectName("profile_line_edit")
        self.gridLayout.addWidget(self.profile_line_edit, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.saveprofile_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.saveprofile_checkBox.setGeometry(QtCore.QRect(20, 110, 291, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveprofile_checkBox.sizePolicy().hasHeightForWidth())
        self.saveprofile_checkBox.setSizePolicy(sizePolicy)
        self.saveprofile_checkBox.setChecked(False)
        self.saveprofile_checkBox.setObjectName("saveprofile_checkBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 150, 291, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.savedprofiles_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.savedprofiles_comboBox.setObjectName("savedprofiles_comboBox")
        self.horizontalLayout.addWidget(self.savedprofiles_comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 200, 291, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.autofillprofile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.autofillprofile_button.setObjectName("autofillprofile_button")
        self.horizontalLayout_2.addWidget(self.autofillprofile_button)
        self.deleteprofile_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.deleteprofile_button.setObjectName("deleteprofile_button")
        self.horizontalLayout_2.addWidget(self.deleteprofile_button)
        self.groupBox_2 = QtWidgets.QGroupBox(self.mainpage)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 410, 331, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 40, 291, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.sort_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.sort_comboBox.setObjectName("sort_comboBox")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.sort_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.sort_comboBox)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 90, 291, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.typeaccount_comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.typeaccount_comboBox.setObjectName("typeaccount_comboBox")
        self.typeaccount_comboBox.addItem("")
        self.typeaccount_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.typeaccount_comboBox)
        self.githubimage_label_2 = QtWidgets.QLabel(self.mainpage)
        self.githubimage_label_2.setGeometry(QtCore.QRect(40, 180, 581, 401))
        self.githubimage_label_2.setText("")
        self.githubimage_label_2.setPixmap(QtGui.QPixmap("/usr/share/github-webscrapping/screenshots/Screenshot_2.png"))
        self.githubimage_label_2.setScaledContents(True)
        self.githubimage_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.githubimage_label_2.setObjectName("githubimage_label_2")
        self.githubimage_label_4 = QtWidgets.QLabel(self.mainpage)
        self.githubimage_label_4.setGeometry(QtCore.QRect(260, 10, 71, 71))
        self.githubimage_label_4.setText("")
        self.githubimage_label_4.setPixmap(QtGui.QPixmap("/usr/share/github-webscrapping/icons/github-webscrapping.svg"))
        self.githubimage_label_4.setScaledContents(True)
        self.githubimage_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.githubimage_label_4.setObjectName("githubimage_label_4")
        self.label_4 = QtWidgets.QLabel(self.mainpage)
        self.label_4.setGeometry(QtCore.QRect(40, 127, 581, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.mainpage)
        self.github_profile_window = QtWidgets.QWidget()
        self.github_profile_window.setObjectName("github_profile_window")
        self.groupBox_3 = QtWidgets.QGroupBox(self.github_profile_window)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 10, 601, 331))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.github_profile_window)
        self.groupBox_4.setGeometry(QtCore.QRect(430, 350, 601, 271))
        self.groupBox_4.setObjectName("groupBox_4")
        self.title_repositories_label = QtWidgets.QLabel(self.groupBox_4)
        self.title_repositories_label.setGeometry(QtCore.QRect(20, 30, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_repositories_label.setFont(font)
        self.title_repositories_label.setObjectName("title_repositories_label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 80, 101, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_3.addWidget(self.label_18)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(130, 80, 331, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.language_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.language_label.setFont(font)
        self.language_label.setText("")
        self.language_label.setObjectName("language_label")
        self.verticalLayout_4.addWidget(self.language_label)
        self.stars_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.stars_label.setFont(font)
        self.stars_label.setText("")
        self.stars_label.setObjectName("stars_label")
        self.verticalLayout_4.addWidget(self.stars_label)
        self.license_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.license_label.setFont(font)
        self.license_label.setText("")
        self.license_label.setObjectName("license_label")
        self.verticalLayout_4.addWidget(self.license_label)
        self.updated_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.updated_label.setFont(font)
        self.updated_label.setText("")
        self.updated_label.setObjectName("updated_label")
        self.verticalLayout_4.addWidget(self.updated_label)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(480, 80, 101, 171))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.web_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.web_button.setObjectName("web_button")
        self.verticalLayout_5.addWidget(self.web_button)
        self.clone_button = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.clone_button.setObjectName("clone_button")
        self.verticalLayout_5.addWidget(self.clone_button)
        self.groupBox_5 = QtWidgets.QGroupBox(self.github_profile_window)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 10, 381, 611))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 574))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.profile_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.profile_label.setGeometry(QtCore.QRect(20, 10, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.profile_label.setFont(font)
        self.profile_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.profile_label.setObjectName("profile_label")
        self.githubimage_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.githubimage_label.setGeometry(QtCore.QRect(130, 70, 101, 101))
        self.githubimage_label.setText("")
        self.githubimage_label.setPixmap(QtGui.QPixmap(""))
        self.githubimage_label.setScaledContents(True)
        self.githubimage_label.setAlignment(QtCore.Qt.AlignCenter)
        self.githubimage_label.setObjectName("githubimage_label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 200, 111, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 200, 181, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.followers_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.followers_label.setText("")
        self.followers_label.setObjectName("followers_label")
        self.verticalLayout_2.addWidget(self.followers_label)
        self.webpage_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.webpage_label.setText("")
        self.webpage_label.setObjectName("webpage_label")
        self.verticalLayout_2.addWidget(self.webpage_label)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 340, 301, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 297, 197))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.description_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description_label.setFont(font)
        self.description_label.setText("")
        self.description_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.gridLayout_4.addWidget(self.description_label, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)
        self.return_button = QtWidgets.QPushButton(self.github_profile_window)
        self.return_button.setGeometry(QtCore.QRect(30, 630, 84, 24))
        self.return_button.setObjectName("return_button")
        self.stackedWidget.addWidget(self.github_profile_window)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# /// | Variables | /////////////////////////////////////////////////////

        # Path to the user's HOME directory and URL:
        self.homepath      =  subprocess.check_output('echo $HOME', shell=True, universal_newlines=True)
        self.homepath      +=  "/.github_webscrapping/"
        self.homepath      =  self.homepath.replace("\n", "")
        self.url           =  "https://github.com/"
        self.image_profile =  "profile.jpg"
        os.system(f'mkdir {self.homepath}')

        # Disabled buttons:
        self.web_button.setEnabled(False)
        self.clone_button.setEnabled(False)

        # JSON File:
        try:
            with open(f'{self.homepath}saves_profiles.json', 'r') as self.file_json:
                self.save_data         = json.load(self.file_json)
                self.list_saveprofiles = self.save_data
        except:
            print(f'Info: Creating JSON file at {self.homepath}')
            self.list_saveprofiles = []
            with open(f'{self.homepath}saves_profiles.json', 'w') as self.file_json:
                json.dump(self.list_saveprofiles, self.file_json)

        # Save the elements from the JSON file into the comboBox:
        for i in self.list_saveprofiles:
            self.savedprofiles_comboBox.addItem(i)

# /// | Actions & Buttons | /////////////////////////////////////////////

        # Actions:
        self.actionHelp.triggered.connect(self.click_help)
        self.actionAbout.triggered.connect(self.click_about)

        # mainpage:
        self.search_button.clicked.connect(self.click_search_button)
        self.autofillprofile_button.clicked.connect(self.click_autofill)
        self.deleteprofile_button.clicked.connect(self.click_delete)

        # github_page:
        self.return_button.clicked.connect(self.click_return)
        self.listWidget.selectionModel().selectionChanged.connect(self.click_listwidget)
        self.web_button.clicked.connect(self.click_web)
        self.clone_button.clicked.connect(self.click_clone)

# ///////////////////////////////////////////////////////////////////////


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GitHub WebScrapping"))
        self.label.setText(_translate("MainWindow", "GitHub WebScrapping"))
        self.groupBox.setTitle(_translate("MainWindow", "Search Profile"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "GitHub Profile:"))
        self.saveprofile_checkBox.setText(_translate("MainWindow", "Save Profile"))
        self.label_3.setText(_translate("MainWindow", "Saved Profiles"))
        self.autofillprofile_button.setText(_translate("MainWindow", "Auto-fill"))
        self.deleteprofile_button.setText(_translate("MainWindow", "Delete"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search parameters"))
        self.label_5.setText(_translate("MainWindow", "Sort"))
        self.sort_comboBox.setItemText(0, _translate("MainWindow", "Stars"))
        self.sort_comboBox.setItemText(1, _translate("MainWindow", "Last update"))
        self.sort_comboBox.setItemText(2, _translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Type of account"))
        self.typeaccount_comboBox.setItemText(0, _translate("MainWindow", "User"))
        self.typeaccount_comboBox.setItemText(1, _translate("MainWindow", "Organization"))
        self.label_4.setText(_translate("MainWindow", "View GitHub profiles and access information about their repositories."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Repositories"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Repository details"))
        self.title_repositories_label.setText(_translate("MainWindow", "No items selected"))
        self.label_15.setText(_translate("MainWindow", "Language:"))
        self.label_16.setText(_translate("MainWindow", "Stars:"))
        self.label_17.setText(_translate("MainWindow", "License:"))
        self.label_18.setText(_translate("MainWindow", "Updated:"))
        self.web_button.setText(_translate("MainWindow", "Web"))
        self.clone_button.setText(_translate("MainWindow", "Clone"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Github Profile"))
        self.profile_label.setText(_translate("MainWindow", "Profile"))
        self.label_7.setText(_translate("MainWindow", "Followers:"))
        self.label_10.setText(_translate("MainWindow", "WebPage:"))
        self.label_12.setText(_translate("MainWindow", "Description:"))
        self.return_button.setText(_translate("MainWindow", "Return"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About"))


# | Functions | ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# - Actions ------------------------------------------------------------------------------------------------------------------------------------

    def click_help(self):
        QMessageBox.about(MainWindow, 'Help Github-WebScrapping', '''Search Profile:
- Search: Search for the specified profile on 'GitHub Profile'.
- Save profile: Save the search for future queries.
- Saved profiles: Consult the saved profiles.
- Auto-fill: Fill the search with the selected value in 'saved profiles'.
- Delete: Delete the selected item in 'saved profiles'.

Search Parameters:
- Sort: Sort the repository search.
- Type of account: Select type of account.

Repository details:
- Web: Open the selected repository in the browser.        
- Clone: Clone the repository to a selected path.
''')
    
    def click_about(self):
        os.system('python3 /usr/share/github-webscrapping/about.py')

# - Fuctions in mainpage -----------------------------------------------------------------------------------------------------------------------

    def click_search_button(self):
        # Search Profile:
        self.search_profile_ = str(self.profile_line_edit.text())
        self.search_profile_ = self.search_profile_.replace(" ", "")
        self.search_profile_ = self.search_profile_.replace("/", "")
        print(f'Search: {self.search_profile_}')


        # Parameters:
        type_account       = self.typeaccount_comboBox.currentText()
        self.type_account_ = type_account
        sort_              = self.sort_comboBox.currentText()
        saved_search       = self.saveprofile_checkBox.checkState()


        # Check if the variable is empty:
        if not self.search_profile_:
            print('Info: Enter a value')
            QMessageBox.information(MainWindow, 'Info', 'Enter a value', QMessageBox.Ok)
            return
        

        # Repositories:
        # -- Repositories URL
        if type_account   == 'User':
            repositories_url = f'{self.url}{self.search_profile_}?tab=repositories&'

        elif type_account == 'Organization':
            repositories_url = f'{self.url}orgs/{self.search_profile_}/repositories?'
        
        # -- Sort parameter
        if sort_   == "Stars":
            repositories_url += 'q=&type=all&language=&sort=stargazers'
        elif sort_ == "Last updated":
            repositories_url += 'q=&type=&language=&sort='
        elif sort_ == "Name":
            repositories_url += 'q=&type=all&language=&sort=name'
        print(f'Repos URL: {repositories_url}')


        # Request GitHub Profile:
        request = requests.get(self.url + self.search_profile_)
        print('request = Status code:', request.status_code)

        if 400 <= request.status_code <= 599:
            print(f'Error: {type_account} not found')
            QMessageBox.critical(MainWindow, 'Error', f'{type_account} or resource not found, please try again.', QMessageBox.Ok)
            return
        content = request.text


        # Request Repositories:
        # -- Code to detect if it's an organization:
        view_content = BeautifulSoup(content, 'lxml')
        x            = view_content.find('div', attrs={'itemtype': True})
        x            = x.get('itemtype')

        if x == 'http://schema.org/Organization':
            if type_account == 'User':
                print(f'Error: The profile is not {type_account.lower()} account')
                QMessageBox.critical(MainWindow, 'Error', f'The GitHub profile is not {type_account.lower()} account')
                return

        request_repos = requests.get(repositories_url)
        print('request_repos = Status code:', request_repos.status_code)

        if 400 <= request_repos.status_code <= 599:
            print('Error: Resource not found')
            QMessageBox.critical(MainWindow, 'Error', 'Resource not found, try specifying the account type.', QMessageBox.Ok)
            return
        content_repos           = request_repos.text
        self.view_content_repos = BeautifulSoup(content_repos, 'lxml')


        # Save user or organization information
        if saved_search != 0:
            self.savedprofiles_comboBox.addItem(self.search_profile_)
            self.list_saveprofiles.append(self.search_profile_)

            with open(f'{self.homepath}saves_profiles.json', 'w') as self.file_json:
                json.dump(self.list_saveprofiles, self.file_json)


        # <> Actions for the user <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        if type_account == 'User':

            # -> Set the profile information
            self.profile   = view_content.find('span', class_='p-nickname vcard-username d-block').get_text()
            self.profile   = self.profile.replace(" ", "")
            self.profile   = self.profile.replace("\n", "")
            print(f'profile_label = {self.profile}')
            self.profile_label.setText(f"{self.profile}")


            # -> Set the followers
            followers = view_content.find('span', class_='text-bold color-fg-default')
            if followers != None:
                followers = followers.get_text()
                followers = followers.replace(" ", "")
                print(f'followers_label = {followers}')
                self.followers_label.setText(f"{followers} followers")
            else:
                print("There are no followers")
                self.followers_label.setText('Not Found')


            # -> Set the webpage
            webpage   = view_content.find('li', {'data-test-selector': 'profile-website-url'})
            if webpage != None:
                webpage = webpage.find('a').get_text()
                self.webpage_label.setText(f'<a href="{webpage}">Link webpage</a>')
                self.webpage_label.setOpenExternalLinks(True)
                print(f'webpage_label = {webpage}')
            else:
                print("Web page link not found")
                self.webpage_label.setText('Not Found')


            # -> Set image
            image_url = view_content.find('img', class_="avatar avatar-user width-full border color-bg-default")
            if image_url != None:
                image_url     = image_url.get('src')
                image_request = requests.get(image_url)

                # --> Save image
                try:
                    with open(self.homepath + self.image_profile, "wb") as image_:
                        image_.write(image_request.content)
                    self.githubimage_label.setPixmap(QtGui.QPixmap(f"{self.homepath}{self.image_profile}"))
                except:
                    print('Error: Error load image')
                    self.githubimage_label.setPixmap(QtGui.QPixmap(""))
                
            else:
                print('Image not found')
                self.githubimage_label.setPixmap(QtGui.QPixmap(""))


            # -> Set description
            description = view_content.find('div', class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
            if description != None:
                description = description.get('data-bio-text')
                print(f'description = "{description}"')
                self.description_label.setText(f'{description}')
            else:
                print('Description not found')


            # -> Set repositories
            self.repositories_list      = self.view_content_repos.find_all('a', {'itemprop': 'name codeRepository'})
            self.repositories_list_info = self.view_content_repos.find_all('div', class_="col-10 col-lg-9 d-inline-block")
            if self.repositories_list != []:
                for i in self.repositories_list:
                    item = i.get_text()
                    item = item.replace("\n", "")
                    item = item.replace(" ", "")
                    print(f'Add item in listWidget: {item}')
                    self.listWidget.addItem(f'{item}')
                    
            else:
                print(f'This profile has no repositories')


            # -> Change stackedWidget
            self.stackedWidget.setCurrentWidget(self.github_profile_window)

        # <> Actions for the organization <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        elif type_account == 'Organization':

            # -> Set the profile information
            self.profile   = view_content.find('h1', class_='h2 lh-condensed').get_text()
            self.profile   = self.profile.replace(" ", "")
            self.profile   = self.profile.replace("\n", "")
            print(f'profile_label = {self.profile}')
            self.profile_label.setText(f"{self.profile}")
            

            # -> Set the followers
            followers = view_content.find('span', class_='text-bold color-fg-default')
            if followers != None:
                followers = followers.get_text()
                followers = followers.replace(" ", "")
                print(f'followers_label = {followers}')
                self.followers_label.setText(f"{followers} followers")
            else:
                print("There are no followers")
                self.followers_label.setText('Not Found')


            # -> Set the webpage
            webpage   = view_content.find('a', {'class': 'color-fg-default', 'rel': 'nofollow'})
            if webpage != None:
                webpage = webpage.get_text()
                self.webpage_label.setText(f'<a href="{webpage}">Link webpage</a>')
                self.webpage_label.setOpenExternalLinks(True)
                print(f'webpage_label = {webpage}')
            else:
                print("Web page link not found")
                self.webpage_label.setText('Not Found')


            # -> Set image
            image_url = view_content.find('img', class_="avatar flex-shrink-0 mb-3 mr-3 mb-md-0 mr-md-4")
            if image_url != None:
                image_url     = image_url.get('src')
                image_request = requests.get(image_url)

                # --> Save image
                try:
                    with open(self.homepath + self.image_profile, "wb") as image_:
                        image_.write(image_request.content)
                    self.githubimage_label.setPixmap(QtGui.QPixmap(f"{self.homepath}{self.image_profile}"))
                except:
                    print('Error: Error load image')
                    self.githubimage_label.setPixmap(QtGui.QPixmap(""))
                
            else:
                print('Image not found')
                self.githubimage_label.setPixmap(QtGui.QPixmap(""))


            # -> Set description
            description = view_content.find('div', class_="d-flex flex-wrap flex-items-start flex-md-items-center my-3")
            description = description.find('div', class_="color-fg-muted")
            if description != None:
                description = description.div.text.strip()
                print(f'description = "{description}"')
                self.description_label.setText(f'{description}')
            else:
                print('Description not found')


            # -> Set repositories
            self.repositories_list      = self.view_content_repos.find_all('a', {'itemprop': 'name codeRepository'})
            self.repositories_list_info = self.view_content_repos.find_all('div', {'itemprop' : 'owns', 'itemtype' : 'http://schema.org/Code'})
            if self.repositories_list != []:
                for i in self.repositories_list:
                    item = i.get_text()
                    item = item.replace("\n", "")
                    item = item.replace(" ", "")
                    print(f'Add item in listWidget: {item}')
                    self.listWidget.addItem(f'{item}')
                    
            else:
                print(f'This profile has no repositories')


            # -> Change stackedWidget
            self.stackedWidget.setCurrentWidget(self.github_profile_window)
    
    
    # Complete the search information:
    def click_autofill(self):
        autofill = self.savedprofiles_comboBox.currentText()
        self.profile_line_edit.setText(autofill)

    # Delete items:
    def click_delete(self):
        delete_item              = self.savedprofiles_comboBox.currentIndex()
        self.savedprofiles_comboBox.removeItem(delete_item)
        self.list_saveprofiles   = [self.savedprofiles_comboBox.itemText(i) for i in range(self.savedprofiles_comboBox.count())]

        with open(f'{self.homepath}saves_profiles.json', 'w') as self.file_json:
                json.dump(self.list_saveprofiles, self.file_json)

# - Fuctions in github_profile_window ----------------------------------------------------------------------------------------------------------

    # Return to the main page: 
    def click_return(self):
        self.stackedWidget.setCurrentIndex(0)

        # Clear github_profile_window
        self.listWidget.clear()

        # Clear lists
        self.repositories_list_info = []
        self.repositories_list      = []

        # Clear repo info
        self.title_repositories_label.setText("No items selected")
        self.language_label.setText("")
        self.stars_label.setText("")
        self.license_label.setText("")
        self.updated_label.setText("")

        # Disabled buttons
        self.web_button.setEnabled(False)


    # Change the information of the selected repository.
    def click_listwidget(self):
        index_listwidget = self.listWidget.currentRow()
        print(f'index listWidget = {index_listwidget}')
        repo_title       = self.listWidget.currentItem()
        repo_title       = repo_title.text()
        print(f'title_repositories = {repo_title}')
        self.title_repositories_label.setText(repo_title)

        # Enabled buttons:
        self.web_button.setEnabled(True)
        self.clone_button.setEnabled(True)

        # - Get info -
        Elements = self.repositories_list_info[index_listwidget]


        # <> Actions for the user | listWidget <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        if self.type_account_ == "User":

            # -> Set language
            language = Elements.find('span', {'itemprop' : 'programmingLanguage'})
            if language != None:
                language = language.get_text()
                print(f'language = {language}')
                self.language_label.setText(language)
            else:
                print('language not found')
                self.language_label.setText('Not found')


            # -> Set star
            stars = self.view_content_repos.find('a', {'href': f'/{self.profile}/{repo_title}/stargazers'})
            if stars != None:
                stars = stars.get_text()
                stars = stars.replace("\n", "")
                stars = stars.replace(" ", "")
                print(f'stars = {stars}')
                self.stars_label.setText(stars)
            else:
                print('Stars not found')
                self.stars_label.setText('0')


            # -> Set license
            license_ = Elements.select_one('span.mr-3:not([class*="ml-"])')
            if license_ != None:
                license_ = license_.get_text()
                license_ = license_.replace("\n", "")
                print(f'license = {license_}')
                self.license_label.setText(license_)
            else:
                print('license not found')
                self.license_label.setText('Not found')


            # -> Set updated
            updated = Elements.find('relative-time', class_="no-wrap")
            if updated != None:
                updated = updated.get_text()
                print(f'updated = {updated}')
                self.updated_label.setText(updated)
            else:
                print('updated not found')
                self.updated_label.setText('Not found')

        # <> Actions for the organization | listWidget <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        elif self.type_account_ == "Organization":

            # -> Set language
            language = Elements.find('span', {'itemprop' : 'programmingLanguage'})
            if language != None:
                language = language.get_text()
                print(f'language = {language}')
                self.language_label.setText(language)
            else:
                print('language not found')
                self.language_label.setText('Not found')


            # -> Set star
            stars = self.view_content_repos.find('a', {'href': f'/{self.profile}/{repo_title}/stargazers'})
            if stars != None:
                stars = stars.get_text()
                stars = stars.replace("\n", "")
                stars = stars.replace(" ", "")
                print(f'stars = {stars}')
                self.stars_label.setText(stars)
            else:
                print('Stars not found')
                self.stars_label.setText('0')


            # -> Set license
            license_ = Elements.find('span', {'class': 'mr-3', 'data-view-component': 'true'})
            if license_ != None:
                license_ = license_.get_text()
                license_ = license_.replace("\n", "")
                print(f'license = {license_}')
                self.license_label.setText(license_)
            else:
                print('license not found')
                self.license_label.setText('Not found')


            # -> Set updated
            updated = Elements.find('relative-time', class_="no-wrap")
            if updated != None:
                updated = updated.get_text()
                print(f'updated = {updated}')
                self.updated_label.setText(updated)
            else:
                print('updated not found')
                self.updated_label.setText('Not found')
    

    # Open the selected repository in the browser:
    def click_web(self):
        repo_title       = self.listWidget.currentItem().text()
        web_repo         = f'{self.url}{self.profile}/{repo_title}'

        try:
            webbrowser.open(web_repo)
        except:
            QMessageBox.critical(MainWindow, "Error", 'Error trying to open the link', QMessageBox.Ok)


    # Clone the repository to a selected path:
    def click_clone(self):
        repo_title       = self.listWidget.currentItem().text()
        clone_repo       = f'{self.url}{self.profile}/{repo_title}.git'

        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        clone_path = QFileDialog.getExistingDirectory(MainWindow, "Select a directory", options=options)

        if clone_path:
            print(f'clone_path = {clone_path}')
            try:
                subprocess.run([f"cd '{clone_path}' && git clone {clone_repo}"], check=True, shell=True)
            except subprocess.CalledProcessError:
                QMessageBox.critical(MainWindow, "Error", 'Error while trying to clone the repository', QMessageBox.Ok)

# //////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    with open("/usr/share/github-webscrapping/styles/styles.css", "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())
