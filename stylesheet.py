from PyQt5 import QtGui

def set_font(app):
    QtGui.QFontDatabase.addApplicationFont("Exo 2")
    font = QtGui.QFont("Exo 2")
    font.setPointSize(12)
    app.setFont(font)

def set_style(app):
    app.setStyleSheet(
        "QWidget { color: #bbbfc3; background-color: #282b30; }"
        "QPushButton { background-color: #424549; }"
        "QGroupBox { font: bold; border: 1px solid white; border-radius: 6px; margin-top: 6px; }"
        "QGroupBox::title { subcontrol-origin: margin; left: 7px; margin; bottom: 9px; padding: 0px 5px 0px 5px; }"
    )
