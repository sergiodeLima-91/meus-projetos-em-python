import requests, webbrowser
from PyQt6.QtWidgets import QMessageBox, QPushButton

def check_updates(cur_ver):
      repo_url = "https://api.github.com/repos/sergiodeLima-91/Python_Tests_Repository/releases/latest"
      response = requests.get(repo_url)
      latest_version = response.json()["tag_name"]

      if latest_version != cur_ver:
            return latest_version
      
      return None

def notify_user(new_ver_url):
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Icon.Information)
      msg.setText("Uma nova versão está disponível")
      msg.setInformativeText(f"Baixe a nova versão aqui: {new_ver_url}")

      download_button = QPushButton("Baixar Nova Versão")
      download_button.clicked.connect(lambda: webbrowser.open(new_ver_url))

      msg.addButton(download_button, QMessageBox.ButtonRole.ActionRole)
      
      msg.exec()
