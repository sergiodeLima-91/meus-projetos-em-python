from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Criando o Objeto da classe Canvas presente no módulo canvas:
page1 = canvas.Canvas("testes.pdf")
# Atributo "mask" em drawImage() especifica se a transparência da imagem deve ser preservada ou não:
page1.drawImage(r'./src/images/logo.png', x=30, y=770, width=70, height=70, mask='auto')

page1.showPage()
page1.save()