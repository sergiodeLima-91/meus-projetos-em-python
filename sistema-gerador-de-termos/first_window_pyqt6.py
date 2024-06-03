import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


# ============= CRIANDO A JANELA BASE =============
# Criando a aplicação
# Sys.argv passado como parâmetro a fim do UI ter acesso as settings do sistema:
app = QApplication(sys.argv)

# Criando novo obetjo para a classe QWidgets:
window = QWidget()
#Redimensionando a Janela:
window.resize(500, 400)
window.setWindowTitle('Primeira Janela')

# Inserindo botões:
# Altera cor do texto:
# Recebe dois parâmetros: o nome do botão e a janela na qual ele será exibido
btn = QPushButton("Clique aqui para alterar a cor!",window)
# Definindo local onde a janela ficará posicionada:
btn.setGeometry(210,100, 185, 20)
# Função que muda cor do botão quando clicado:
def mudaCorBotao():
    btn.setText('ALTERADA!')
    return btn.setStyleSheet('QPushButton:pressed{background-color: yellow; font-weight: bold;}')
# Aplicar negrito:
btn_negrito = QPushButton('B', window)
btn_negrito.adjustSize()
btn.setGeometry()
def negrito():
    textEdit.setStyleSheet('QLineEdit{\n'
            'font-weight: bold;'
    '\n}')

# Inserindo Label:
label = QLabel("Texto de Exemplo", window)
# Posicionando o Label:
label.move(400, 100)
# Colocando bordas no texto:
label.setStyleSheet('border: 1px solid rgb(50,88,75)')
# Mudando cor do texto e alterando conteúdo depois disso:
def mudaCorTexto():
    label.setText('COR MUDADA!')
    label.adjustSize()
    return label.setStyleSheet('QLabel{color: black; background-color: rgb(255,200,210); font-weight: bold}')

# Inserindo editor de texto:
textEdit = QLineEdit("", window)
textEdit.setGeometry(210, 150, 200, 150)
textEdit.setStyleSheet("QLineEdit:focus{\n"
"    border: 2px solid rgb(100, 100, 255);\n"
"}")

# Criando evento de clique:
btn.clicked.connect(mudaCorTexto)
btn.clicked.connect(mudaCorBotao)
btn_negrito.clicked.connect(negrito)



# Start da Janela:
window.show()
app.exec()