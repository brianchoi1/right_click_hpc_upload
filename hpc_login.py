from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication, QDialog, QLabel, QLineEdit, QGridLayout
import sys, paramiko

class setupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI_d()
        self.ssh = paramiko.SSHClient() 
        self.ip = 'hpc.lge.com'  
        self.id = ''
        self.pw = ''

    def setupUI_d(self):
        self.setGeometry(800, 200, 300, 200)
        self.setWindowTitle("HPC login check")

        label1 = QLabel("HPC ID: ")
        label2 = QLabel("HPC Password: ")
        self.label3 = QLabel(" ")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setFixedWidth(150)
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setFixedWidth(150)
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.pushButton1= QPushButton("Login")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.pushButton1, 3, 0)
        layout.addWidget(self.label3, 4, 1)

        self.setLayout(layout)

    def pushButtonClicked(self):
        self.id = self.lineEdit1.text()
        self.pw = self.lineEdit2.text()
        login_key = self.login_check()
        if login_key == 1:
            f = open('hpc_id_pw_check', 'w', encoding='utf-8')
            f.write(self.id + '\n')
            f.write(self.pw)
            f.close()
            self.About_event()
            self.close()
        else:
            self.label3.setText("Login failed. Try again")

    def About_event(self): 
        QMessageBox.about(self,'ID available','Login comfirmed')

    def login_check(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        try:
            self.ssh.connect(self.ip, 22, self.id, self.pw)
            login_key = 1
            return login_key
        except:
            login_key = 0
            return login_key

# if __name__ == "__main__":
app = QApplication(sys.argv)
window = setupDialog()
window.show()
app.exec_()