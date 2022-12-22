from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle
  
### Create Application Object ###
app = QApplication([])

### Style Sheet ###
#* Font
QtGui.QFontDatabase.addApplicationFont("Exo 2")
font = QtGui.QFont("Exo 2")
font.setPointSize(12)
app.setFont(font)

#* Styles
app.setStyleSheet(
    "QWidget { color: #bbbfc3; background-color: #282b30; }"
    "QPushButton { background-color: #424549; }"
    "QGroupBox { font: bold; border: 1px solid white; border-radius: 6px; margin-top: 6px; }"
    "QGroupBox::title { subcontrol-origin: margin; left: 7px; margin; bottom: 9px; padding: 0px 5px 0px 5px; }"

)

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

#* Add Radio Buttons To List
answers = [ansBtn_1, ansBtn_2, ansBtn_3, ansBtn_4] #!Pt2

#* Create Label Objects
questLbl = QLabel("What year was Ho Chi Minh City founded?")
resultLbl = QLabel("Are you correct or not?") #!Pt2
correctLbl = QLabel("The answer will be here!") #!Pt2

#* Create Layout Objects
layoutMain = QVBoxLayout()

radioGrpBox = QGroupBox("Answer Options")
ansGrpBox = QGroupBox("Test Result") #!Pt2

layoutResult_V1 = QVBoxLayout() #!Pt2

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

layoutResult_V1.addWidget(resultLbl, alignment=(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)) #!Pt2
layoutResult_V1.addWidget(correctLbl, alignment=Qt.AlignmentFlag.AlignHCenter, stretch=2) #!Pt2

#* Assign Vertical Radio Layouts to Horizontal Radio Layout
layoutRadio_H1.addLayout(layoutRadio_V1)
layoutRadio_H1.addLayout(layoutRadio_V2)

#* Add Layouts to Group Boxes
radioGrpBox.setLayout(layoutRadio_H1)
ansGrpBox.setLayout(layoutResult_V1) #!Pt2

#* Add Widgets to Main Window Layout Lines
layoutMW_H1.addWidget(questLbl, alignment=(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter))
layoutMW_H2.addWidget(radioGrpBox)
layoutMW_H2.addWidget(ansGrpBox) #!Pt2
ansGrpBox.hide() #!Pt2
layoutMW_H3.addStretch(1)
layoutMW_H3.addWidget(ansBtn, stretch=2)

#* Add layouts to Layout Main
layoutMain.addLayout(layoutMW_H1, stretch=2)
layoutMain.addLayout(layoutMW_H2, stretch=8)
layoutMain.stretch(1)
layoutMain.addLayout(layoutMW_H3, stretch=1)
layoutMain.addStretch(1)
layoutMain.setSpacing(5)

### Application Functions ### #!Pt2
#* Function for showing result of answer
def showResult(): #!Pt2
    radioGrpBox.hide()
    ansGrpBox.show()
    ansBtn.setText("Next Question")

#* Function for showing new question
def showQuestion(): #!Pt2
    ansGrpBox.hide()
    radioGrpBox.show()
    ansBtn.setText("Answer")
    radioGrpBox.setExclusive(False)
    ansBtn_1.setChecked(False)
    ansBtn_2.setChecked(False)
    ansBtn_3.setChecked(False)
    ansBtn_4.setChecked(False)
    radioGrpBox.setExclusive(True)

#* Function for displaying the values of questtions and answering into their widgets and randomly distributes the answers to buttons
def ask(question, right_answer, wrong1, wrong2, wrong3): #!Pt2
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    questLbl.setText(question)
    correctLbl.setText(right_answer) 
    showQuestion() 

#* Function for showing the result
def showCorrect(res): #!Pt2
    resultLbl.setText(res)
    showResult()

#* Function for checking the selected answer and displaying the result True/False
def checkAnswer(): #!Pt2
    if answers[0].isChecked():
        showCorrect('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            showCorrect('Incorrect!')

#* Add Layout Main to Main Window
mainWin.setLayout(layoutMain)

#ask('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian') #!Pt2
#ansBtn.clicked.connect(checkAnswer) #!Pt2

### Execute the Application ###
mainWin.show()
app.exec()