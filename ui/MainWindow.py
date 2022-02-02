# Form implementation generated from reading ui file 'tif2pdf/ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout_2.addWidget(self.dirEdit)
        self.dirSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.dirSelectButton.setObjectName("dirSelectButton")
        self.horizontalLayout_2.addWidget(self.dirSelectButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.selectAllCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.selectAllCheckbox.setObjectName("selectAllCheckbox")
        self.gridLayout.addWidget(self.selectAllCheckbox, 0, 0, 1, 1)
        self.selectedDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedDirLabel.setObjectName("selectedDirLabel")
        self.gridLayout.addWidget(self.selectedDirLabel, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.dirList = QtWidgets.QListWidget(self.centralwidget)
        self.dirList.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.dirList.setObjectName("dirList")
        self.gridLayout.addWidget(self.dirList, 2, 0, 1, 1)
        self.convertedList = QtWidgets.QListWidget(self.centralwidget)
        self.convertedList.setObjectName("convertedList")
        self.gridLayout.addWidget(self.convertedList, 2, 1, 1, 1)
        self.numSelectedLabel = QtWidgets.QLabel(self.centralwidget)
        self.numSelectedLabel.setObjectName("numSelectedLabel")
        self.gridLayout.addWidget(self.numSelectedLabel, 3, 0, 1, 1)
        self.numConvertedLabel = QtWidgets.QLabel(self.centralwidget)
        self.numConvertedLabel.setObjectName("numConvertedLabel")
        self.gridLayout.addWidget(self.numConvertedLabel, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setMinimumSize(QtCore.QSize(35, 0))
        self.progressLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_3.addWidget(self.progressLabel)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setMinimumSize(QtCore.QSize(0, 40))
        self.convertButton.setObjectName("convertButton")
        self.gridLayout_2.addWidget(self.convertButton, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tif2pdf"))
        self.dirEdit.setPlaceholderText(_translate("MainWindow", "Please select a folder"))
        self.dirSelectButton.setText(_translate("MainWindow", "&Select Folder"))
        self.selectAllCheckbox.setText(_translate("MainWindow", "Select All"))
        self.selectedDirLabel.setText(_translate("MainWindow", "Files in:"))
        self.label_3.setText(_translate("MainWindow", "Converted Files"))
        self.dirList.setSortingEnabled(False)
        self.numSelectedLabel.setText(_translate("MainWindow", "0 files selected"))
        self.numConvertedLabel.setText(_translate("MainWindow", "0 files converted"))
        self.progressLabel.setText(_translate("MainWindow", "0%"))
        self.convertButton.setText(_translate("MainWindow", "&Convert Selected Files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
