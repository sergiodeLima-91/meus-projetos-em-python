from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date

def GerarTermoDeCancelamento():
        cnv = canvas.Canvas(f'TESTE - RECIBO.pdf')

        #INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
        cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
        cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

        #INSERIR IMAGEM DOS DADOS DA EMPRESA:
        cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=55)
                        #INSERIR DADOS DA EMPRESA
        cnv.setFont(psfontname='Times-Roman',size=12)
        cnv.drawString(x=298,y=737, text= 'MAXIMA PROTEÇAÕ VEICULAR')
        cnv.drawString(x=298,y=725, text= '414.252.0001-85')

        #INSERIR IMAGEM DO TIPO DE TERMO:
        cnv.drawImage(r'term_type.png',x=40,y=710,width=230,height=20)
                        #INSERIR TIPO DE TERMO
        cnv.setFont(psfontname='Times-Bold',size=12)
        cnv.drawString(x=100,y=717, text= 'RECIBO')

        #INSERIR IMAGEM DOS DETALHES DO TIPO DE TERMO:
        cnv.drawImage(r'recibo_detalhamento.png',x=40,y=588,width=520,height=120)

        #INSERIR IMAGEM DOS DADOS DO ASSOCIADO:
        cnv.drawImage(r'clientdata_cancel.png',x=40,y=495,width=520,height=94)
        #INSERIR DADOS DO ASSOCIADO:
                        #NOME/RAZÃO SOCIAL:
        cnv.drawString(x=155, y=551, text= 'TESTE')
                        #CPF/CNPJ:
        cnv.drawString(x=85, y=529, text='TESTE')
                        #MONTADORA:
        cnv.drawString(x=285, y=529, text= 'TESTE')
                        #MODELO:
        cnv.drawString(x=415, y=529, text= 'TESTE')
                        #ANO:
        cnv.drawString(x=85, y=507, text= 'TESTE')
                        #PLACA:
        cnv.drawString(x=265, y=507, text= 'TESTE')
                        #COR:
        cnv.drawString(x=405, y=507, text= 'TESTE')

        #INSERIR IMAGEM DOS DADOS FINANCEIROS:
        cnv.drawImage(r'finance.png',x=40,y=445,width=520,height=50)
        #INSERIR DADOS FINANCEIROS:
                        #MENSALIDADE:
        cnv.drawString(x=106, y=457.5, text= 'TESTE')
                        #TAXA DE CANCELAMENTO:
        cnv.drawString(x=362, y=457.5, text= 'TESTE')

        #ENCERRAMENTO:
                #CAPTAÇÃO DA DATA ATUAL:
        day = date.today().day
        month = date.today().month
        year = date.today().year
        month_current = str()
        if month == 1:
                month_current = 'JANEIRO'
        elif month == 2:
                month_current = 'FEVEREIRO'
        elif month == 3:
                 month_current = 'MARCO'
        elif month == 4:
                month_current = 'ABRIL'
        elif month == 5:
                month_current = 'MAIO'
        elif month == 6:
                month_current = 'JUNHO'
        elif month == 7:
                month_current = 'JULHO'
        elif month == 8:
                month_current = 'AGOSTO'
        elif month == 9:
                month_current = 'SETEMBRO'
        elif month == 10:
                month_current = 'OUTUBRO'
        elif month == 11:
                month_current = 'NOVEMBRO'
        elif month == 12:
                month_current = 'DEZEMBRO'

        cnv.drawString(x=40,y=350, text='Sem mais,')
        cnv.setFont(psfontname='Times-Italic',size=12)
                        #NOME FANTASIA DA EMPRESA PARA ASSINATURA:
        cnv.drawString(x=40,y=250,text= 'CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
        cnv.setFont(psfontname='Times-BoldItalic',size=12)
                        #IMPRIMIR DATA ATUAL E CIDADE DA SEDE ADMINISTRATIVA NO DOCUMENTO:
        cnv.drawString(x=40,y=200,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')


        #SALVAR PDF:
        cnv.save()

GerarTermoDeCancelamento()