# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './cnmf_template.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CNMFParmsWindow(object):
    def setupUi(self, CNMFParmsWindow):
        CNMFParmsWindow.setObjectName("CNMFParmsWindow")
        CNMFParmsWindow.resize(699, 726)
        self.centralwidget = QtWidgets.QWidget(CNMFParmsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxP = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxP.setMinimum(0)
        self.spinBoxP.setMaximum(10)
        self.spinBoxP.setSingleStep(1)
        self.spinBoxP.setProperty("value", 2)
        self.spinBoxP.setObjectName("spinBoxP")
        self.horizontalLayout.addWidget(self.spinBoxP)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout.addWidget(self.label_28)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_19.addWidget(self.label_27)
        self.spinBoxnb = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxnb.setMaximum(99)
        self.spinBoxnb.setProperty("value", 1)
        self.spinBoxnb.setObjectName("spinBoxnb")
        self.horizontalLayout_19.addWidget(self.spinBoxnb)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_19.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.doubleSpinBoxMergeThresh = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxMergeThresh.setMaximum(1.0)
        self.doubleSpinBoxMergeThresh.setSingleStep(0.05)
        self.doubleSpinBoxMergeThresh.setProperty("value", 0.7)
        self.doubleSpinBoxMergeThresh.setObjectName("doubleSpinBoxMergeThresh")
        self.horizontalLayout_7.addWidget(self.doubleSpinBoxMergeThresh)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        self.spinBoxRf = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxRf.setMaximum(999)
        self.spinBoxRf.setProperty("value", 50)
        self.spinBoxRf.setObjectName("spinBoxRf")
        self.horizontalLayout_13.addWidget(self.spinBoxRf)
        self.checkBoxRfNone = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxRfNone.setObjectName("checkBoxRfNone")
        self.horizontalLayout_13.addWidget(self.checkBoxRfNone)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.spinBoxStrideCNMF = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxStrideCNMF.setMaximum(999)
        self.spinBoxStrideCNMF.setProperty("value", 30)
        self.spinBoxStrideCNMF.setObjectName("spinBoxStrideCNMF")
        self.horizontalLayout_8.addWidget(self.spinBoxStrideCNMF)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_21.addWidget(self.label_31)
        self.spinBoxK = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxK.setMinimum(1)
        self.spinBoxK.setProperty("value", 10)
        self.spinBoxK.setObjectName("spinBoxK")
        self.horizontalLayout_21.addWidget(self.spinBoxK)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_21.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setObjectName("label_33")
        self.verticalLayout.addWidget(self.label_33)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_22.addWidget(self.label_34)
        self.spinBox_gSig_x = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_gSig_x.setMinimum(1)
        self.spinBox_gSig_x.setProperty("value", 5)
        self.spinBox_gSig_x.setObjectName("spinBox_gSig_x")
        self.horizontalLayout_22.addWidget(self.spinBox_gSig_x)
        self.spinBox_gSig_y = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_gSig_y.setMinimum(1)
        self.spinBox_gSig_y.setProperty("value", 5)
        self.spinBox_gSig_y.setObjectName("spinBox_gSig_y")
        self.horizontalLayout_22.addWidget(self.spinBox_gSig_y)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_22.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_22.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_23.addWidget(self.label_35)
        self.spinBox_ssub = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ssub.setMinimum(1)
        self.spinBox_ssub.setProperty("value", 1)
        self.spinBox_ssub.setObjectName("spinBox_ssub")
        self.horizontalLayout_23.addWidget(self.spinBox_ssub)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_23.addWidget(self.line)
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_23.addWidget(self.label_36)
        self.spinBox_tsub = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_tsub.setMinimum(1)
        self.spinBox_tsub.setSingleStep(1)
        self.spinBox_tsub.setProperty("value", 1)
        self.spinBox_tsub.setObjectName("spinBox_tsub")
        self.horizontalLayout_23.addWidget(self.spinBox_tsub)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_23.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_method_init = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_method_init.setObjectName("comboBox_method_init")
        self.comboBox_method_init.addItem("")
        self.comboBox_method_init.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_method_init)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox_cnmf_kwargs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_cnmf_kwargs.setStatusTip("")
        self.groupBox_cnmf_kwargs.setCheckable(True)
        self.groupBox_cnmf_kwargs.setChecked(False)
        self.groupBox_cnmf_kwargs.setObjectName("groupBox_cnmf_kwargs")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_cnmf_kwargs)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit_cnmf_kwargs = QtWidgets.QPlainTextEdit(
            self.groupBox_cnmf_kwargs
        )
        self.plainTextEdit_cnmf_kwargs.setObjectName("plainTextEdit_cnmf_kwargs")
        self.verticalLayout_3.addWidget(self.plainTextEdit_cnmf_kwargs)
        self.verticalLayout.addWidget(self.groupBox_cnmf_kwargs)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_14.addWidget(self.label_23)
        self.doubleSpinBoxMinSNR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxMinSNR.setMaximum(100.0)
        self.doubleSpinBoxMinSNR.setSingleStep(0.25)
        self.doubleSpinBoxMinSNR.setProperty("value", 2.5)
        self.doubleSpinBoxMinSNR.setObjectName("doubleSpinBoxMinSNR")
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxMinSNR)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_14.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.doubleSpinBoxRvalThr = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRvalThr.setMaximum(1.0)
        self.doubleSpinBoxRvalThr.setSingleStep(0.05)
        self.doubleSpinBoxRvalThr.setProperty("value", 0.8)
        self.doubleSpinBoxRvalThr.setObjectName("doubleSpinBoxRvalThr")
        self.horizontalLayout_9.addWidget(self.doubleSpinBoxRvalThr)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_9.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.checkBoxUseCNN = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxUseCNN.setChecked(True)
        self.checkBoxUseCNN.setObjectName("checkBoxUseCNN")
        self.horizontalLayout_15.addWidget(self.checkBoxUseCNN)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_15.addWidget(self.line_2)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_15.addWidget(self.label_26)
        self.doubleSpinBoxCNNThr = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxCNNThr.setMaximum(1.0)
        self.doubleSpinBoxCNNThr.setSingleStep(0.05)
        self.doubleSpinBoxCNNThr.setProperty("value", 0.8)
        self.doubleSpinBoxCNNThr.setObjectName("doubleSpinBoxCNNThr")
        self.horizontalLayout_15.addWidget(self.doubleSpinBoxCNNThr)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        self.doubleSpinBox_cnn_lowest = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_cnn_lowest.setMaximum(1.0)
        self.doubleSpinBox_cnn_lowest.setSingleStep(0.05)
        self.doubleSpinBox_cnn_lowest.setProperty("value", 0.1)
        self.doubleSpinBox_cnn_lowest.setObjectName("doubleSpinBox_cnn_lowest")
        self.horizontalLayout_15.addWidget(self.doubleSpinBox_cnn_lowest)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_15.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.spinBoxDecayTime = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBoxDecayTime.setSingleStep(0.5)
        self.spinBoxDecayTime.setProperty("value", 1.0)
        self.spinBoxDecayTime.setObjectName("spinBoxDecayTime")
        self.horizontalLayout_10.addWidget(self.spinBoxDecayTime)
        spacerItem13 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_10.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox)
        spacerItem14 = QtWidgets.QSpacerItem(37, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox_eval_kwargs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_eval_kwargs.setCheckable(True)
        self.groupBox_eval_kwargs.setChecked(False)
        self.groupBox_eval_kwargs.setObjectName("groupBox_eval_kwargs")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_eval_kwargs)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.plainTextEdit_eval_kwargs = QtWidgets.QPlainTextEdit(
            self.groupBox_eval_kwargs
        )
        self.plainTextEdit_eval_kwargs.setObjectName("plainTextEdit_eval_kwargs")
        self.verticalLayout_5.addWidget(self.plainTextEdit_eval_kwargs)
        self.verticalLayout_2.addWidget(self.groupBox_eval_kwargs)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_5.addWidget(self.label_29)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.comboBox)
        spacerItem15 = QtWidgets.QSpacerItem(34, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxRefit = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxRefit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBoxRefit.setChecked(True)
        self.checkBoxRefit.setObjectName("checkBoxRefit")
        self.horizontalLayout_2.addWidget(self.checkBoxRefit)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdName.setObjectName("lineEdName")
        self.horizontalLayout_11.addWidget(self.lineEdName)
        self.btnAddToBatchCNMF = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddToBatchCNMF.setObjectName("btnAddToBatchCNMF")
        self.horizontalLayout_11.addWidget(self.btnAddToBatchCNMF)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        CNMFParmsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CNMFParmsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 30))
        self.menubar.setObjectName("menubar")
        CNMFParmsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CNMFParmsWindow)
        self.statusbar.setObjectName("statusbar")
        CNMFParmsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CNMFParmsWindow)
        QtCore.QMetaObject.connectSlotsByName(CNMFParmsWindow)
        CNMFParmsWindow.setTabOrder(self.spinBoxP, self.spinBoxnb)
        CNMFParmsWindow.setTabOrder(self.spinBoxnb, self.doubleSpinBoxMergeThresh)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBoxMergeThresh, self.spinBoxRf)
        CNMFParmsWindow.setTabOrder(self.spinBoxRf, self.checkBoxRfNone)
        CNMFParmsWindow.setTabOrder(self.checkBoxRfNone, self.spinBoxStrideCNMF)
        CNMFParmsWindow.setTabOrder(self.spinBoxStrideCNMF, self.spinBoxK)
        CNMFParmsWindow.setTabOrder(self.spinBoxK, self.spinBox_gSig_x)
        CNMFParmsWindow.setTabOrder(self.spinBox_gSig_x, self.spinBox_gSig_y)
        CNMFParmsWindow.setTabOrder(self.spinBox_gSig_y, self.spinBox_ssub)
        CNMFParmsWindow.setTabOrder(self.spinBox_ssub, self.spinBox_tsub)
        CNMFParmsWindow.setTabOrder(self.spinBox_tsub, self.comboBox_method_init)
        CNMFParmsWindow.setTabOrder(self.comboBox_method_init, self.groupBox_cnmf_kwargs)
        CNMFParmsWindow.setTabOrder(self.groupBox_cnmf_kwargs, self.plainTextEdit_cnmf_kwargs)
        CNMFParmsWindow.setTabOrder(self.plainTextEdit_cnmf_kwargs, self.doubleSpinBoxMinSNR)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBoxMinSNR, self.doubleSpinBoxRvalThr)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBoxRvalThr, self.checkBoxUseCNN)
        CNMFParmsWindow.setTabOrder(self.checkBoxUseCNN, self.doubleSpinBoxCNNThr)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBoxCNNThr, self.doubleSpinBox_cnn_lowest)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBox_cnn_lowest, self.spinBoxDecayTime)
        CNMFParmsWindow.setTabOrder(self.spinBoxDecayTime, self.doubleSpinBox)
        CNMFParmsWindow.setTabOrder(self.doubleSpinBox, self.groupBox_eval_kwargs)
        CNMFParmsWindow.setTabOrder(self.groupBox_eval_kwargs, self.plainTextEdit_eval_kwargs)
        CNMFParmsWindow.setTabOrder(self.plainTextEdit_eval_kwargs, self.comboBox)
        CNMFParmsWindow.setTabOrder(self.comboBox, self.checkBoxRefit)
        CNMFParmsWindow.setTabOrder(self.checkBoxRefit, self.lineEdName)
        CNMFParmsWindow.setTabOrder(self.lineEdName, self.btnAddToBatchCNMF)

    def retranslateUi(self, CNMFParmsWindow):
        _translate = QtCore.QCoreApplication.translate
        CNMFParmsWindow.setWindowTitle(_translate("CNMFParmsWindow", "cnmf params"))
        self.label_22.setText(_translate("CNMFParmsWindow", "Order of the autoregressive system"))
        self.label.setText(_translate("CNMFParmsWindow", "p:"))
        self.label_28.setText(_translate("CNMFParmsWindow", "Global number of background components"))
        self.label_27.setText(_translate("CNMFParmsWindow", "nb:"))
        self.label_11.setText(_translate("CNMFParmsWindow", "Merging threshold, max correlation allowed"))
        self.label_10.setText(_translate("CNMFParmsWindow", "merge_thresh:"))
        self.label_24.setText(_translate("CNMFParmsWindow", "Half size of patch in pixels"))
        self.label_21.setText(_translate("CNMFParmsWindow", "rf:"))
        self.checkBoxRfNone.setToolTip(_translate("CNMFParmsWindow", "Set `rf` as `None`"))
        self.checkBoxRfNone.setText(_translate("CNMFParmsWindow", "None"))
        self.label_13.setText(_translate("CNMFParmsWindow", "amount of overlap between the patches in pixels"))
        self.label_12.setText(_translate("CNMFParmsWindow", "stride_cnmf:"))
        self.label_32.setText(_translate("CNMFParmsWindow", "Number of neurons/cell per patch"))
        self.label_31.setText(_translate("CNMFParmsWindow", "K:"))
        self.label_33.setText(_translate("CNMFParmsWindow", "Expected half size of neurons (x, y)"))
        self.label_34.setText(_translate("CNMFParmsWindow", "gSig:"))
        self.label_35.setText(_translate("CNMFParmsWindow", "ssub:"))
        self.label_36.setText(_translate("CNMFParmsWindow", "tsub:"))
        self.label_4.setText(_translate("CNMFParmsWindow", "method_init"))
        self.comboBox_method_init.setItemText(0, _translate("CNMFParmsWindow", "greedy_roi"))
        self.comboBox_method_init.setItemText(1, _translate("CNMFParmsWindow", "sparse_nmf"))
        self.groupBox_cnmf_kwargs.setToolTip(_translate("CNMFParmsWindow", "You can enter additional kwargs to pass for CNMF instantiation.\n"
"Use single quotes for strings, do not use double quotes."))
        self.groupBox_cnmf_kwargs.setTitle(_translate("CNMFParmsWindow", "&Use additional CNMF params"))
        self.plainTextEdit_cnmf_kwargs.setToolTip(_translate("CNMFParmsWindow", "You can enter additional kwargs to pass for CNMF instantiation.\n"
"Use single quotes for strings, do not use double quotes."))
        self.label_20.setText(_translate("CNMFParmsWindow", "Signal to noise ratio for accepting a component"))
        self.label_23.setText(_translate("CNMFParmsWindow", "min_SNR:"))
        self.label_14.setText(_translate("CNMFParmsWindow", "Space correlation threshold for accepting a component"))
        self.label_15.setText(_translate("CNMFParmsWindow", "rval_thr:"))
        self.label_25.setText(_translate("CNMFParmsWindow", "Threshold for CNN based classifier"))
        self.checkBoxUseCNN.setText(_translate("CNMFParmsWindow", "use_cnn"))
        self.label_26.setText(_translate("CNMFParmsWindow", "cnn_thr:"))
        self.label_3.setText(_translate("CNMFParmsWindow", "cnn_lowest"))
        self.label_17.setText(_translate("CNMFParmsWindow", "Average decay time of calcium spikes (seconds)"))
        self.label_16.setText(_translate("CNMFParmsWindow", "decay_time:"))
        self.label_19.setText(_translate("CNMFParmsWindow", "framerate of video"))
        self.label_18.setText(_translate("CNMFParmsWindow", "frate:"))
        self.groupBox_eval_kwargs.setToolTip(_translate("CNMFParmsWindow", "You can enter additional parameters to use for component evaluation.\n"
"Use single quotes for strings, do not use double quotes"))
        self.groupBox_eval_kwargs.setTitle(_translate("CNMFParmsWindow", "Use additional &quality (evaluation) params"))
        self.plainTextEdit_eval_kwargs.setToolTip(_translate("CNMFParmsWindow", "You can enter additional parameters to use for component evaluation.\n"
"Use single quotes for strings, do not use double quotes"))
        self.label_29.setText(_translate("CNMFParmsWindow", "input movie:"))
        self.label_2.setText(_translate("CNMFParmsWindow", "perform second iteration of cnmf by re-fitting the components"))
        self.checkBoxRefit.setText(_translate("CNMFParmsWindow", "refit"))
        self.lineEdName.setPlaceholderText(_translate("CNMFParmsWindow", "Enter name"))
        self.btnAddToBatchCNMF.setText(_translate("CNMFParmsWindow", "Add to batch"))
