import requests
import json
from PyQt6 import QtWidgets, QtGui, QtCore

class UpdateChecker:
    def __init__(self, current_version):
        self.current_version = current_version
        self.repo_url = "https://api.github.com/repos/sergiodeLima-91/Python_Tests_Repository/releases/latest"

    def check_for_updates(self):
        response = requests.get(self.repo_url)
        latest_release = json.loads(response.text)
        latest_version = latest_release["tag_name"]

        if latest_version != self.current_version:
            self.show_update_dialog(latest_release["html_url"])

    def show_update_dialog(self, download_url):
        app = QtWidgets.QApplication([])
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
        dialog.setWindowTitle("Atualização Disponível")
        dialog.setText("Uma nova versão do aplicativo está disponível.")
        dialog.setInformativeText("Deseja baixar a nova versão?")
        dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        dialog.setDefaultButton(QtWidgets.QMessageBox.StandardButton.Yes)
        
        if dialog.exec() == QtWidgets.QMessageBox.StandardButton.Yes:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(download_url))
        app.exec()

