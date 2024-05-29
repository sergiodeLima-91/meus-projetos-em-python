import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel


# ============= CRIANDO A JANELA BASE =============
# Criando a aplicação
# Sys.argv passado como parâmetro a fim do UI ter acesso as settings do sistema:
app = QApplication(sys.argv)

# Criando novo obetjo para a classe QWidgets:
window = QWidget()
#Redimensionando a Janela:
window.resize(500, 400)
window.setWindowTitle('Primeira Janela')

# Inserindo botão:
# Recebe dois parâmetros: o nome do botão e a janela na qual ele será exibido
btn = QPushButton("Clique aqui",window)
# Definindo local onde a janela ficará posicionada:
btn.setGeometry(220,100, 80, 20)
# Aplicando CSS no elemento:
btn.setStyleSheet('background-color: blue')

# Inserindo Label:
label = QLabel("Texto", window)
# Posicionando o Label:
label.move(400, 100)



# Start da Janela:
window.show()
app.exec()