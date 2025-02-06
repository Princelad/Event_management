from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from .main_screen import MainWindow


class StartMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('College Event Management')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Welcome to College Event Management')
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        button = QPushButton('Enter')
        button.setFixedHeight(40)
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

    def on_button_clicked(self):
        """Opens the main event management window."""
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
