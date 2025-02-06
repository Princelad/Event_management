import sys
from PySide6.QtWidgets import QApplication
from ui.start_screen import StartMenu


def main():
    app = QApplication(sys.argv)
    window = StartMenu()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
