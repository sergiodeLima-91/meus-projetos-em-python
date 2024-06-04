import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QFont


# ============= CRIANDO A JANELA BASE =============
# Criando a aplicação
# Sys.argv passado como parâmetro a fim do UI ter acesso as settings do sistema:
app = QApplication(sys.argv)
# Criando novo obetjo para a classe QWidgets:
window = QWidget()
#Redimensionando a Janela:
window.resize(500, 400)
window.setWindowTitle('Aplicar negrito')

# == FUNÇÕES:
def aplicarNegrito():
    # Obtem o cursor do texto:
    cursor = textEdit.textCursor()
    # Criação do objeto para manipulação do estilo do texto:
    char_format = QTextCharFormat()
    # Criação de novo objeto "font" da classe QFont, pois não é possível realizar estilizações diretamente no objeto dela!
    font = QFont()
    font.setBold(not cursor.charFormat().font().bold())
    char_format.setFont(font)
    cursor.mergeCharFormat(char_format)
    textEdit.mergeCurrentCharFormat(char_format)


btn = QPushButton("Negrito", window)
btn.setGeometry(150, 150, 75, 25)
btn.clicked.connect(aplicarNegrito)

textEdit = QTextEdit("", window)
textEdit.setGeometry(250, 110, 100, 100)


# Start da Janela:
window.show()
app.exec()