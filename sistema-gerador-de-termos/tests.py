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
window.setWindowTitle('Editor de Texto')

# == FUNÇÕES:
# Negrito
def applyBold():
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
# Italico
def applyItalic():
    cursor = textEdit.textCursor()
    char_format = QTextCharFormat()
    font = QFont()
    font.setItalic( not cursor.charFormat().font().italic())
    char_format.setFont(font)
    cursor.mergeCharFormat(char_format)
    textEdit.mergeCurrentCharFormat(char_format)
# Sublinhado:
def applyUnderline():
    cursor = textEdit.textCursor()
    char_format = QTextCharFormat()
    font = QFont()
    font.setUnderline(not cursor.charFormat().font().underline())
    char_format.setFont(font)
    cursor.mergeCharFormat(char_format)
    textEdit.mergeCurrentCharFormat(char_format)

def showText():
    texto_digitado = textEdit.toPlainText()
    print("Texto digitado:")
    print(texto_digitado)


# === Botões ===:
# Negrito:
btn_bold = QPushButton("Negrito", window)
btn_bold.setGeometry(150, 110, 75, 25)
# Itálico:
btn_italic = QPushButton("Itálico", window)
btn_italic.setGeometry(150,140, 72, 25)
# Sublinhado:
btn_under = QPushButton("Sublinhado", window)
btn_under.setGeometry(150, 170, 75, 25)
# Mostrar texto digitado no textEdit:
btn_show_text = QPushButton("Exibir Texto", window)
btn_show_text.setGeometry(150, 230, 100, 25)
btn_show_text.clicked.connect(showText)

# Campo de Testo:
textEdit = QTextEdit("", window)
textEdit.setGeometry(250, 110, 100, 100)

# Eventos:
btn_bold.clicked.connect(applyBold)
btn_italic.clicked.connect(applyItalic)
btn_under.clicked.connect(applyUnderline)
btn_show_text.clicked.connect(showText)


# Start da Janela:
window.show()
app.exec()