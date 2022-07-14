from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QDialog
from PyQt5.QtGui import QIcon
import os, sys

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        icon = QIcon("OUTGOING.ICO")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(icon)
        self.tray.show()
        self.tray.showMessage("File upload complete", "File upload complete")     

    def run(self):
        # Enter Qt application main loop
        self.app.exec_()
        sys.exit()

    def exit(self):
        pid = os.getpid()
        os.kill(pid, 2)

app = QApplication(sys.argv)
window = App()
window.run()
app.exec_()