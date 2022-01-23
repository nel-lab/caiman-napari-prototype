# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_offline_gui_template.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainOfflineGUIWidget(object):
    def setupUi(self, MainOfflineGUIWidget):
        MainOfflineGUIWidget.setObjectName("MainOfflineGUIWidget")
        MainOfflineGUIWidget.resize(300, 905)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainOfflineGUIWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(MainOfflineGUIWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButtonNewBatch = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonNewBatch.setObjectName("pushButtonNewBatch")
        self.horizontalLayout_9.addWidget(self.pushButtonNewBatch)
        self.pushButtonOpenBatch = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonOpenBatch.setObjectName("pushButtonOpenBatch")
        self.horizontalLayout_9.addWidget(self.pushButtonOpenBatch)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.pushButtonOpenMovie = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonOpenMovie.setObjectName("pushButtonOpenMovie")
        self.verticalLayout.addWidget(self.pushButtonOpenMovie)
        self.groupBox = QtWidgets.QGroupBox(MainOfflineGUIWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtonParamsMCorr = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonParamsMCorr.setObjectName("pushButtonParamsMCorr")
        self.horizontalLayout_10.addWidget(self.pushButtonParamsMCorr)
        self.pushButtonParamsCNMF = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonParamsCNMF.setObjectName("pushButtonParamsCNMF")
        self.horizontalLayout_10.addWidget(self.pushButtonParamsCNMF)
        self.pushButtonParamsCNMFE = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonParamsCNMFE.setObjectName("pushButtonParamsCNMFE")
        self.horizontalLayout_10.addWidget(self.pushButtonParamsCNMFE)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButtonStart = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.horizontalLayout_11.addWidget(self.pushButtonStart)
        self.pushButtonStartItem = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonStartItem.setObjectName("pushButtonStartItem")
        self.horizontalLayout_11.addWidget(self.pushButtonStartItem)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButtonDelItem = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonDelItem.setObjectName("pushButtonDelItem")
        self.horizontalLayout_12.addWidget(self.pushButtonDelItem)
        self.pushButtonAbort = QtWidgets.QPushButton(MainOfflineGUIWidget)
        self.pushButtonAbort.setObjectName("pushButtonAbort")
        self.horizontalLayout_12.addWidget(self.pushButtonAbort)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.label = QtWidgets.QLabel(MainOfflineGUIWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidgetItems = QtWidgets.QListWidget(MainOfflineGUIWidget)
        self.listWidgetItems.setObjectName("listWidgetItems")
        self.verticalLayout.addWidget(self.listWidgetItems)
        self.groupBox_2 = QtWidgets.QGroupBox(MainOfflineGUIWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxProjectionOpts = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxProjectionOpts.setObjectName("comboBoxProjectionOpts")
        self.comboBoxProjectionOpts.addItem("")
        self.comboBoxProjectionOpts.addItem("")
        self.comboBoxProjectionOpts.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxProjectionOpts)
        self.pushButtonViewProjection = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonViewProjection.setObjectName("pushButtonViewProjection")
        self.horizontalLayout.addWidget(self.pushButtonViewProjection)
        self.pushButtonEvalComponents = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonEvalComponents.setObjectName("pushButtonEvalComponents")
        self.horizontalLayout.addWidget(self.pushButtonEvalComponents)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.textBrowserParams = QtWidgets.QTextBrowser(MainOfflineGUIWidget)
        self.textBrowserParams.setObjectName("textBrowserParams")
        self.verticalLayout.addWidget(self.textBrowserParams)
        self.textBrowserStdOut = QtWidgets.QTextBrowser(MainOfflineGUIWidget)
        self.textBrowserStdOut.setObjectName("textBrowserStdOut")
        self.verticalLayout.addWidget(self.textBrowserStdOut)

        self.retranslateUi(MainOfflineGUIWidget)
        QtCore.QMetaObject.connectSlotsByName(MainOfflineGUIWidget)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonNewBatch, self.pushButtonOpenBatch)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonOpenBatch, self.pushButtonOpenMovie)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonOpenMovie, self.pushButtonParamsMCorr)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonParamsMCorr, self.pushButtonParamsCNMF)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonParamsCNMF, self.pushButtonParamsCNMFE)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonParamsCNMFE, self.pushButtonStart)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonStart, self.pushButtonStartItem)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonStartItem, self.pushButtonDelItem)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonDelItem, self.pushButtonAbort)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonAbort, self.listWidgetItems)
        MainOfflineGUIWidget.setTabOrder(self.listWidgetItems, self.comboBoxProjectionOpts)
        MainOfflineGUIWidget.setTabOrder(self.comboBoxProjectionOpts, self.pushButtonViewProjection)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonViewProjection, self.pushButtonEvalComponents)
        MainOfflineGUIWidget.setTabOrder(self.pushButtonEvalComponents, self.textBrowserParams)
        MainOfflineGUIWidget.setTabOrder(self.textBrowserParams, self.textBrowserStdOut)

    def retranslateUi(self, MainOfflineGUIWidget):
        _translate = QtCore.QCoreApplication.translate
        MainOfflineGUIWidget.setWindowTitle(_translate("MainOfflineGUIWidget", "Form"))
        self.label_2.setText(_translate("MainOfflineGUIWidget", "CaImAn Offline"))
        self.pushButtonNewBatch.setText(_translate("MainOfflineGUIWidget", "New Batch"))
        self.pushButtonOpenBatch.setText(_translate("MainOfflineGUIWidget", "Open Batch"))
        self.pushButtonOpenMovie.setText(_translate("MainOfflineGUIWidget", "Open Movie"))
        self.groupBox.setTitle(_translate("MainOfflineGUIWidget", "Parameter Setting"))
        self.pushButtonParamsMCorr.setText(_translate("MainOfflineGUIWidget", "MCorr"))
        self.pushButtonParamsCNMF.setText(_translate("MainOfflineGUIWidget", "CNMF"))
        self.pushButtonParamsCNMFE.setText(_translate("MainOfflineGUIWidget", "CNMFE"))
        self.pushButtonStart.setToolTip(_translate("MainOfflineGUIWidget", "Run the batch from the first item"))
        self.pushButtonStart.setText(_translate("MainOfflineGUIWidget", "Start"))
        self.pushButtonStartItem.setToolTip(_translate("MainOfflineGUIWidget", "Run the batch from the currently selected item"))
        self.pushButtonStartItem.setText(_translate("MainOfflineGUIWidget", "Start at item"))
        self.pushButtonDelItem.setText(_translate("MainOfflineGUIWidget", "Del Item"))
        self.pushButtonAbort.setText(_translate("MainOfflineGUIWidget", "Abort"))
        self.label.setText(_translate("MainOfflineGUIWidget", "Items"))
        self.listWidgetItems.setToolTip(_translate("MainOfflineGUIWidget", "List of items in current batch"))
        self.groupBox_2.setToolTip(_translate("MainOfflineGUIWidget", "Click an item and use post-processing tools"))
        self.groupBox_2.setTitle(_translate("MainOfflineGUIWidget", "Post-processing"))
        self.comboBoxProjectionOpts.setToolTip(_translate("MainOfflineGUIWidget", "Type of projections to show"))
        self.comboBoxProjectionOpts.setItemText(0, _translate("MainOfflineGUIWidget", "mean"))
        self.comboBoxProjectionOpts.setItemText(1, _translate("MainOfflineGUIWidget", "std"))
        self.comboBoxProjectionOpts.setItemText(2, _translate("MainOfflineGUIWidget", "max"))
        self.pushButtonViewProjection.setToolTip(_translate("MainOfflineGUIWidget", "View the mean/std/max Projection (for motion correction) \n"
"and/or Correlation Image (for CNMF)."))
        self.pushButtonViewProjection.setText(_translate("MainOfflineGUIWidget", "View Proj/Corr"))
        self.pushButtonEvalComponents.setToolTip(_translate("MainOfflineGUIWidget", "Open GUI for component evaluation"))
        self.pushButtonEvalComponents.setText(_translate("MainOfflineGUIWidget", "Eval Comps"))
        self.textBrowserParams.setToolTip(_translate("MainOfflineGUIWidget", "Parameters for the currently selected batch item"))
        self.textBrowserStdOut.setToolTip(_translate("MainOfflineGUIWidget", "stdout and stderr from externally running QProcess"))
