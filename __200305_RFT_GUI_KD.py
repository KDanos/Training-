# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '__200305_RFT_GUI_KD.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 967)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget_Master = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget_Master.setObjectName("treeWidget_Master")
        self.treeWidget_Master.headerItem().setText(0, "1")
        self.frame_all_data = QtWidgets.QFrame(self.splitter)
        self.frame_all_data.setStyleSheet("color = rgb(255, 255, 255)")
        self.frame_all_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_all_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_all_data.setObjectName("frame_all_data")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_all_data)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_all_data)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_plots_w_widgets = QtWidgets.QFrame(self.splitter_2)
        self.frame_plots_w_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plots_w_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plots_w_widgets.setObjectName("frame_plots_w_widgets")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_plots_w_widgets)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_3 = QtWidgets.QSplitter(self.frame_plots_w_widgets)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.frame_plot_widgets = QtWidgets.QFrame(self.splitter_3)
        self.frame_plot_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot_widgets.setObjectName("frame_plot_widgets")
        self.frame_plots = QtWidgets.QFrame(self.splitter_3)
        self.frame_plots.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plots.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plots.setObjectName("frame_plots")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_plots)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_Pressure_Plot = QtWidgets.QFrame(self.frame_plots)
        self.frame_Pressure_Plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Pressure_Plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Pressure_Plot.setObjectName("frame_Pressure_Plot")
        self.horizontalLayout_7.addWidget(self.frame_Pressure_Plot)
        self.frame_Excess_Pressure = QtWidgets.QFrame(self.frame_plots)
        self.frame_Excess_Pressure.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Excess_Pressure.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Excess_Pressure.setObjectName("frame_Excess_Pressure")
        self.horizontalLayout_7.addWidget(self.frame_Excess_Pressure)
        self.frame_Logs_Plot = QtWidgets.QFrame(self.frame_plots)
        self.frame_Logs_Plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Logs_Plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Logs_Plot.setObjectName("frame_Logs_Plot")
        self.horizontalLayout_7.addWidget(self.frame_Logs_Plot)
        self.horizontalLayout_3.addWidget(self.splitter_3)
        self.frame_tables_w_widgets = QtWidgets.QFrame(self.splitter_2)
        self.frame_tables_w_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tables_w_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tables_w_widgets.setObjectName("frame_tables_w_widgets")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_tables_w_widgets)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_tables_w_widgets)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.frame_stations_w_widgets = QtWidgets.QFrame(self.splitter_4)
        self.frame_stations_w_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_stations_w_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_stations_w_widgets.setObjectName("frame_stations_w_widgets")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_stations_w_widgets)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter_5 = QtWidgets.QSplitter(self.frame_stations_w_widgets)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.treeWidget_Stations = QtWidgets.QTreeWidget(self.splitter_5)
        self.treeWidget_Stations.setObjectName("treeWidget_Stations")
        self.treeWidget_Stations.headerItem().setText(0, "1")
        self.tableWidget_Stations = QtWidgets.QTableWidget(self.splitter_5)
        self.tableWidget_Stations.setObjectName("tableWidget_Stations")
        self.tableWidget_Stations.setColumnCount(0)
        self.tableWidget_Stations.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.splitter_5)
        self.frame_samples_w_widgets = QtWidgets.QFrame(self.splitter_4)
        self.frame_samples_w_widgets.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_samples_w_widgets.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_samples_w_widgets.setObjectName("frame_samples_w_widgets")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_samples_w_widgets)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.splitter_6 = QtWidgets.QSplitter(self.frame_samples_w_widgets)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.treeWidget_Samples = QtWidgets.QTreeWidget(self.splitter_6)
        self.treeWidget_Samples.setObjectName("treeWidget_Samples")
        self.treeWidget_Samples.headerItem().setText(0, "1")
        self.tableWidget_Samples = QtWidgets.QTableWidget(self.splitter_6)
        self.tableWidget_Samples.setObjectName("tableWidget_Samples")
        self.tableWidget_Samples.setColumnCount(0)
        self.tableWidget_Samples.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.splitter_6)
        self.horizontalLayout_4.addWidget(self.splitter_4)
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

