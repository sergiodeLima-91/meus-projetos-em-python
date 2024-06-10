from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


page1 = canvas.Canvas("hello-world.pdf")
page1.drawString(50, 780, "Hello World!")

page1.showPage()
page1.save()