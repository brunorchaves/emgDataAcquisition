# coding: utf-8

# TODO:
# - message to tell wether recording was successful in finishRecording()
# - separate window to show the signal while recording
# - button to stop recording
# - setting window

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from qwt.plot import QwtPlot
import resources_rc

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1463, 915)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #fafafa")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainBody)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.logBody = QtWidgets.QWidget(self.mainBody)
        self.logBody.setObjectName("logBody")
        self.logBody.setStyleSheet("background-color: #f0f0f0")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.logBody)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.emgBody = QtWidgets.QWidget(self.logBody)
        self.emgBody.setObjectName("emgBody")
        self.emgBody.setStyleSheet("background-color: #fafafa")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.emgBody)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.labelEMGHeader = QtWidgets.QLabel(self.emgBody)
        self.labelEMGHeader.setObjectName("labelEMGHeader")
        self.verticalLayout_11.addWidget(self.labelEMGHeader)
        self.plotEMG = QwtPlot(self.emgBody)
        self.plotEMG.setMaximumSize(QtCore.QSize(600, 300))
        self.plotEMG.setMinimumSize(QtCore.QSize(80, 50))
        self.plotEMG.setObjectName("plotEMG")
        self.verticalLayout_11.addWidget(self.plotEMG)
        self.emgButtonsMenu = QtWidgets.QWidget(self.emgBody)
        self.emgButtonsMenu.setObjectName("emgButtonsMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.emgButtonsMenu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonEMGPrevious = QtWidgets.QPushButton(self.emgButtonsMenu)
        self.buttonEMGPrevious.setObjectName("buttonEMGPrevious")
        self.buttonEMGPrevious.clicked.connect(lambda: self.changeEMGChannelPlot(-1))
        self.horizontalLayout_3.addWidget(self.buttonEMGPrevious)
        self.buttonEMGNext = QtWidgets.QPushButton(self.emgButtonsMenu)
        self.buttonEMGNext.setObjectName("buttonEMGNext")
        self.buttonEMGNext.clicked.connect(lambda: self.changeEMGChannelPlot(1))
        self.horizontalLayout_3.addWidget(self.buttonEMGNext)
        self.verticalLayout_11.addWidget(self.emgButtonsMenu)
        self.verticalLayout_7.addWidget(self.emgBody)
        
        self.imuBody = QtWidgets.QWidget(self.logBody)
        self.imuBody.setObjectName("imuBody")
        self.imuBody.setStyleSheet("background-color: #fafafa")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.imuBody)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelIMUHeader = QtWidgets.QLabel(self.imuBody)
        self.labelIMUHeader.setObjectName("labelIMUHeader")
        self.verticalLayout_9.addWidget(self.labelIMUHeader)
        self.plotIMU = QwtPlot(self.imuBody)
        self.plotIMU.setMaximumSize(QtCore.QSize(600, 300))
        self.plotIMU.setMinimumSize(QtCore.QSize(80, 50))
        self.plotIMU.setObjectName("plotIMU")
        self.verticalLayout_9.addWidget(self.plotIMU)
        self.imuButtonsMenu = QtWidgets.QWidget(self.imuBody)
        self.imuButtonsMenu.setObjectName("imuButtonsMenu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.imuButtonsMenu)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonIMUPrevious = QtWidgets.QPushButton(self.imuButtonsMenu)
        self.buttonIMUPrevious.setObjectName("buttonIMUPrevious")
        self.buttonIMUPrevious.clicked.connect(lambda: self.changeIMUPlot(-1))
        self.horizontalLayout_4.addWidget(self.buttonIMUPrevious)
        self.buttonIMUNext = QtWidgets.QPushButton(self.imuButtonsMenu)
        self.buttonIMUNext.setObjectName("buttonIMUNext")
        self.buttonIMUNext.clicked.connect(lambda: self.changeIMUPlot(1))
        self.horizontalLayout_4.addWidget(self.buttonIMUNext)
        self.verticalLayout_9.addWidget(self.imuButtonsMenu)
        self.verticalLayout_7.addWidget(self.imuBody)
        
        self.buttonConnectBand = QtWidgets.QPushButton(self.logBody)
        self.buttonConnectBand.setObjectName("buttonConnectBand")
        self.verticalLayout_7.addWidget(self.buttonConnectBand)
        
        self.horizontalLayout_5.addWidget(self.logBody)
        
        self.selectPositionBody = QtWidgets.QWidget(self.mainBody)
        self.selectPositionBody.setObjectName("selectPositionBody")
        self.gridLayout = QtWidgets.QGridLayout(self.selectPositionBody)
        self.gridLayout.setObjectName("gridLayout")
        
        self.handOpen = QtWidgets.QWidget(self.selectPositionBody)
        self.handOpen.setObjectName("handOpen")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.handOpen)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelOpen = QtWidgets.QLabel(self.handOpen)
        self.labelOpen.setMaximumSize(QtCore.QSize(100, 100))
        self.labelOpen.setText("")
        self.labelOpen.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/open.png"))
        self.labelOpen.setScaledContents(True)
        self.labelOpen.setObjectName("labelOpen")
        self.verticalLayout_5.addWidget(self.labelOpen)
        self.buttonOpen = QtWidgets.QPushButton(self.handOpen)
        self.buttonOpen.setObjectName("buttonOpen")
        self.buttonOpen.clicked.connect(lambda: self.selectPosition("Open", "Keep your hand relaxed for 15 seconds, them, keep her fully open for more 15 seconds.", ":/positionsGifs/assets/open.gif"))
        self.verticalLayout_5.addWidget(self.buttonOpen)
        self.gridLayout.addWidget(self.handOpen, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.handNaruto = QtWidgets.QWidget(self.selectPositionBody)
        self.handNaruto.setObjectName("handNaruto")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.handNaruto)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelNaruto = QtWidgets.QLabel(self.handNaruto)
        self.labelNaruto.setMaximumSize(QtCore.QSize(100, 100))
        self.labelNaruto.setText("")
        self.labelNaruto.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/naruto.png"))
        self.labelNaruto.setScaledContents(True)
        self.labelNaruto.setObjectName("labelNaruto")
        self.verticalLayout_6.addWidget(self.labelNaruto)
        self.buttonNaruto = QtWidgets.QPushButton(self.handNaruto)
        self.buttonNaruto.setObjectName("buttonNaruto")
        self.buttonNaruto.clicked.connect(lambda: self.selectPosition("Naruto", "Keep your hand relaxed for 15 seconds, them, keep your index and middle fingers erect for more 15 seconds.", ":/positionsGifs/assets/naruto.gif"))
        self.verticalLayout_6.addWidget(self.buttonNaruto)
        self.gridLayout.addWidget(self.handNaruto, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.handPointing = QtWidgets.QWidget(self.selectPositionBody)
        self.handPointing.setObjectName("handPointing")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.handPointing)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelPointing = QtWidgets.QLabel(self.handPointing)
        self.labelPointing.setMaximumSize(QtCore.QSize(100, 100))
        self.labelPointing.setText("")
        self.labelPointing.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/pointing.png"))
        self.labelPointing.setScaledContents(True)
        self.labelPointing.setObjectName("labelPointing")
        self.verticalLayout_3.addWidget(self.labelPointing)
        self.buttonPointing = QtWidgets.QPushButton(self.handPointing)
        self.buttonPointing.setObjectName("buttonPointing")
        self.buttonPointing.clicked.connect(lambda: self.selectPosition("Pointing", "Keep your hand relaxed for 15 seconds, them, keep your index finger erect for more 15 seconds.", ":/positionsGifs/assets/pointing.gif"))
        self.verticalLayout_3.addWidget(self.buttonPointing)
        self.gridLayout.addWidget(self.handPointing, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.handRock = QtWidgets.QWidget(self.selectPositionBody)
        self.handRock.setObjectName("handRock")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.handRock)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelRock = QtWidgets.QLabel(self.handRock)
        self.labelRock.setMaximumSize(QtCore.QSize(100, 100))
        self.labelRock.setText("")
        self.labelRock.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/rock.png"))
        self.labelRock.setScaledContents(True)
        self.labelRock.setObjectName("labelRock")
        self.verticalLayout_4.addWidget(self.labelRock)
        self.buttonRock = QtWidgets.QPushButton(self.handRock)
        self.buttonRock.setObjectName("buttonRock")
        self.buttonRock.clicked.connect(lambda: self.selectPosition("Rock", "Keep your hand relaxed for 15 seconds, them, keep your thumb, index and little fingers erect for more 15 seconds.", ":/positionsGifs/assets/rock.gif"))
        self.verticalLayout_4.addWidget(self.buttonRock)
        self.gridLayout.addWidget(self.handRock, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.handSpock = QtWidgets.QWidget(self.selectPositionBody)
        self.handSpock.setObjectName("handSpock")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.handSpock)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSpock = QtWidgets.QLabel(self.handSpock)
        self.labelSpock.setMaximumSize(QtCore.QSize(100, 100))
        self.labelSpock.setText("")
        self.labelSpock.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/spock.png"))
        self.labelSpock.setScaledContents(True)
        self.labelSpock.setObjectName("labelSpock")
        self.verticalLayout.addWidget(self.labelSpock)
        self.buttonSpock = QtWidgets.QPushButton(self.handSpock)
        self.buttonSpock.setObjectName("buttonSpock")
        self.buttonSpock.clicked.connect(lambda: self.selectPosition("Spock", "Keep your hand relaxed for 15 seconds, them, keep her fully open and join your index and middle fingers, and your ring and little fingers, for more 15 seconds.", ":/positionsGifs/assets/spock.gif"))
        self.verticalLayout.addWidget(self.buttonSpock)
        self.gridLayout.addWidget(self.handSpock, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.handClosed = QtWidgets.QWidget(self.selectPositionBody)
        self.handClosed.setObjectName("handClosed")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.handClosed)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelClosed = QtWidgets.QLabel(self.handClosed)
        self.labelClosed.setMaximumSize(QtCore.QSize(100, 100))
        self.labelClosed.setText("")
        self.labelClosed.setPixmap(QtGui.QPixmap(":/positionsGifs/assets/closed.png"))
        self.labelClosed.setScaledContents(True)
        self.labelClosed.setObjectName("labelClosed")
        self.verticalLayout_2.addWidget(self.labelClosed)
        self.buttonClosed = QtWidgets.QPushButton(self.handClosed)
        self.buttonClosed.setObjectName("buttonClosed")
        self.buttonClosed.clicked.connect(lambda: self.selectPosition("Closed", "Keep your hand relaxed for 15 seconds, them, keep her fully closed for more 15 seconds.", ":/positionsGifs/assets/closed.gif"))
        self.verticalLayout_2.addWidget(self.buttonClosed)
        self.gridLayout.addWidget(self.handClosed, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        
        self.horizontalLayout_5.addWidget(self.selectPositionBody)
        self.horizontalLayout.addWidget(self.mainBody, 0, QtCore.Qt.AlignLeft)
        
        self.instructionsBody = QtWidgets.QWidget(self.centralwidget)
        self.instructionsBody.setObjectName("instructionsBody")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.instructionsBody)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelPosition = QtWidgets.QLabel(self.instructionsBody)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelPosition.setFont(font)
        self.labelPosition.setObjectName("labelPosition")
        self.verticalLayout_8.addWidget(self.labelPosition, 0, QtCore.Qt.AlignLeft)
        self.labelInstruction = QtWidgets.QLabel(self.instructionsBody)
        self.labelInstruction.setTextFormat(QtCore.Qt.AutoText)
        self.labelInstruction.setWordWrap(True)
        self.labelInstruction.setObjectName("labelInstruction")
        self.verticalLayout_8.addWidget(self.labelInstruction)
        self.imageInstruction = QtWidgets.QLabel(self.instructionsBody)
        self.imageInstruction.setMaximumSize(QtCore.QSize(300, 300))
        self.imageInstruction.setText("")
        self.instructionMovie = QtGui.QMovie(":/positionsGifs/assets/open.gif")
        self.imageInstruction.setMovie(self.instructionMovie)
        self.instructionMovie.start()
        self.imageInstruction.setScaledContents(True)
        self.imageInstruction.setObjectName("imageInstruction")
        self.verticalLayout_8.addWidget(self.imageInstruction, 0, QtCore.Qt.AlignHCenter)
        self.buttonInstructionStart = QtWidgets.QPushButton(self.instructionsBody)
        self.buttonInstructionStart.setObjectName("buttonInstructionStart")
        self.buttonInstructionStart.clicked.connect(self.startRecordingRoutine)
        self.verticalLayout_8.addWidget(self.buttonInstructionStart)
        self.horizontalLayout.addWidget(self.instructionsBody)
        
        self.recordingBody = QtWidgets.QWidget(self.centralwidget)
        self.recordingBody.setObjectName("recordingBody")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.recordingBody)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.headerBody = QtWidgets.QWidget(self.recordingBody)
        self.headerBody.setObjectName("headerBody")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerBody)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelCurrentInstruction = QtWidgets.QLabel(self.headerBody)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelCurrentInstruction.setFont(font)
        self.labelCurrentInstruction.setObjectName("labelCurrentInstruction")
        self.horizontalLayout_2.addWidget(self.labelCurrentInstruction)
        self.verticalLayout_10.addWidget(self.headerBody)
        self.checkBoxPlots = QtWidgets.QCheckBox(self.recordingBody)
        self.checkBoxPlots.setObjectName("checkBoxPlots")
        self.verticalLayout_10.addWidget(self.checkBoxPlots)
        self.horizontalLayout.addWidget(self.recordingBody, 0, QtCore.Qt.AlignVCenter)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1463, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit)
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.recordingBody.hide()

        self.cronometer = QtCore.QTimer(self)
        self.cronometer.timeout.connect(self.cronometerTimeout)

        # state machine params
        self.stateTimer = QtCore.QTimer(self)
        self.recordingState = -1
        self.remainingTime = -1
        self.recordingInstruction = 'NULL'

        self.currentEMGChannelPlot = 1
        self.currentIMUPlot = 1
        self.imuPlotDict = {1: "Acceleration", 2: "Velocity", 3: "Position"}

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelEMGHeader.setText(_translate("MainWindow", "Real time sEMG signal: Channel 1"))
        self.buttonEMGPrevious.setText(_translate("MainWindow", "Previous"))
        self.buttonEMGNext.setText(_translate("MainWindow", "Next"))
        self.labelIMUHeader.setText(_translate("MainWindow", "Real time IMU data: Acceleration"))
        self.buttonIMUPrevious.setText(_translate("MainWindow", "Previous"))
        self.buttonIMUNext.setText(_translate("MainWindow", "Next"))
        self.buttonConnectBand.setText(_translate("MainWindow", "Connect band"))
        self.buttonOpen.setText(_translate("MainWindow", "Select"))
        self.buttonNaruto.setText(_translate("MainWindow", "Select"))
        self.buttonPointing.setText(_translate("MainWindow", "Select"))
        self.buttonRock.setText(_translate("MainWindow", "Select"))
        self.buttonSpock.setText(_translate("MainWindow", "Select"))
        self.buttonClosed.setText(_translate("MainWindow", "Select"))
        self.labelPosition.setText(_translate("MainWindow", "Open"))
        self.labelInstruction.setText(_translate("MainWindow", "Keep your hand relaxed for 15 seconds, them, keep her fully open for more 15 seconds."))
        self.buttonInstructionStart.setText(_translate("MainWindow", "Start"))
        self.labelCurrentInstruction.setText(_translate("MainWindow", "Relax your hand in 5"))
        self.checkBoxPlots.setText(_translate("MainWindow", "Show real time data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRecent.setText(_translate("MainWindow", "Recent"))
        self.actionHelp.setText(_translate("MainWindow", "Visit our site"))

    def changeEMGChannelPlot(self, action):
        ''' action = +/- 1, depending if you want the next or previous channel '''
        nextChannel = self.currentEMGChannelPlot + action
        if nextChannel < 1:
            nextChannel = 16
        elif nextChannel > 16:
            nextChannel = 1

        self.currentEMGChannelPlot = nextChannel
        self.labelEMGHeader.setText("Real time sEMG signal: Channel {}".format(self.currentEMGChannelPlot))

    def changeIMUPlot(self, action):
        ''' action = +/- 1, depending if you want the next or previous channel '''
        next = self.currentIMUPlot + action
        if next < 1:
            next = 3
        elif next > 3:
            next = 1

        self.currentIMUPlot = next
        self.labelIMUHeader.setText("Real time IMU data: {}".format(self.imuPlotDict[self.currentIMUPlot]))

    def selectPosition(self, position, instruction, gif_path):
        '''
        called when one hand position is selected
        '''
        self.instructionsBody.show()

        self.labelPosition.setText(position)
        self.labelInstruction.setText(instruction)

        self.instructionMovie = QtGui.QMovie(gif_path)
        self.imageInstruction.setMovie(self.instructionMovie)
        self.instructionMovie.start()


    def cronometerTimeout(self):
        self.remainingTime -= 1
        self.labelCurrentInstruction.setText(self.recordingInstruction.format(self.remainingTime))

    def startRecordingRoutine(self):
        '''
        called by "start recording" button. begins signal recording routine
        '''
        self.mainBody.hide()
        self.instructionsBody.hide()
        self.recordingBody.show()

        self.nextRecordingState()
        self.cronometer.start(1000)

    def recordRelaxed(self):
        ''' 
        record relaxed arm data
        '''
        pass

    def recordContracted(self):
        '''
        record contracted arm data
        '''        
        pass

    def finishRecording(self):
        self.recordingBody.hide()
        self.mainBody.show()
        self.instructionsBody.show()

    def nextRecordingState(self):
        if self.recordingState == -1:
            self.recordingState = 0
            self.remainingTime = 5
            self.recordingInstruction = 'Relax your hand in {}'
            self.stateTimer.singleShot(5000, self.nextRecordingState)
        elif self.recordingState == 0:
            self.recordingState = 1
            self.remainingTime = 15
            self.recordingInstruction = 'Keep your hand relaxed for more {} seconds'
            self.stateTimer.singleShot(15000, self.nextRecordingState)
        elif self.recordingState == 1:
            self.recordingState = 2
            self.remainingTime = 15
            self.recordingInstruction = 'Keep your hand in the selected position for more {} seconds'
            self.stateTimer.singleShot(15000, self.nextRecordingState)
        elif self.recordingState == 2:
            self.recordingState = -1
            self.remainingTime = -1
            self.recordingInstruction = 'Relax your hand in 5'
            self.stateTimer.stop()
            self.finishRecording()

    def exit(self):
        QtCore.QCoreApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
