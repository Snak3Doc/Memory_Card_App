from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QMessageBox, QRadioButton, QGroupBox

### Create Application Object ###
app = QApplication([])

### Create Main Window Object ###
mainWin = QWidget()
mainWin.setWindowTitle("Memory Card Quizz")

### Create GUI ###
#* Create Button Objects
ansBtn = QPushButton("Answer")

ansBtn_1 = QRadioButton("1921")
ansBtn_2 = QRadioButton("1963")
ansBtn_3 = QRadioButton("1975") # Correct Ans
ansBtn_4 = QRadioButton("1947")

#* Create Label Objects
questLbl = QLabel("What year was Ho Chi Minh City founded?")

#* Create Layout Objects
layoutMain = QVBoxLayout()

radioGrpBox = QGroupBox("Answer Options")

layoutRadio_H1 = QHBoxLayout()
layoutRadio_V1 = QVBoxLayout()
layoutRadio_V2 = QVBoxLayout()

layoutMW_H1 = QHBoxLayout()
layoutMW_H2 = QHBoxLayout()
layoutMW_H3 = QHBoxLayout()

#* Assign Widgets to layouts
layoutRadio_V1.addWidget(ansBtn_1)
layoutRadio_V1.addWidget(ansBtn_2)
layoutRadio_V2.addWidget(ansBtn_3)
layoutRadio_V2.addWidget(ansBtn_4)

#* Assign Vertical Radio Layouts to Horizontal Radio Layout
layoutRadio_H1.addLayout(layoutRadio_V1)
layoutRadio_H1.addLayout(layoutRadio_V2)

#* Add Layouts to Group Boxes
radioGrpBox.setLayout(layoutRadio_H1)

#* Add Widgets to Main Window Layout Lines
layoutMW_H1.addWidget(questLbl, alignment=(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter))
layoutMW_H2.addWidget(radioGrpBox)
layoutMW_H3.addStretch(1)
layoutMW_H3.addWidget(ansBtn, stretch=2)

#* Add layouts to Layout Main
layoutMain.addLayout(layoutMW_H1, stretch=2)
layoutMain.addLayout(layoutMW_H2, stretch=8)
layoutMain.stretch(1)
layoutMain.addLayout(layoutMW_H3, stretch=1)
layoutMain.addStretch(1)
layoutMain.setSpacing(5)

#* Add Layout Main to Main Window
mainWin.setLayout(layoutMain)


### Execute the Application ###
mainWin.show()
app.exec()