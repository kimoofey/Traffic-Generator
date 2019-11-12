# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kimoo\PycharmProjects\TrafficGenerator\traffic_generator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from scapy.layers.inet import *
from scapy.sendrecv import *
from scapy.utils import *
from scapy.arch import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pathlib import Path, PureWindowsPath

TCP_NUM = 6
UDP_NUM = 17
ICMP_NUM = 1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 457)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(480, 10, 231, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tcpSourcePort = QtWidgets.QLineEdit(self.tab)
        self.tcpSourcePort.setGeometry(QtCore.QRect(110, 10, 101, 20))
        self.tcpSourcePort.setObjectName("tcpSourcePort")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_17.setObjectName("label_17")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 190, 201, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tcpURG = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpURG.setGeometry(QtCore.QRect(10, 20, 70, 21))
        self.tcpURG.setObjectName("tcpURG")
        self.tcpACK = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpACK.setGeometry(QtCore.QRect(10, 40, 70, 21))
        self.tcpACK.setObjectName("tcpACK")
        self.tcpPSH = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpPSH.setGeometry(QtCore.QRect(10, 60, 70, 21))
        self.tcpPSH.setObjectName("tcpPSH")
        self.tcpFIN = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpFIN.setGeometry(QtCore.QRect(100, 60, 70, 21))
        self.tcpFIN.setObjectName("tcpFIN")
        self.tcpSYN = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpSYN.setGeometry(QtCore.QRect(100, 40, 70, 21))
        self.tcpSYN.setObjectName("tcpSYN")
        self.tcpRST = QtWidgets.QCheckBox(self.groupBox_5)
        self.tcpRST.setGeometry(QtCore.QRect(100, 20, 70, 21))
        self.tcpRST.setObjectName("tcpRST")
        self.tcpDestinationPort = QtWidgets.QLineEdit(self.tab)
        self.tcpDestinationPort.setGeometry(QtCore.QRect(110, 40, 101, 20))
        self.tcpDestinationPort.setObjectName("tcpDestinationPort")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.label_18.setObjectName("label_18")
        self.tcpSeqNumber = QtWidgets.QLineEdit(self.tab)
        self.tcpSeqNumber.setGeometry(QtCore.QRect(110, 70, 101, 20))
        self.tcpSeqNumber.setObjectName("tcpSeqNumber")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(10, 70, 81, 21))
        self.label_19.setObjectName("label_19")
        self.tcpAckNumber = QtWidgets.QLineEdit(self.tab)
        self.tcpAckNumber.setGeometry(QtCore.QRect(110, 100, 101, 20))
        self.tcpAckNumber.setObjectName("tcpAckNumber")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.label_20.setObjectName("label_20")
        self.tcpOffset = QtWidgets.QLineEdit(self.tab)
        self.tcpOffset.setGeometry(QtCore.QRect(110, 130, 101, 20))
        self.tcpOffset.setObjectName("tcpOffset")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_21.setObjectName("label_21")
        self.tcpReserved = QtWidgets.QLineEdit(self.tab)
        self.tcpReserved.setGeometry(QtCore.QRect(110, 160, 101, 20))
        self.tcpReserved.setObjectName("tcpReserved")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(10, 160, 61, 21))
        self.label_22.setObjectName("label_22")
        self.tcpWindSize = QtWidgets.QLineEdit(self.tab)
        self.tcpWindSize.setGeometry(QtCore.QRect(110, 290, 101, 20))
        self.tcpWindSize.setObjectName("tcpWindSize")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 290, 61, 21))
        self.label_23.setObjectName("label_23")
        self.tcpUrPointer = QtWidgets.QLineEdit(self.tab)
        self.tcpUrPointer.setGeometry(QtCore.QRect(110, 320, 101, 20))
        self.tcpUrPointer.setObjectName("tcpUrPointer")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(10, 320, 61, 21))
        self.label_24.setObjectName("label_24")
        self.tcpChecksum = QtWidgets.QLineEdit(self.tab)
        self.tcpChecksum.setGeometry(QtCore.QRect(130, 350, 81, 20))
        self.tcpChecksum.setObjectName("tcpChecksum")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(10, 350, 61, 21))
        self.label_25.setObjectName("label_25")
        self.tcpChecksumCheckbox = QtWidgets.QCheckBox(self.tab)
        self.tcpChecksumCheckbox.setGeometry(QtCore.QRect(70, 350, 70, 21))
        self.tcpChecksumCheckbox.setObjectName("tcpChecksumCheckbox")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.udpSourcePort = QtWidgets.QLineEdit(self.tab_2)
        self.udpSourcePort.setGeometry(QtCore.QRect(110, 10, 101, 20))
        self.udpSourcePort.setObjectName("udpSourcePort")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_26.setObjectName("label_26")
        self.udpDestinationPort = QtWidgets.QLineEdit(self.tab_2)
        self.udpDestinationPort.setGeometry(QtCore.QRect(110, 40, 101, 20))
        self.udpDestinationPort.setObjectName("udpDestinationPort")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(10, 40, 81, 21))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_28.setObjectName("label_28")
        self.udpLength = QtWidgets.QLineEdit(self.tab_2)
        self.udpLength.setGeometry(QtCore.QRect(130, 70, 81, 20))
        self.udpLength.setObjectName("udpLength")
        self.udpLengthCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.udpLengthCheckbox.setGeometry(QtCore.QRect(70, 70, 70, 21))
        self.udpLengthCheckbox.setObjectName("udpLengthCheckbox")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_29.setObjectName("label_29")
        self.udpChecksum = QtWidgets.QLineEdit(self.tab_2)
        self.udpChecksum.setGeometry(QtCore.QRect(130, 100, 81, 20))
        self.udpChecksum.setObjectName("udpChecksum")
        self.udpChecksumCheckbox = QtWidgets.QCheckBox(self.tab_2)
        self.udpChecksumCheckbox.setGeometry(QtCore.QRect(70, 100, 70, 21))
        self.udpChecksumCheckbox.setObjectName("udpChecksumCheckbox")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.icmpChecksum = QtWidgets.QLineEdit(self.tab_3)
        self.icmpChecksum.setGeometry(QtCore.QRect(130, 130, 81, 20))
        self.icmpChecksum.setObjectName("icmpChecksum")
        self.icmpChecksumCheckbox = QtWidgets.QCheckBox(self.tab_3)
        self.icmpChecksumCheckbox.setGeometry(QtCore.QRect(70, 130, 70, 21))
        self.icmpChecksumCheckbox.setObjectName("icmpChecksumCheckbox")
        self.label_43 = QtWidgets.QLabel(self.tab_3)
        self.label_43.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.tab_3)
        self.label_44.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_44.setObjectName("label_44")
        self.icmpSeqNumber = QtWidgets.QLineEdit(self.tab_3)
        self.icmpSeqNumber.setGeometry(QtCore.QRect(110, 40, 101, 20))
        self.icmpSeqNumber.setObjectName("icmpSeqNumber")
        self.label_45 = QtWidgets.QLabel(self.tab_3)
        self.label_45.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_45.setObjectName("label_45")
        self.icmpCode = QtWidgets.QLineEdit(self.tab_3)
        self.icmpCode.setGeometry(QtCore.QRect(110, 70, 101, 20))
        self.icmpCode.setObjectName("icmpCode")
        self.label_46 = QtWidgets.QLabel(self.tab_3)
        self.label_46.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_46.setObjectName("label_46")
        self.icmpID = QtWidgets.QLineEdit(self.tab_3)
        self.icmpID.setGeometry(QtCore.QRect(110, 100, 101, 20))
        self.icmpID.setObjectName("icmpID")
        self.label_47 = QtWidgets.QLabel(self.tab_3)
        self.label_47.setGeometry(QtCore.QRect(10, 100, 61, 21))
        self.label_47.setObjectName("label_47")
        self.icmpType = QtWidgets.QComboBox(self.tab_3)
        self.icmpType.setGeometry(QtCore.QRect(110, 10, 101, 21))
        self.icmpType.setObjectName("icmpType")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.icmpType.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.ipNetworkAdapter = QtWidgets.QComboBox(self.centralwidget)
        self.ipNetworkAdapter.setGeometry(QtCore.QRect(10, 30, 451, 21))
        self.ipNetworkAdapter.setObjectName("ipNetworkAdapter")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 59, 451, 371))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 151, 151))
        self.groupBox.setObjectName("groupBox")
        self.ipDelay = QtWidgets.QCheckBox(self.groupBox)
        self.ipDelay.setGeometry(QtCore.QRect(10, 50, 70, 21))
        self.ipDelay.setObjectName("ipDelay")
        self.ipReliability = QtWidgets.QCheckBox(self.groupBox)
        self.ipReliability.setGeometry(QtCore.QRect(10, 70, 70, 21))
        self.ipReliability.setObjectName("ipReliability")
        self.ipThroughput = QtWidgets.QCheckBox(self.groupBox)
        self.ipThroughput.setGeometry(QtCore.QRect(10, 90, 81, 21))
        self.ipThroughput.setObjectName("ipThroughput")
        self.ipECN = QtWidgets.QComboBox(self.groupBox)
        self.ipECN.setGeometry(QtCore.QRect(80, 120, 61, 21))
        self.ipECN.setObjectName("ipECN")
        self.ipECN.addItem("")
        self.ipECN.addItem("")
        self.ipECN.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 61, 21))
        self.label_8.setObjectName("label_8")
        self.ipPrecendence = QtWidgets.QLineEdit(self.groupBox)
        self.ipPrecendence.setGeometry(QtCore.QRect(80, 20, 61, 20))
        self.ipPrecendence.setObjectName("ipPrecendence")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_3.setGeometry(QtCore.QRect(180, 180, 251, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ipData = QtWidgets.QTextEdit(self.groupBox_3)
        self.ipData.setGeometry(QtCore.QRect(10, 20, 231, 121))
        self.ipData.setObjectName("ipData")
        self.ipSourceIP = QtWidgets.QLineEdit(self.tab_4)
        self.ipSourceIP.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.ipSourceIP.setObjectName("ipSourceIP")
        self.ipTotalLength = QtWidgets.QLineEdit(self.tab_4)
        self.ipTotalLength.setGeometry(QtCore.QRect(10, 140, 101, 20))
        self.ipTotalLength.setObjectName("ipTotalLength")
        self.ipChecksum = QtWidgets.QLineEdit(self.tab_4)
        self.ipChecksum.setGeometry(QtCore.QRect(10, 80, 101, 20))
        self.ipChecksum.setObjectName("ipChecksum")
        self.ipSourceIPCheckbox = QtWidgets.QCheckBox(self.tab_4)
        self.ipSourceIPCheckbox.setGeometry(QtCore.QRect(120, 20, 70, 17))
        self.ipSourceIPCheckbox.setObjectName("ipSourceIPCheckbox")
        self.ipChecksumCheckbox = QtWidgets.QCheckBox(self.tab_4)
        self.ipChecksumCheckbox.setGeometry(QtCore.QRect(120, 80, 70, 17))
        self.ipChecksumCheckbox.setObjectName("ipChecksumCheckbox")
        self.ipTotalLengthCheckbox = QtWidgets.QCheckBox(self.tab_4)
        self.ipTotalLengthCheckbox.setGeometry(QtCore.QRect(120, 140, 70, 17))
        self.ipTotalLengthCheckbox.setObjectName("ipTotalLengthCheckbox")
        self.ipDestinationIP = QtWidgets.QLineEdit(self.tab_4)
        self.ipDestinationIP.setGeometry(QtCore.QRect(200, 20, 111, 20))
        self.ipDestinationIP.setObjectName("ipDestinationIP")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(200, 0, 111, 20))
        self.label_10.setObjectName("label_10")
        self.ipProtocol = QtWidgets.QLineEdit(self.tab_4)
        self.ipProtocol.setGeometry(QtCore.QRect(200, 80, 51, 20))
        self.ipProtocol.setObjectName("ipProtocol")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(200, 60, 61, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(200, 120, 61, 20))
        self.label_12.setObjectName("label_12")
        self.ipOffset = QtWidgets.QLineEdit(self.tab_4)
        self.ipOffset.setGeometry(QtCore.QRect(200, 140, 51, 20))
        self.ipOffset.setObjectName("ipOffset")
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(260, 120, 61, 20))
        self.label_13.setObjectName("label_13")
        self.ipIHL = QtWidgets.QLineEdit(self.tab_4)
        self.ipIHL.setGeometry(QtCore.QRect(260, 140, 51, 20))
        self.ipIHL.setObjectName("ipIHL")
        self.ipID = QtWidgets.QLineEdit(self.tab_4)
        self.ipID.setGeometry(QtCore.QRect(380, 140, 51, 20))
        self.ipID.setObjectName("ipID")
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setGeometry(QtCore.QRect(380, 120, 61, 20))
        self.label_14.setObjectName("label_14")
        self.ipVersion = QtWidgets.QLineEdit(self.tab_4)
        self.ipVersion.setGeometry(QtCore.QRect(320, 140, 51, 20))
        self.ipVersion.setObjectName("ipVersion")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(320, 120, 61, 20))
        self.label_15.setObjectName("label_15")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(330, 10, 101, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.ipReserved = QtWidgets.QCheckBox(self.groupBox_4)
        self.ipReserved.setGeometry(QtCore.QRect(10, 20, 70, 21))
        self.ipReserved.setObjectName("ipReserved")
        self.ipDF = QtWidgets.QCheckBox(self.groupBox_4)
        self.ipDF.setGeometry(QtCore.QRect(10, 40, 70, 21))
        self.ipDF.setObjectName("ipDF")
        self.ipMF = QtWidgets.QCheckBox(self.groupBox_4)
        self.ipMF.setGeometry(QtCore.QRect(10, 60, 70, 21))
        self.ipMF.setObjectName("ipMF")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setGeometry(QtCore.QRect(260, 60, 61, 20))
        self.label_16.setObjectName("label_16")
        self.ipTTL = QtWidgets.QLineEdit(self.tab_4)
        self.ipTTL.setGeometry(QtCore.QRect(260, 80, 51, 20))
        self.ipTTL.setObjectName("ipTTL")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 11, 111, 20))
        self.label.setObjectName("label")
        self.sourceMACCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sourceMACCheckbox.setGeometry(QtCore.QRect(840, 30, 70, 17))
        self.sourceMACCheckbox.setObjectName("sourceMACCheckbox")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(730, 10, 61, 20))
        self.label_48.setObjectName("label_48")
        self.sourceMAC = QtWidgets.QLineEdit(self.centralwidget)
        self.sourceMAC.setGeometry(QtCore.QRect(730, 30, 101, 20))
        self.sourceMAC.setObjectName("sourceMAC")
        self.destinationMACCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.destinationMACCheckbox.setGeometry(QtCore.QRect(840, 70, 70, 17))
        self.destinationMACCheckbox.setObjectName("destinationMACCheckbox")
        self.destinationMAC = QtWidgets.QLineEdit(self.centralwidget)
        self.destinationMAC.setGeometry(QtCore.QRect(730, 70, 101, 20))
        self.destinationMAC.setObjectName("destinationMAC")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(730, 50, 91, 20))
        self.label_49.setObjectName("label_49")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(730, 100, 181, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_7)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 161, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 109))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.packetsList = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.packetsList.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.packetsList.setObjectName("packetsList")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(740, 250, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(830, 250, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(740, 280, 75, 23))
        self.loadButton.setObjectName("loadButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(830, 280, 75, 23))
        self.addButton.setObjectName("addButton")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(730, 310, 181, 51))
        self.groupBox_8.setObjectName("groupBox_8")
        self.packetName = QtWidgets.QLineEdit(self.groupBox_8)
        self.packetName.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.packetName.setObjectName("packetName")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(740, 370, 161, 23))
        self.saveButton.setObjectName("saveButton")
        self.sendAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendAllButton.setGeometry(QtCore.QRect(830, 400, 75, 31))
        self.sendAllButton.setObjectName("sendAllButton")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(740, 400, 75, 31))
        self.sendButton.setObjectName("sendButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)

        self.clearButton.clicked.connect(self.clear)
        self.deleteButton.clicked.connect(self.delete)
        self.loadButton.clicked.connect(self.load)
        # self.addButton.clicked.connect(self.add)
        self.saveButton.clicked.connect(self.save)
        self.sendButton.clicked.connect(self.sendPacket)
        self.sendAllButton.clicked.connect(self.sendAll)

        interfaces = get_windows_if_list()
        for i in range(len(interfaces) - 1):
            self.ipNetworkAdapter.addItem(
                str(interfaces[i].get("name")) + " - " + str(interfaces[i].get("description")))
            # print(interfaces[i])

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ipSourceIPCheckbox.stateChanged.connect(self.ipSourceIPState)
        self.ipChecksumCheckbox.stateChanged.connect(self.ipChecksumState)
        self.ipTotalLengthCheckbox.stateChanged.connect(self.ipTotalLengthState)
        self.sourceMACCheckbox.stateChanged.connect(self.sourceMACState)
        self.destinationMACCheckbox.stateChanged.connect(self.destinationMACState)
        self.tcpChecksumCheckbox.stateChanged.connect(self.tcpChecksumState)
        self.udpLengthCheckbox.stateChanged.connect(self.udpLengthState)
        self.udpChecksumCheckbox.stateChanged.connect(self.udpChecksumState)
        self.icmpChecksumCheckbox.stateChanged.connect(self.icmpChecksumState)
        self.ipMF.stateChanged.connect(self.checkIPFlags)
        self.ipDF.stateChanged.connect(self.checkIPFlags)
        self.ipReserved.stateChanged.connect(self.checkIPFlags)
        self.packetsList.itemClicked.connect(self.showPacketInfo)
        # Mockups TCP
        self.tcpSourcePort.setText("20")
        self.tcpDestinationPort.setText("80")
        self.tcpSeqNumber.setText("0")
        self.tcpAckNumber.setText("0")
        self.tcpOffset.setText("5")
        self.tcpReserved.setText("0")
        self.tcpWindSize.setText("8192")
        self.tcpUrPointer.setText("0")

        self.ipVersion.setText("4")
        self.ipIHL.setText("5")
        self.ipID.setText("1")
        self.ipTTL.setText("64")
        self.ipDestinationIP.setText("127.0.0.1")
        self.ipPrecendence.setText("0")
        self.ipSourceIP.setText("127.0.0.1")
        self.ipTotalLength.setText("67")
        self.ipChecksumCheckbox.setChecked(True)
        self.ipTotalLengthCheckbox.setChecked(True)
        self.ipSourceIPCheckbox.setChecked(True)
        self.ipDF.setChecked(True)
        self.sourceMACCheckbox.setChecked(True)
        self.destinationMACCheckbox.setChecked(True)

        # Mockups UDP
        self.udpSourcePort.setText("53")
        self.udpDestinationPort.setText("53")

        # Mockups ICMP
        self.icmpSeqNumber.setText("0")
        self.icmpCode.setText("8")
        self.icmpID.setText("0")

    def showPacketInfo(self):
        print(self.packetsList.currentItem().text())
        packet = rdpcap(self.packetsList.currentItem().text())

        index = self.ipNetworkAdapter.currentIndex()
        interfaces = get_windows_if_list()
        inter = interfaces[index].get("description")
        send(packet, iface=inter)
        packet.show()
        return

    def ipSourceIPState(self):
        if self.ipSourceIPCheckbox.isChecked():
            self.ipSourceIP.setDisabled(True)
        else:
            self.ipSourceIP.setEnabled(True)
    def ipChecksumState(self):
        if self.ipChecksumCheckbox.isChecked():
            self.ipChecksum.setDisabled(True)
        else:
            self.ipChecksum.setEnabled(True)
    def ipTotalLengthState(self):
        if self.ipTotalLengthCheckbox.isChecked():
            self.ipTotalLength.setDisabled(True)
        else:
            self.ipTotalLength.setEnabled(True)
    def sourceMACState(self):
        if self.sourceMACCheckbox.isChecked():
            self.sourceMAC.setDisabled(True)
        else:
            self.sourceMAC.setEnabled(True)
    def destinationMACState(self):
        if self.destinationMACCheckbox.isChecked():
            self.destinationMAC.setDisabled(True)
        else:
            self.destinationMAC.setEnabled(True)
    def tcpChecksumState(self):
        if self.tcpChecksumCheckbox.isChecked():
            self.tcpChecksum.setDisabled(True)
        else:
            self.tcpChecksum.setEnabled(True)
    def udpLengthState(self):
        if self.udpLengthCheckbox.isChecked():
            self.udpLength.setDisabled(True)
        else:
            self.udpLength.setEnabled(True)
    def udpChecksumState(self):
        if self.udpChecksumCheckbox.isChecked():
            self.udpChecksum.setDisabled(True)
        else:
            self.udpChecksum.setEnabled(True)
    def icmpChecksumState(self):
        if self.icmpChecksumCheckbox.isChecked():
            self.icmpChecksum.setDisabled(True)
        else:
            self.icmpChecksum.setEnabled(True)
    def checkIPFlags(self):
        if self.ipReserved.isChecked():
            self.ipMF.setCheckState(False)
            self.ipDF.setCheckState(False)

        if self.ipDF.isChecked():
            self.ipMF.setCheckState(False)
            self.ipReserved.setCheckState(False)

        if self.ipMF.isChecked():
            self.ipDF.setCheckState(False)
            self.ipReserved.setCheckState(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Traffic Generator"))
        self.label_17.setText(_translate("MainWindow", "Source Port"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Flags"))
        self.tcpURG.setText(_translate("MainWindow", "URG"))
        self.tcpACK.setText(_translate("MainWindow", "ACK"))
        self.tcpPSH.setText(_translate("MainWindow", "PSH"))
        self.tcpFIN.setText(_translate("MainWindow", "FIN"))
        self.tcpSYN.setText(_translate("MainWindow", "SYN"))
        self.tcpRST.setText(_translate("MainWindow", "RST"))
        self.label_18.setText(_translate("MainWindow", "Destination Port"))
        self.label_19.setText(_translate("MainWindow", "Seq. number"))
        self.label_20.setText(_translate("MainWindow", "Ack. number"))
        self.label_21.setText(_translate("MainWindow", "Offset"))
        self.label_22.setText(_translate("MainWindow", "Reserved"))
        self.label_23.setText(_translate("MainWindow", "Wind. size"))
        self.label_24.setText(_translate("MainWindow", "Ur. pointer"))
        self.label_25.setText(_translate("MainWindow", "Checksum"))
        self.tcpChecksumCheckbox.setText(_translate("MainWindow", "auto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "TCP"))
        self.label_26.setText(_translate("MainWindow", "Source Port"))
        self.label_27.setText(_translate("MainWindow", "Destination Port"))
        self.label_28.setText(_translate("MainWindow", "Length"))
        self.udpLengthCheckbox.setText(_translate("MainWindow", "auto"))
        self.label_29.setText(_translate("MainWindow", "Checksum"))
        self.udpChecksumCheckbox.setText(_translate("MainWindow", "auto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "UDP"))
        self.icmpChecksumCheckbox.setText(_translate("MainWindow", "auto"))
        self.label_43.setText(_translate("MainWindow", "Checksum"))
        self.label_44.setText(_translate("MainWindow", "Type"))
        self.label_45.setText(_translate("MainWindow", "Seq. number"))
        self.label_46.setText(_translate("MainWindow", "Code"))
        self.label_47.setText(_translate("MainWindow", "ID"))
        self.icmpType.setItemText(0, _translate("MainWindow", "0"))
        self.icmpType.setItemText(1, _translate("MainWindow", "3"))
        self.icmpType.setItemText(2, _translate("MainWindow", "4"))
        self.icmpType.setItemText(3, _translate("MainWindow", "5"))
        self.icmpType.setItemText(4, _translate("MainWindow", "6"))
        self.icmpType.setItemText(5, _translate("MainWindow", "8"))
        self.icmpType.setItemText(6, _translate("MainWindow", "9"))
        self.icmpType.setItemText(7, _translate("MainWindow", "10"))
        self.icmpType.setItemText(8, _translate("MainWindow", "11"))
        self.icmpType.setItemText(9, _translate("MainWindow", "12"))
        self.icmpType.setItemText(10, _translate("MainWindow", "13"))
        self.icmpType.setItemText(11, _translate("MainWindow", "14"))
        self.icmpType.setItemText(12, _translate("MainWindow", "15"))
        self.icmpType.setItemText(13, _translate("MainWindow", "16"))
        self.icmpType.setItemText(14, _translate("MainWindow", "17"))
        self.icmpType.setItemText(15, _translate("MainWindow", "18"))
        self.icmpType.setItemText(16, _translate("MainWindow", "30"))
        self.icmpType.setItemText(17, _translate("MainWindow", "31"))
        self.icmpType.setItemText(18, _translate("MainWindow", "32"))
        self.icmpType.setItemText(19, _translate("MainWindow", "33"))
        self.icmpType.setItemText(20, _translate("MainWindow", "34"))
        self.icmpType.setItemText(21, _translate("MainWindow", "35"))
        self.icmpType.setItemText(22, _translate("MainWindow", "36"))
        self.icmpType.setItemText(23, _translate("MainWindow", "37"))
        self.icmpType.setItemText(24, _translate("MainWindow", "38"))
        self.icmpType.setItemText(25, _translate("MainWindow", "39"))
        self.icmpType.setItemText(26, _translate("MainWindow", "40"))
        self.icmpType.setItemText(27, _translate("MainWindow", "41"))
        self.icmpType.setItemText(28, _translate("MainWindow", "42"))
        self.icmpType.setItemText(29, _translate("MainWindow", "43"))
        self.icmpType.setItemText(30, _translate("MainWindow", "253"))
        self.icmpType.setItemText(31, _translate("MainWindow", "254"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "ICMP"))
        self.groupBox.setTitle(_translate("MainWindow", "Type of Service"))
        self.ipDelay.setText(_translate("MainWindow", "Delay"))
        self.ipReliability.setText(_translate("MainWindow", "Reliability"))
        self.ipThroughput.setText(_translate("MainWindow", "Throughput"))
        self.ipECN.setItemText(0, _translate("MainWindow", "ECT"))
        self.ipECN.setItemText(1, _translate("MainWindow", "Not-ECT"))
        self.ipECN.setItemText(2, _translate("MainWindow", "CE"))
        self.label_8.setText(_translate("MainWindow", "ECN"))
        self.label_9.setText(_translate("MainWindow", "Precendence"))
        self.label_2.setText(_translate("MainWindow", "Source IP"))
        self.label_3.setText(_translate("MainWindow", "Checksum"))
        self.label_4.setText(_translate("MainWindow", "Total Length"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Data"))
        self.ipSourceIPCheckbox.setText(_translate("MainWindow", "auto"))
        self.ipChecksumCheckbox.setText(_translate("MainWindow", "auto"))
        self.ipTotalLengthCheckbox.setText(_translate("MainWindow", "auto"))
        self.label_10.setText(_translate("MainWindow", "Destination IP"))
        self.label_11.setText(_translate("MainWindow", "Protocol"))
        self.label_12.setText(_translate("MainWindow", "Offset"))
        self.label_13.setText(_translate("MainWindow", "IHL"))
        self.label_14.setText(_translate("MainWindow", "ID"))
        self.label_15.setText(_translate("MainWindow", "Version"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Flags"))
        self.ipReserved.setText(_translate("MainWindow", "Reserved"))
        self.ipDF.setText(_translate("MainWindow", "DF"))
        self.ipMF.setText(_translate("MainWindow", "MF"))
        self.label_16.setText(_translate("MainWindow", "TTL"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "IPv4"))
        self.label.setText(_translate("MainWindow", "Network Adapter"))
        self.sourceMACCheckbox.setText(_translate("MainWindow", "auto"))
        self.label_48.setText(_translate("MainWindow", "Source MAC"))
        self.destinationMACCheckbox.setText(_translate("MainWindow", "auto"))
        self.label_49.setText(_translate("MainWindow", "Destination MAC"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Packets"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Name"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.sendAllButton.setText(_translate("MainWindow", "Send all"))
        self.sendButton.setText(_translate("MainWindow", "Send"))

    def readData(self):

        packet = IP()
        packet[IP].version = int(self.ipVersion.text())
        packet[IP].ihl = int(self.ipIHL.text())
        packet[IP].tos = self.calcTOS()
        packet[IP].id = int(self.ipID.text())
        packet[IP].flags = self.calcFlags()
        packet[IP].ttl = int(self.ipTTL.text())
        packet[IP].dst = self.ipDestinationIP.text()
        packet[IP].frag = int(self.ipOffset.text())

        if not self.ipSourceIPCheckbox.isChecked():
            packet[IP].src = self.ipSourceIP.text()

        if not self.ipChecksumCheckbox.isChecked():
            packet[IP].chksum = int(self.ipChecksum.text())

        if not self.ipTotalLengthCheckbox.isChecked():
            packet[IP].len = int(self.ipTotalLength.text())

        if self.tabWidget.currentIndex() == 0:
            packet[IP].proto = TCP_NUM
            packetTCP = packet / TCP()
            packetTCP[TCP].sport = int(self.tcpSourcePort.text())
            packetTCP[TCP].dport = int(self.tcpDestinationPort.text())
            packetTCP[TCP].seq = int(self.tcpSeqNumber.text())
            packetTCP[TCP].ack = int(self.tcpAckNumber.text())
            packetTCP[TCP].dataofs = int(self.tcpOffset.text())
            packetTCP[TCP].reserved = int(self.tcpReserved.text())
            packetTCP[TCP].window = int(self.tcpWindSize.text())
            packetTCP[TCP].urgptr = int(self.tcpUrPointer.text())

            if self.tcpURG.isChecked():
                packetTCP[TCP].flags = "U"
            if self.tcpACK.isChecked():
                packetTCP[TCP].flags = "A"
            if self.tcpPSH.isChecked():
                packetTCP[TCP].flags = "P"
            if self.tcpRST.isChecked():
                packetTCP[TCP].flags = "R"
            if self.tcpSYN.isChecked():
                packetTCP[TCP].flags = "S"
            if self.tcpFIN.isChecked():
                packetTCP[TCP].flags = "F"

            if not self.tcpChecksumCheckbox.isChecked():
                packetTCP[TCP].chksum = int(self.tcpChecksum.text())

            packet = packetTCP
        elif self.tabWidget.currentIndex() == 1:
            packet[IP].proto = UDP_NUM
            packetUDP = packet / UDP()

            packetUDP[UDP].sport = int(self.udpSourcePort.text())
            packetUDP[UDP].dport = int(self.udpDestinationPort.text())

            if not self.udpLengthCheckbox.isChecked():
                packetUDP[UDP].len = int(self.udpLength.text())

            if not self.udpChecksumCheckbox.isChecked():
                packetUDP[UDP].chksum = int(self.udpChecksum.text())

            packet = packetUDP
        else:
            packet[IP].proto = ICMP_NUM
            packetICMP = packet / ICMP()
            packetICMP[ICMP].type = int(self.icmpType.currentText())
            packetICMP[ICMP].seq = int(self.icmpSeqNumber.text())
            packetICMP[ICMP].code = int(self.icmpCode.text())
            packetICMP[ICMP].id = int(self.icmpID.text())

            if not self.icmpChecksumCheckbox.isChecked():
                packetICMP[ICMP].chksum = int(self.icmpChecksum.text())

            packet = packetICMP

        packet = packet / self.ipData.toPlainText()
        print(packet)
        return packet

    def calcTOS(self):
        tos = bin(int(self.ipPrecendence.text()))
        tos = str(tos)
        if self.ipDelay.isChecked():
            tos += '1'
        else:
            tos += '0'
        if self.ipThroughput.isChecked():
            tos += '1'
        else:
            tos += '0'
        if self.ipReliability.isChecked():
            tos += '1'
        else:
            tos += '0'

        if self.ipECN.currentIndex() == 0:
            tos += '01'
        if self.ipECN.currentIndex() == 1:
            tos += '00'
        else:
            tos += '11'

        tos = int(tos, 2)
        return tos

    def calcFlags(self):
        if self.ipReserved.isChecked():
            return ""
        if self.ipDF.isChecked():
            return "DF"
        if self.ipMF.isChecked():
            return "MF"

    def clear(self):
        self.packetsList.clear()
        return

    def delete(self):
        packet = self.packetsList.row(self.packetsList.currentItem())
        self.packetsList.takeItem(packet)
        return

    def openFileNameDialog(self):
        fileName = QFileDialog.getOpenFileName(MainWindow, "Choose file", "C:\\Users\\kimoo\\Desktop",
                                               "All files (*.*);;Packet Capture (*.cap)")
        return fileName[0]

    def load(self):
        packet = self.openFileNameDialog()
        packet = str(PureWindowsPath(packet))
        self.packetsList.addItem(packet)
        return

    def save(self):
        packet = self.readData()
        filePath = "C:\\Users\\kimoo\\Desktop\\"
        filePath += str(self.packetName.text())
        filePath += ".cap"
        wrpcap(filePath, packet)
        return

    def getInterface(self):
        iface = None
        for i in get_if_list():
            print(i)
            if "\\Device\\NPF_{4F65BF41-7731-41E0-9D24-A51413E698F3}" in i:
                iface = i
        if not iface:
            print("Cannot find Realtek PCIe GBE Family Controller interface")
        return iface

    def sendPacket(self):
        packet = self.readData()
        index = self.ipNetworkAdapter.currentIndex()
        interface = get_windows_if_list()
        send(packet, iface=interface[index].get("name"))
        return

    def sendAll(self):
        print(self.packetsList.count())
        index = self.ipNetworkAdapter.currentIndex()
        interface = get_windows_if_list()
        for i in range(self.packetsList.count()):
            item = self.packetsList.item(i)
            packet = rdpcap(item.text())
            send(packet, iface=interface[index].get("name"))

        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
