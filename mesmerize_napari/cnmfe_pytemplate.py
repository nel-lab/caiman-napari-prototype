# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/cnmfe_template_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CNMFEDockWidget(object):
    def setupUi(self, CNMFEDockWidget):
        CNMFEDockWidget.setObjectName("CNMFEDockWidget")
        CNMFEDockWidget.setWindowModality(QtCore.Qt.NonModal)
        CNMFEDockWidget.resize(701, 720)
        CNMFEDockWidget.setFloating(True)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.dockWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxGSig = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxGSig.setMinimum(2)
        self.spinBoxGSig.setMaximum(998)
        self.spinBoxGSig.setSingleStep(1)
        self.spinBoxGSig.setProperty("value", 10)
        self.spinBoxGSig.setObjectName("spinBoxGSig")
        self.horizontalLayout.addWidget(self.spinBoxGSig)
        self.spinBoxDownsample = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxDownsample.setProperty("value", 1)
        self.spinBoxDownsample.setObjectName("spinBoxDownsample")
        self.horizontalLayout.addWidget(self.spinBoxDownsample)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdCorrPNRName = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdCorrPNRName.setObjectName("lineEdCorrPNRName")
        self.horizontalLayout_3.addWidget(self.lineEdCorrPNRName)
        self.btnAddToBatchCorrPNR = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnAddToBatchCorrPNR.setObjectName("btnAddToBatchCorrPNR")
        self.horizontalLayout_3.addWidget(self.btnAddToBatchCorrPNR)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_20 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEditAin = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEditAin.setObjectName("lineEditAin")
        self.horizontalLayout_2.addWidget(self.lineEditAin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.spinBox_p = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox_p.setProperty("value", 1)
        self.spinBox_p.setObjectName("spinBox_p")
        self.horizontalLayout_12.addWidget(self.spinBox_p)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.label_7 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.doubleSpinBoxMinCorr = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBoxMinCorr.setDecimals(3)
        self.doubleSpinBoxMinCorr.setMaximum(1.0)
        self.doubleSpinBoxMinCorr.setSingleStep(0.005)
        self.doubleSpinBoxMinCorr.setProperty("value", 0.89)
        self.doubleSpinBoxMinCorr.setObjectName("doubleSpinBoxMinCorr")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxMinCorr)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.spinBoxMinPNR = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxMinPNR.setMaximum(999)
        self.spinBoxMinPNR.setProperty("value", 4)
        self.spinBoxMinPNR.setObjectName("spinBoxMinPNR")
        self.horizontalLayout_7.addWidget(self.spinBoxMinPNR)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_13 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_24 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        self.spinBoxRf = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxRf.setMaximum(999)
        self.spinBoxRf.setProperty("value", 50)
        self.spinBoxRf.setObjectName("spinBoxRf")
        self.horizontalLayout_13.addWidget(self.spinBoxRf)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.label_25 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_26 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_18.addWidget(self.label_26)
        self.spinBoxOverlap = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxOverlap.setMaximum(999)
        self.spinBoxOverlap.setProperty("value", 30)
        self.spinBoxOverlap.setObjectName("spinBoxOverlap")
        self.horizontalLayout_18.addWidget(self.spinBoxOverlap)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_18.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_18)
        self.label_28 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_27 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_19.addWidget(self.label_27)
        self.spinBoxGnb = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxGnb.setMinimum(-1)
        self.spinBoxGnb.setMaximum(99)
        self.spinBoxGnb.setProperty("value", 0)
        self.spinBoxGnb.setObjectName("spinBoxGnb")
        self.horizontalLayout_19.addWidget(self.spinBoxGnb)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_19.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.label_30 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_29 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_20.addWidget(self.label_29)
        self.spinBoxNb_patch = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxNb_patch.setMinimum(-1)
        self.spinBoxNb_patch.setProperty("value", 0)
        self.spinBoxNb_patch.setObjectName("spinBoxNb_patch")
        self.horizontalLayout_20.addWidget(self.spinBoxNb_patch)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_20.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.label_32 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_2.addWidget(self.label_32)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_31 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_21.addWidget(self.label_31)
        self.spinBoxK = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBoxK.setMinimum(0)
        self.spinBoxK.setProperty("value", 10)
        self.spinBoxK.setObjectName("spinBoxK")
        self.horizontalLayout_21.addWidget(self.spinBoxK)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_21.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2
        )
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_35 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_23.addWidget(self.label_35)
        self.spinBox_ssub = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox_ssub.setMinimum(1)
        self.spinBox_ssub.setProperty("value", 1)
        self.spinBox_ssub.setObjectName("spinBox_ssub")
        self.horizontalLayout_23.addWidget(self.spinBox_ssub)
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_23.addWidget(self.line)
        self.label_36 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_23.addWidget(self.label_36)
        self.spinBox_tsub = QtWidgets.QSpinBox(self.dockWidgetContents)
        self.spinBox_tsub.setMinimum(1)
        self.spinBox_tsub.setSingleStep(1)
        self.spinBox_tsub.setProperty("value", 1)
        self.spinBox_tsub.setObjectName("spinBox_tsub")
        self.horizontalLayout_23.addWidget(self.spinBox_tsub)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_23.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_23)
        self.checkBox_low_rank_background = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBox_low_rank_background.setObjectName("checkBox_low_rank_background")
        self.verticalLayout.addWidget(self.checkBox_low_rank_background)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.doubleSpinBox_ring_size_factor = QtWidgets.QDoubleSpinBox(
            self.dockWidgetContents
        )
        self.doubleSpinBox_ring_size_factor.setSingleStep(0.1)
        self.doubleSpinBox_ring_size_factor.setProperty("value", 1.5)
        self.doubleSpinBox_ring_size_factor.setObjectName(
            "doubleSpinBox_ring_size_factor"
        )
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_ring_size_factor)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBoxDeconv = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxDeconv.setObjectName("comboBoxDeconv")
        self.comboBoxDeconv.addItem("")
        self.comboBoxDeconv.addItem("")
        self.comboBoxDeconv.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxDeconv)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_22 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_14.addWidget(self.label_22)
        self.doubleSpinBoxMergeThresh = QtWidgets.QDoubleSpinBox(
            self.dockWidgetContents
        )
        self.doubleSpinBoxMergeThresh.setMaximum(1.0)
        self.doubleSpinBoxMergeThresh.setSingleStep(0.05)
        self.doubleSpinBoxMergeThresh.setProperty("value", 0.7)
        self.doubleSpinBoxMergeThresh.setObjectName("doubleSpinBoxMergeThresh")
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxMergeThresh)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_14.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.groupBox_cnmf_kwargs = QtWidgets.QGroupBox(self.dockWidgetContents)
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
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.checkBoxKeepMemmap = QtWidgets.QCheckBox(self.dockWidgetContents)
        self.checkBoxKeepMemmap.setObjectName("checkBoxKeepMemmap")
        self.verticalLayout.addWidget(self.checkBoxKeepMemmap)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.lineEdName = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdName.setObjectName("lineEdName")
        self.horizontalLayout_11.addWidget(self.lineEdName)
        self.btnAddToBatchCNMFE = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btnAddToBatchCNMFE.setObjectName("btnAddToBatchCNMFE")
        self.horizontalLayout_11.addWidget(self.btnAddToBatchCNMFE)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout
        )
        CNMFEDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(CNMFEDockWidget)
        self.lineEdName.returnPressed.connect(self.btnAddToBatchCNMFE.click)
        QtCore.QMetaObject.connectSlotsByName(CNMFEDockWidget)
        CNMFEDockWidget.setTabOrder(self.spinBoxGSig, self.spinBoxDownsample)
        CNMFEDockWidget.setTabOrder(self.spinBoxDownsample, self.lineEdCorrPNRName)
        CNMFEDockWidget.setTabOrder(self.lineEdCorrPNRName, self.btnAddToBatchCorrPNR)
        CNMFEDockWidget.setTabOrder(self.btnAddToBatchCorrPNR, self.lineEditAin)
        CNMFEDockWidget.setTabOrder(self.lineEditAin, self.spinBox_p)
        CNMFEDockWidget.setTabOrder(self.spinBox_p, self.doubleSpinBoxMinCorr)
        CNMFEDockWidget.setTabOrder(self.doubleSpinBoxMinCorr, self.spinBoxMinPNR)
        CNMFEDockWidget.setTabOrder(self.spinBoxMinPNR, self.spinBoxRf)
        CNMFEDockWidget.setTabOrder(self.spinBoxRf, self.spinBoxOverlap)
        CNMFEDockWidget.setTabOrder(self.spinBoxOverlap, self.spinBoxGnb)
        CNMFEDockWidget.setTabOrder(self.spinBoxGnb, self.spinBoxNb_patch)
        CNMFEDockWidget.setTabOrder(self.spinBoxNb_patch, self.spinBoxK)
        CNMFEDockWidget.setTabOrder(self.spinBoxK, self.spinBox_ssub)
        CNMFEDockWidget.setTabOrder(self.spinBox_ssub, self.spinBox_tsub)
        CNMFEDockWidget.setTabOrder(
            self.spinBox_tsub, self.checkBox_low_rank_background
        )
        CNMFEDockWidget.setTabOrder(
            self.checkBox_low_rank_background, self.doubleSpinBox_ring_size_factor
        )
        CNMFEDockWidget.setTabOrder(
            self.doubleSpinBox_ring_size_factor, self.comboBoxDeconv
        )
        CNMFEDockWidget.setTabOrder(self.comboBoxDeconv, self.doubleSpinBoxMergeThresh)
        CNMFEDockWidget.setTabOrder(
            self.doubleSpinBoxMergeThresh, self.groupBox_cnmf_kwargs
        )
        CNMFEDockWidget.setTabOrder(
            self.groupBox_cnmf_kwargs, self.plainTextEdit_cnmf_kwargs
        )
        CNMFEDockWidget.setTabOrder(
            self.plainTextEdit_cnmf_kwargs, self.checkBoxKeepMemmap
        )
        CNMFEDockWidget.setTabOrder(self.checkBoxKeepMemmap, self.lineEdName)
        CNMFEDockWidget.setTabOrder(self.lineEdName, self.btnAddToBatchCNMFE)

    def retranslateUi(self, CNMFEDockWidget):
        _translate = QtCore.QCoreApplication.translate
        CNMFEDockWidget.setWindowTitle(_translate("CNMFEDockWidget", "CNMF-E Params"))
        self.label_5.setToolTip(
            _translate(
                "CNMFEDockWidget",
                "Compute some summary images (correlation and peak to noise ratio)",
            )
        )
        self.label_5.setText(
            _translate("CNMFEDockWidget", "Inspect Correlation and PNR")
        )
        self.label_2.setText(
            _translate(
                "CNMFEDockWidget",
                "gaussian width of a 2D gaussian kernel, which approximates \n"
                " a neuron 3 times less than the average diameters\n"
                " of a neuron (pixels)",
            )
        )
        self.label.setText(_translate("CNMFEDockWidget", "gSig:"))
        self.label_9.setText(_translate("CNMFEDockWidget", "Stop here:"))
        self.lineEdCorrPNRName.setPlaceholderText(
            _translate("CNMFEDockWidget", "Enter name")
        )
        self.btnAddToBatchCorrPNR.setText(_translate("CNMFEDockWidget", "Add to batch"))
        self.label_20.setText(_translate("CNMFEDockWidget", "CNMF-E"))
        self.label_3.setText(_translate("CNMFEDockWidget", "Ain:"))
        self.label_19.setText(_translate("CNMFEDockWidget", "p:"))
        self.label_7.setText(
            _translate("CNMFEDockWidget", "Minimum correlation of peak")
        )
        self.label_8.setText(_translate("CNMFEDockWidget", "min_corr:"))
        self.label_11.setText(
            _translate("CNMFEDockWidget", "Minimum peak to noise ratio")
        )
        self.label_10.setText(_translate("CNMFEDockWidget", "min_pnr:"))
        self.label_13.setText(
            _translate(
                "CNMFEDockWidget", "Adaptive way to set threshold on the transient size"
            )
        )
        self.label_24.setText(_translate("CNMFEDockWidget", "Half size of patch"))
        self.label_21.setText(_translate("CNMFEDockWidget", "rf:"))
        self.label_25.setText(
            _translate(
                "CNMFEDockWidget",
                "Overlap of patches (at least 4 times the size of a neuron/cell)",
            )
        )
        self.label_26.setText(_translate("CNMFEDockWidget", "overlap:"))
        self.label_28.setText(
            _translate("CNMFEDockWidget", "Global number of background components")
        )
        self.label_27.setText(_translate("CNMFEDockWidget", "gnb:"))
        self.label_30.setText(
            _translate("CNMFEDockWidget", "Background components per patch")
        )
        self.label_29.setText(_translate("CNMFEDockWidget", "nb_patch:"))
        self.label_32.setText(
            _translate("CNMFEDockWidget", "Number of neurons/cell per patch")
        )
        self.label_31.setText(_translate("CNMFEDockWidget", "k:"))
        self.label_35.setText(_translate("CNMFEDockWidget", "ssub:"))
        self.label_36.setText(_translate("CNMFEDockWidget", "tsub:"))
        self.checkBox_low_rank_background.setText(
            _translate("CNMFEDockWidget", "low_rank_background")
        )
        self.label_6.setText(_translate("CNMFEDockWidget", "ring_size_factor:"))
        self.label_4.setText(_translate("CNMFEDockWidget", "deconvolution: "))
        self.comboBoxDeconv.setItemText(0, _translate("CNMFEDockWidget", "oasis"))
        self.comboBoxDeconv.setItemText(1, _translate("CNMFEDockWidget", "cvxpy"))
        self.comboBoxDeconv.setItemText(2, _translate("CNMFEDockWidget", "SKIP"))
        self.label_22.setText(_translate("CNMFEDockWidget", "merge_thresh:"))
        self.groupBox_cnmf_kwargs.setToolTip(
            _translate(
                "CNMFEDockWidget",
                "You can enter additional kwargs to pass for CNMF instantiation.\n"
                "Use single quotes for strings, do not use double quotes.",
            )
        )
        self.groupBox_cnmf_kwargs.setTitle(
            _translate("CNMFEDockWidget", "Use CNMF &kwargs")
        )
        self.plainTextEdit_cnmf_kwargs.setToolTip(
            _translate(
                "CNMFEDockWidget",
                "You can enter additional kwargs to pass for CNMF instantiation.\n"
                "Use single quotes for strings, do not use double quotes.",
            )
        )
        self.checkBoxKeepMemmap.setText(_translate("CNMFEDockWidget", "Keep memmap"))
        self.label_18.setText(_translate("CNMFEDockWidget", "Perform CNMF-E:"))
        self.lineEdName.setPlaceholderText(_translate("CNMFEDockWidget", "Enter name"))
        self.btnAddToBatchCNMFE.setText(_translate("CNMFEDockWidget", "Add to batch"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CNMFEDockWidget = QtWidgets.QDockWidget()
    ui = Ui_CNMFEDockWidget()
    ui.setupUi(CNMFEDockWidget)
    CNMFEDockWidget.show()
    sys.exit(app.exec_())
