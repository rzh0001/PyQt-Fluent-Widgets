# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from qfluentwidgets import Dialog, setTheme, Theme, PrimaryPushButton


class Demo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(950, 500)
        self.btn = PrimaryPushButton('Click Me', parent=self)
        self.btn.move(425, 225)
        self.btn.clicked.connect(self.showDialog)
        self.setStyleSheet('Demo{background:white}')

        # setTheme(Theme.DARK)

    def showDialog(self):
        title = 'Are you sure you want to delete the folder?'
        content = """If you delete the "Music" folder from the list, the folder will no longer appear in the list, but will not be deleted."""
        w = Dialog(title, content, self)
        if w.exec():
            print('Yes button is pressed')
        else:
            print('Cancel button is pressed')


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec_())
