import sys
from PySide6 import QtCore, QtWidgets, QtGui
from webbrowser import open_new

class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Connect")
        self.text = QtWidgets.QLabel("Voltage's Launcher.\nHave a nice playtime!")
        self.text.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        self.choose = QtWidgets.QComboBox(frame=True)
        self.choose.addItem('Test server')
        self.choose.addItem('Choose a server')
        self.choose.setCurrentIndex(1)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.choose)

        self.button.clicked.connect(self.connect)

    @QtCore.Slot()
    def connect(self):
            if self.choose.currentIndex() == 1:
                self.text.setText('Choose a server.')
            elif self.choose.currentIndex() == 0:
                self.text.setText('Connecting to ' + self.choose.currentText())
                open_new('steam://connect/23.88.73.88:13294')
                self.text.setText('Have a nice playtime!\nYou can close the launcher.')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Launcher()
    widget.setWindowTitle('Launcher GUI')
    widget.resize(350, 100)
    widget.show()

    sys.exit(app.exec())
