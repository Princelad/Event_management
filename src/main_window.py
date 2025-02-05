from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My PySide App')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Hello, World!')
        layout.addWidget(label)

        button = QPushButton('Click me!')
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)

        self.show()

    def on_button_clicked(self):
        print('Button clicked!')