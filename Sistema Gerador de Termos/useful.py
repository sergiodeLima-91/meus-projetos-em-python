from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph    
from reportlab.pdfgen.canvas import Canvas
from datetime import date    


#========================================== GERAÇÃO DE TERMO DE ADESÃO ==========================================
"""cnv = Canvas('GeraPDF.pdf')
cnv.setFont(psfontname='Times-Roman',size=10)


#INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

#INSERIR IMAGEM DOS DADOS DA EMPRESA:
cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=50)
                #INSERIR DADOS DA EMPRESA
cnv.drawString(x=298,y=737, text='CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.drawString(x=298,y=725, text='40.989.892/0001-10')

#INSERIR IMAGEM DE TÍTULO, CABEÇALHO E TIPO DE PLANO:
cnv.drawImage(r'header_sgt.png',x=40,y=600,width=520,height=110)
                #INSERIR DADOS DO PLANO:
cnv.drawString(x=75,y=609, text='MONITORAMENTO')


#INSERIR IMAGEM DOS DADOS DO ASSOCIADO E ENDEREÇO:
cnv.drawImage(r'clientdata_address.png',x=40,y=440,width=520,height=160)
#INSERIR DADOS DO ASSOCIADO:
                #NOME:
cnv.drawString(x=155, y=556, text='MARIA JOANA GOES DA SILVA')
                #RG:
cnv.drawString(x=62, y=536, text='3543976')
                #CPF/CNPJ:
cnv.drawString(x=200, y=535, text='05236345289')
                #DATA DE NASCIMENTO:
cnv.drawString(x=425, y=535, text='22/05/1985')
                #NACIONALIDADE:
cnv.drawString(x=105, y=512, text='NACIONALIDADE')
               #DATA DA RUA:
cnv.drawString(x=290, y=511, text='VALDAIR PEQUENO DE MELO')
                #NUMERO:
cnv.drawString(x=62, y=491, text='35A')
                #COMPLEMENTO:
cnv.drawString(x=160, y=491, text='CASA/APARTAMENTO')
                #BAIRRO:
cnv.drawString(x=380, y=491, text='MALVINAS')
                #CEP:
cnv.drawString(x=62, y=469, text='35739-726')
                #CIDADE:
cnv.drawString(x=205, y=469, text='CAMPINA GRANDE')
                #UF:
cnv.drawString(x=510, y=469, text='PB')
                #TELEFONE 1:
cnv.drawString(x=95, y=448, text='083985656523')
                #TELEFONE 2:
cnv.drawString(x=275, y=448, text='083985656523')


#INSERIR IMAGEM DOS DADOS DO VEÍCULO:
cnv.drawImage(r'vehicle_data.png',x=40,y=340,width=520,height=100)
#INSERIR DADOS DO VEICULO:
                #MONTADORA:
cnv.drawString(x=88, y=403, text='MONTADORA')
                #MODELO:
cnv.drawString(x=260,y=403, text='MODELO')
                #ANO:
cnv.drawString(x=450, y=404, text='ANO')
                #PLACA:
cnv.drawString(x=70, y=385, text='PLACA')
                #COR:
cnv.drawString(x=230, y=385, text='COR')
                #RENAVAM:
cnv.drawString(x=410, y=385, text='RENAVAM')
                #CHASSI:
cnv.drawString(x=73, y=366, text='CHASSI')
               #RVALOR FIPE:
cnv.drawString(x=426, y=366, text='VALOR FIPE')
                #CÓD.FIPE:
cnv.drawString(x=85, y=347, text='CÓDIGO FIPE')


#INSERIR IMAGEM DOS DADOS FINANCEIROS:
cnv.drawImage(r'finance.png',x=40,y=290,width=520,height=50)
#INSERIR DADOS FINANCEIROS:
                #CÓD.FIPE:
cnv.drawString(x=106, y=298, text='125,90')
                #ADESÃO:
cnv.drawString(x=220, y=298, text='300,00')
                #TAXA DE CANCELAMENTO:
cnv.drawString(x=360, y=298, text='200,00')
                #PAGTO TOTAL DE PLANO:
cnv.drawString(x=492, y=298, text='2000,00')


#INSERIR IMAGEM DO CAMPO DA COBERTURA:
cnv.drawImage(r'coverages.png',x=40,y=115,width=520,height=175)
#INSERIR DADOS DA COBERTURA:
coberturas = [
    'Monitoramento',
    'Roubo',
    'Furto',
    'Perda Total',
    'Colisão do Associado',
    '3 Reboques Gratuitos',
    '6 Reboques Gratuitos',
    'Reboque Ilimitado',
    'Quinhentos Quilômetros de Reboque',
    'Vidros em Geral',
    'Terceiros'
]
eixo_y = 240
for cobertura in coberturas:
    cnv.drawString(x=50, y=eixo_y, text=f'{cobertura}')
    eixo_y -= 11.2

#IMPRIMIR DATA ATUAL NO DOCUMENTO E NOME FANTASIA DA EMPRESA:
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

cnv.setFont(psfontname='Times-Italic',size=10)
cnv.drawString(x=40,y=75,text= 'CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.setFont(psfontname='Times-BoldItalic',size=10)
cnv.drawString(x=40,y=21,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')

#SALVAR EM PDF:
cnv.save()"""


"""def GenerateTermOfAdhesion(self):
cnv = canvas.Canvas(f'{lineEdit_name.text()}.pdf')
cnv.setFont(psfontname='Times-Roman',size=10)


#INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

#INSERIR IMAGEM DOS DADOS DA EMPRESA:
cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=50)
                #INSERIR DADOS DA EMPRESA
cnv.drawString(x=298,y=737, text='CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.drawString(x=298,y=725, text='40.989.892/0001-10')

#INSERIR IMAGEM DE TÍTULO, CABEÇALHO E TIPO DE PLANO:
cnv.drawImage(r'header_sgt.png',x=40,y=600,width=520,height=110)
                #INSERIR DADOS DO PLANO:
plain_type = 'MONITORAMENTO'
if radioButton_monitoring.isChecked():
        plain_type =   'MONITORAMENTO'
if radioButton_bronze01.isChecked():
        plain_type =   'BRONZE 01'
if radioButton_bronze02.isChecked():
        plain_type =   'BRONZE 02'
if radioButton_silver01.isChecked():
        plain_type =   'PRATA 01'
if radioButton_silver02.isChecked():
        plain_type =   'PRATA 02'
if radioButton_gold.isChecked():
        plain_type =   'OURO'
cnv.drawString(x=75,y=609, text= plain_type.upper())


#INSERIR IMAGEM DOS DADOS DO ASSOCIADO E ENDEREÇO:
cnv.drawImage(r'clientdata_address.png',x=40,y=440,width=520,height=160)
#INSERIR DADOS DO ASSOCIADO:
                #NOME:
cnv.drawString(x=155, y=556, text= lineEdit_name.text())
                #RG:
cnv.drawString(x=62, y=536, text= lineEdit_rg.text())
                #CPF/CNPJ:
cnv.drawString(x=200, y=535, text= lineEdit_cpf.text())
                #DATA DE NASCIMENTO:
cnv.drawString(x=425, y=535, text='22/05/1985')
                #NACIONALIDADE:
cnv.drawString(x=105, y=512, text='NACIONALIDADE')
                #DATA DE NASCIMENTO:
cnv.drawString(x=425, y=535, text= lineEd)
        #DATA DA RUA:
cnv.drawString(x=290, y=511, text='VALDAIR PEQUENO DE MELO')
                #NUMERO:
cnv.drawString(x=62, y=491, text='35A')
                #NCOMPLEMENTO:
cnv.drawString(x=160, y=491, text='CASA/APARTAMENTO')
                #BAIRRO:
cnv.drawString(x=380, y=491, text='MALVINAS')
                #CEP:
cnv.drawString(x=62, y=469, text='35739-726')
                #CIDADE:
cnv.drawString(x=205, y=469, text='CAMPINA GRANDE')
                #UF:
cnv.drawString(x=510, y=469, text='PB')
                #TELEFONE 1:
cnv.drawString(x=95, y=448, text='083985656523')
                #TELEFONE 2:
cnv.drawString(x=275, y=448, text='083985656523')


#INSERIR IMAGEM DOS DADOS DO VEÍCULO:
cnv.drawImage(r'vehicle_data.png',x=40,y=340,width=520,height=100)
#INSERIR DADOS DO VEICULO:
                #MONTADORA:
cnv.drawString(x=88, y=403, text='MONTADORA')
                #MODELO:
cnv.drawString(x=260,y=403, text='MODELO')
                #ANO:
cnv.drawString(x=450, y=404, text='ANO')
                #PLACA:
cnv.drawString(x=70, y=385, text='PLACA')
                #COR:
cnv.drawString(x=230, y=385, text='COR')
                #RENAVAM:
cnv.drawString(x=410, y=385, text='RENAVAM')
                #CHASSI:
cnv.drawString(x=73, y=366, text='CHASSI')
        #RVALOR FIPE:
cnv.drawString(x=426, y=366, text='VALOR FIPE')
                #CÓD.FIPE:
cnv.drawString(x=85, y=347, text='CÓDIGO FIPE')


#INSERIR IMAGEM DOS DADOS FINANCEIROS:
cnv.drawImage(r'finance.png',x=40,y=290,width=520,height=50)
#INSERIR DADOS FINANCEIROS:
                #CÓD.FIPE:
cnv.drawString(x=106, y=298, text='125,90')
                #ADESÃO:
cnv.drawString(x=220, y=298, text='300,00')
                #TAXA DE CANCELAMENTO:
cnv.drawString(x=360, y=298, text='200,00')
                #TAXA DE CANCELAMENTO:
cnv.drawString(x=492, y=298, text='2000,00')


#INSERIR IMAGEM DO CAMPO DA COBERTURA:
cnv.drawImage(r'coverages.png',x=40,y=115,width=520,height=175)
#INSERIR DADOS DA COBERTURA:
coberturas = [
'Monitoramento',
'Roubo',
'Furto',
'Perda Total',
'Colisão do Associado',
'3 Reboques Gratuitos',
'6 Reboques Gratuitos',
'Reboque Ilimitado',
'Quinhentos Quilômetros de Reboque',
'Vidros em Geral',
'Terceiros'
]
eixo_y = 240
for cobertura in coberturas:
        cnv.drawString(x=50, y= eixo_y, text=f'{cobertura}')
        eixo_y -= 11

#IMPRIMIR DATA ATUAL NO DOCUMENTO E NOME FANTASIA DA EMPRESA:
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

cnv.setFont(psfontname='Times-Italic',size=10)
cnv.drawString(x=40,y=75,text= 'CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.setFont(psfontname='Times-BoldItalic',size=10)
cnv.drawString(x=40,y=21,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')

#SALVAR EM PDF:
cnv.save()"""""

#========================================== GERAÇÃO DE TERMO DE CANCELAMENTO ==========================================

"""cnv = Canvas('GeraPDF.pdf')

#INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

#INSERIR IMAGEM DOS DADOS DA EMPRESA:
cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=55)
                #INSERIR DADOS DA EMPRESA
cnv.setFont(psfontname='Times-Roman',size=12)
cnv.drawString(x=298,y=737, text='CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.drawString(x=298,y=725, text='40.989.892/0001-10')

#INSERIR IMAGEM DO TIPO DE TERMO:
cnv.drawImage(r'term_type.png',x=40,y=710,width=230,height=20)
                #INSERIR TIPO DE TERMO
cnv.setFont(psfontname='Times-Bold',size=12)
cnv.drawString(x=100,y=717, text= 'CANCELAMENTO')

#INSERIR IMAGEM DOS DETALHES DO TIPO DE TERMO:
cnv.drawImage(r'details_term_cancel.png',x=40,y=615,width=520,height=94)

#INSERIR IMAGEM DOS DADOS DO ASSOCIADO:
cnv.drawImage(r'clientdata_cancel.png',x=40,y=520,width=520,height=94)
#INSERIR DADOS DO ASSOCIADO:
                #NOME/RAZÃO SOCIAL:
cnv.drawString(x=155, y=571, text= 'NOME DO ASSOCIADO')
                #CPF/CNPJ:
cnv.drawString(x=85, y=549, text= 'CPF/CNPJ')
                #MONTADORA:
cnv.drawString(x=285, y=549, text= 'MONTADORA')
                #MODELO:
cnv.drawString(x=415, y=549, text= 'MODELO')
                #ANO:
cnv.drawString(x=85, y=527, text= 'ANO')
                #PLACA:
cnv.drawString(x=265, y=527, text= 'PLACA')
                #COR:
cnv.drawString(x=405, y=527, text= 'COR')

#INSERIR IMAGEM DOS DADOS FINANCEIROS:
cnv.drawImage(r'finance.png',x=40,y=470,width=520,height=50)
#INSERIR DADOS FINANCEIROS:
                #MENSALIDADE:
cnv.drawString(x=106, y=477.5, text= '150,00')
                #TAXA DE CANCELAMENTO:
cnv.drawString(x=362, y=477.5, text= '200,00')

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

cnv.drawString(x=40,y=400, text='Sem mais,')
cnv.setFont(psfontname='Times-Italic',size=12)
                #NOME FANTASIA DA EMPRESA PARA ASSINATURA:
cnv.drawString(x=40,y=300,text= 'CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.setFont(psfontname='Times-BoldItalic',size=12)
                #IMPRIMIR DATA ATUAL E CIDADE DA SEDE ADMINISTRATIVA NO DOCUMENTO:
cnv.drawString(x=40,y=200,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')


#SALVAR PDF:
cnv.save()"""

#========================================== GERAÇÃO DE TERMO DE ENCAMINHAMENTO ==========================================

"""cnv = Canvas('GeraPDF.pdf')

#INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

#INSERIR IMAGEM DOS DADOS DA EMPRESA:
cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=55)
                #INSERIR DADOS DA EMPRESA
cnv.setFont(psfontname='Times-Roman',size=12)
cnv.drawString(x=298,y=737, text='CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.drawString(x=298,y=725, text='40.989.892/0001-10')

#INSERIR IMAGEM DO TIPO DE TERMO:
cnv.drawImage(r'term_type.png',x=40,y=710,width=230,height=20)
                #INSERIR TIPO DE TERMO
cnv.setFont(psfontname='Times-Bold',size=12)
cnv.drawString(x=100,y=717, text= 'ENCAMINHAMENTO')

#INSERIR IMAGEM DOS DETALHES DO TIPO DE TERMO:
cnv.drawImage(r'details_term_encaminhamento.png',x=40,y=615,width=520,height=94)

#INSERIR IMAGEM DOS DADOS DO ASSOCIADO:
cnv.drawImage(r'clientdata_cancel.png',x=40,y=520,width=520,height=94)
#INSERIR DADOS DO ASSOCIADO:
                #NOME/RAZÃO SOCIAL:
cnv.drawString(x=155, y=571, text= 'NOME DO ASSOCIADO')
                #CPF/CNPJ:
cnv.drawString(x=85, y=549, text= 'CPF/CNPJ')
                #MONTADORA:
cnv.drawString(x=285, y=549, text= 'MONTADORA')
                #MODELO:
cnv.drawString(x=415, y=549, text= 'MODELO')
                #ANO:
cnv.drawString(x=85, y=527, text= 'ANO')
                #PLACA:
cnv.drawString(x=265, y=527, text= 'PLACA')
                #COR:
cnv.drawString(x=405, y=527, text= 'COR')

#INSERIR IMAGEM DOS DADOS FINANCEIROS:
cnv.drawImage(r'finance.png',x=40,y=470,width=520,height=50)
#INSERIR DADOS FINANCEIROS:
                #MENSALIDADE:
cnv.drawString(x=106, y=477.5, text= '150,00')
                #TAXA DE ADESÃO:
cnv.drawString(x=222, y=477.5, text= '200,00')

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

cnv.drawString(x=40,y=400, text='Sem mais,')
cnv.setFont(psfontname='Times-Italic',size=12)
                #NOME FANTASIA DA EMPRESA PARA ASSINATURA:
cnv.drawString(x=40,y=300,text= 'CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.setFont(psfontname='Times-BoldItalic',size=12)
                #IMPRIMIR DATA ATUAL E CIDADE DA SEDE ADMINISTRATIVA NO DOCUMENTO:
cnv.drawString(x=40,y=200,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')


#SALVAR PDF:
cnv.save()"""

#========================================== GERAÇÃO DE TERMO DE ENTREGA DE VEÍCULO ==========================================

cnv = Canvas('GeraPDF.pdf')

#INSERIR IMAGEM DO NOME DO PROGRAMA E LOGO:
cnv.drawImage(r'system_name_logo.png',x=40,y=800,width=190,height=30)
cnv.drawImage(r'system_name_logo.png',x=372,y=10,width=190,height=30)

#INSERIR IMAGEM DOS DADOS DA EMPRESA:
cnv.drawImage(r'company_data.png', x=290, y=710, width=270, height=55)
                #INSERIR DADOS DA EMPRESA
cnv.setFont(psfontname='Times-Roman',size=12)
cnv.drawString(x=298,y=737, text='CLUBE DE BENEFICIOS MÁXIMA PROTEÇÃO')
cnv.drawString(x=298,y=725, text='40.989.892/0001-10')

#INSERIR IMAGEM DO TIPO DE TERMO:
cnv.drawImage(r'term_type.png',x=40,y=710,width=230,height=20)
                #INSERIR TIPO DE TERMO
cnv.setFont(psfontname='Times-Bold',size=12)
cnv.drawString(x=100,y=716.5, text= 'ENTREGA DE VEÍCULO')

#INSERIR IMAGEM DOS DETALHES DO TIPO DE TERMO:
cnv.drawImage(r'details_term_entregadeveiculo.png',x=40,y=560,width=520,height=150)

#INSERIR IMAGEM DOS DADOS DO ASSOCIADO:
cnv.drawImage(r'clientdata_cancel.png',x=40,y=466,width=520,height=94)
#INSERIR DADOS DO ASSOCIADO:
                #NOME/RAZÃO SOCIAL:
cnv.drawString(x=155, y=517, text= 'NOME DO ASSOCIADO')
                #CPF/CNPJ:
cnv.drawString(x=85, y=496, text= 'CPF/CNPJ')
                #MONTADORA:
cnv.drawString(x=285, y=496, text= 'MONTADORA')
                #MODELO:
cnv.drawString(x=415, y=496, text= 'MODELO')
                #ANO:
cnv.drawString(x=85, y=473, text= 'ANO')
                #PLACA:
cnv.drawString(x=265, y=473, text= 'PLACA')
                #COR:
cnv.drawString(x=405, y=473, text= 'COR')

#INSERIR IMAGEM DOS DADOS DO EVENTO:
cnv.drawImage(r'event_data.png', x=40, y=350, width=520, height=115)
#INSERIR DADOS DO EVENTO:
                #DATA:
cnv.drawString(x=70, y=422.5, text='DATA DO EVENTO')

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

cnv.drawString(x=40,y=300, text='Sem mais,')
cnv.setFont(psfontname='Times-Italic',size=12)
                #NOME FANTASIA DA EMPRESA  E DO ASSOCIADO PARA ASSINATURA:
cnv.line(40, 232, 350, 232)
cnv.drawString(x=40,y=220,text= 'CONSULTOR / VISTORIADOR AUTORIZADO')
cnv.line(40, 152, 350, 152)
cnv.drawString(x=40,y=140,text= 'ASSOCIADO (A)')
cnv.setFont(psfontname='Times-BoldItalic',size=12)
                #IMPRIMIR DATA ATUAL E CIDADE DA SEDE ADMINISTRATIVA NO DOCUMENTO:
cnv.drawString(x=40,y=23,text= 'CAMPINA GRANDE ,'  + f' {day} de {month_current} de {year}')


#SALVAR PDF:
cnv.save()