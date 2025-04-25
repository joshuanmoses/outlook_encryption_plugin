from PyQt5 import QtWidgets

def ask_user_encryption_choice():
    app = QtWidgets.QApplication([])
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Email Encryption")
    msg.setText("Send this email encrypted?")
    msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    result = msg.exec_()
    return result == QtWidgets.QMessageBox.Yes
