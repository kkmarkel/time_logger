import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from data.storage import Storage


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Time Logger")
    
    storage = Storage()
    window = MainWindow(storage)
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()