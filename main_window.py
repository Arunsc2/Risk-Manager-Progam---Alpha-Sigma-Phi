from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from main import RM
import sys
import qdarktheme

# For when not all fields are filled in
class ErrorWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Error')
        self.setFixedHeight(100)
        self.setFixedWidth(300)
        errormsg = 'Make sure all the fields are filled in and \nhave an integer value!'
        okButton = QPushButton('OK')
        msg = QLabel(errormsg)
        okButton.clicked.connect(self.ok_command)

        layout = QVBoxLayout()
        layout.addWidget(msg)
        layout.addWidget(okButton)
        msg.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
    
    def ok_command(self):
        self.close()
    
class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        
        
class OutputWindow(QWidget):
    def __init__(self, sobers): 
        super().__init__()
        self.setWindowTitle('Sobers')
        self.setFixedHeight(700)
        self.setFixedWidth(700)

        self.drivers = sobers[0]
        self.roamers = sobers[1]
        self.stationaries = sobers[2]
        self.list = sobers[3]
        self.bartenders = sobers[4]
        self.exec = sobers[5]

        driverString = ''
        roamerString = ''
        stationariesString = ''
        listString = ''
        bartenderString = ''
        execString = ''

        for driver in self.drivers: 
            driverString = driverString + driver + '\n'
        
        for roamer in self.roamers:
            roamerString = roamerString + roamer + '\n'
        
        for stationary in self.stationaries:
            stationariesString = stationariesString + stationary + '\n'
        
        for list in self.list: 
            listString = listString + list + '\n'
        
        for bartender in self.bartenders: 
            bartenderString = bartenderString + bartender + '\n'

        for exec in self.exec:
            execString = execString + exec + '\n'

        driverLabel = QLabel(driverString)
        roamerLabel = QLabel(roamerString)
        stationaryLabel = QLabel(stationariesString)
        listLabel = QLabel(listString)
        bartenderLabel = QLabel(bartenderString)
        execLabel = QLabel(execString)

        driverLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        roamerLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        stationaryLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        listLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        bartenderLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        execLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.setStyleSheet("""
            QLabel {
                font-size: 13px;
            }
        """)

        driverBox = QGroupBox('Drivers')
        roamerBox = QGroupBox('Roamers')
        stationaryBox = QGroupBox('Stationaries')
        listBox = QGroupBox('List')
        bartenderBox = QGroupBox('Bartenders')
        execBox = QGroupBox('Sober Exec')

        driverLayout = QVBoxLayout()
        driverLayout.addWidget(driverLabel)
        driverBox.setLayout(driverLayout)

        roamerLayout = QVBoxLayout()
        roamerLayout.addWidget(roamerLabel)
        roamerBox.setLayout(roamerLayout)
        
        stationaryLayout = QVBoxLayout()
        stationaryLayout.addWidget(stationaryLabel)
        stationaryBox.setLayout(stationaryLayout)

        listLayout = QVBoxLayout()
        listLayout.addWidget(listLabel)
        listBox.setLayout(listLayout)

        bartenderLayout = QVBoxLayout()
        bartenderLayout.addWidget(bartenderLabel)
        bartenderBox.setLayout(bartenderLayout)

        execLayout = QVBoxLayout()
        execLayout.addWidget(execLabel)
        execBox.setLayout(execLayout)
        
        # driverBox.addWidget(driverLabel)
        # roamerBox.addWidget(roamerLabel)
        # stationaryBox.addWidget(stationaryLabel)
        # listBox.addWidget(listLabel)
        # bartenderBox.addWidget(bartenderLabel)
        # execBox.addWidget(execLabel)

        line1 = QHBoxLayout()
        line1.addWidget(driverBox)
        line1.addWidget(roamerBox)
        
        line2 = QHBoxLayout()
        line2.addWidget(bartenderBox)
        line2.addWidget(listBox)
        
        line3 = QHBoxLayout()
        line3.addWidget(stationaryBox)
        line3.addWidget(execBox)

        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addLayout(line2)
        layout.addLayout(line3)

        self.setLayout(layout)


class MainWindow(QWidget): 
    
    def __init__(self): 
        super().__init__()
        # self.soberInput = soberInput
        self.setFixedHeight(800)
        self.setFixedWidth(800)
        layout = QVBoxLayout()
        self.title = 'Risk Manager Program'
        title_label = QLabel(self.title)
        title_label.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(title_label)
        layout.addWidget(QHLine())
        title_label.setFixedHeight(50)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 30px; 
            }
        """)
        self.sober_gbox = SoberInput()
        # self.sober_gbox.setFixedWidth(200)
        self.sober_gbox.setContentsMargins(0,20,0,0)
        layout.addWidget(self.sober_gbox)
        
        go_button = QPushButton("GO")
        # go_button.setFixedWidth(200)
        # go_button.setContentsMargins(200,0,200,0)
        go_button.setStyleSheet("""
            QPushButton {
                border-radius: 3px;
                font-size: 25px;
                color: white;
                background-color: rgb(86, 219, 86);         
            }
            QPushButton:hover {
                background-color: rgb(49, 212, 49);
            }
            QPushButton:pressed {
                background-color: rgb(9, 237, 9)
            }
        """)

        go_button.clicked.connect(self.go_command)

        layout.addWidget(go_button)
        

        self.setLayout(layout)
        self.setWindowTitle(self.title + ' made by Arunav Sen Choudhuri')

    def go_command(self):
        drivers = self.sober_gbox.driversInput.text()
        stationaries = self.sober_gbox.stationariesInput.text()
        roamers = self.sober_gbox.roamersInput.text()
        bartenders = self.sober_gbox.bartendersInput.text()
        list = self.sober_gbox.listInput.text()
        exec = self.sober_gbox.execInput.text()
        isTwentyOne = self.sober_gbox.twentyoneInput.isChecked()
        
        if drivers and stationaries and roamers and bartenders and list and exec: 
            if drivers.isnumeric() and stationaries.isnumeric() and roamers.isnumeric() and bartenders.isnumeric() and list.isnumeric() and exec.isnumeric(): 
                try: 
                    drivers = int(drivers)
                    stationaries = int(stationaries)
                    roamers = int(roamers)
                    bartenders = int(bartenders)
                    list = int(list)
                    exec = int(exec)

                    self.sobers = RM.assignSobers(drivers=drivers, stationaries=stationaries, roamers=roamers, list=list, exec=exec, isTwentyOne=isTwentyOne, bartenders=bartenders)
                    self.outputWindow = OutputWindow(self.sobers)
                    self.outputWindow.show()
                except ValueError: 
                    self.errorWindow = ErrorWindow()
                    self.errorWindow.show()
            else: 
                self.errorWindow = ErrorWindow()
                self.errorWindow.show()
        else: 
            self.errorWindow = ErrorWindow()
            self.errorWindow.show()
            # TODO create filled in error box
        
    
class SoberInput(QGroupBox):

    def __init__(self): 
        super().__init__()
        self.setTitle("Sober Assignments")
        self.setStyleSheet("""
            QGroupBox {
                font-size: 15px;
            }
        """)

        glayout = QVBoxLayout()
        
        instructionLabel = QLabel("Input the number of sobers for each category")
        driversLabel = QLabel("Drivers:")
        stationariesLabel = QLabel("Stationaries:")
        roamersLabel = QLabel("Roamers:")
        bartendersLabel = QLabel("Bartenders:")
        listLabel = QLabel("List:")
        execLabel = QLabel("Exec:")
        twentyoneLabel = QLabel("Bartenders over 21 years of age:")

        self.driversInput = QLineEdit()
        self.stationariesInput = QLineEdit()
        self.roamersInput = QLineEdit()
        self.bartendersInput = QLineEdit()
        self.listInput = QLineEdit()
        self.execInput = QLineEdit('1')
        self.twentyoneInput = QCheckBox()
        
        # size = QSize(100,20)
        # driversInput.setFixedSize(size)
        # stationariesInput.setFixedSize(size)
        # roamersInput.setFixedSize(size)
        # bartendersInput.setFixedSize(size)
        # listInput.setFixedSize(size)
        # execInput.setFixedSize(size)

        self.driversInput.setFixedWidth(50)
        self.stationariesInput.setFixedWidth(50)
        self.roamersInput.setFixedWidth(50)
        self.listInput.setFixedWidth(50)
        self.bartendersInput.setFixedWidth(50)
        self.execInput.setFixedWidth(50)
        self.twentyoneInput.setChecked(True)

        line1 = QHBoxLayout()
        line1.addWidget(driversLabel)
        line1.addWidget(self.driversInput)
        line1.setContentsMargins(250,0,325,0)
       

        line2 = QHBoxLayout()
        line2.addWidget(stationariesLabel)
        line2.addWidget(self.stationariesInput)
        line2.setContentsMargins(250,0,325,0)

        line3 = QHBoxLayout()
        line3.addWidget(roamersLabel)
        line3.addWidget(self.roamersInput)
        line3.setContentsMargins(250,0,325,0)

        line4 = QHBoxLayout()
        line4.addWidget(bartendersLabel)
        line4.addWidget(self.bartendersInput)
        line4.setContentsMargins(250,0,325,0)
        
        line5 = QHBoxLayout()
        line5.addWidget(listLabel)
        line5.addWidget(self.listInput)
        line5.setContentsMargins(250,0,325,0)

        line6 = QHBoxLayout()
        line6.addWidget(execLabel)
        line6.addWidget(self.execInput)
        line6.setContentsMargins(250,0,325,0)

        line7 = QHBoxLayout()
        line7.addWidget(twentyoneLabel)
        line7.addWidget(self.twentyoneInput)
        line7.setContentsMargins(150,0,150,0)


        # glayout.addWidget(instructionLabel)
        glayout.addLayout(line1)
        glayout.addLayout(line2)
        glayout.addLayout(line3)
        glayout.addLayout(line4)
        glayout.addLayout(line5)
        glayout.addLayout(line6)
        glayout.addLayout(line7)

        self.setStyleSheet("""
            QLabel {
                font-size: 15px;
            }
        """)

        self.setLayout(glayout)



        

        




app = QApplication(sys.argv)
qdarktheme.setup_theme()
window = MainWindow()
window.show()
app.exec()