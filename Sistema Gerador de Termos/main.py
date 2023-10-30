import pyautogui
from PySimpleGUI import (Text, Input, Button,
    Column,VSeparator,HSeparator,Push,Window,WIN_CLOSED, Image,Radio,theme,popup_ok,popup_cancel,popup_no_buttons
)
from time import sleep
from datetime import date
import os
import pandas as pd
import win32com.client as win32


theme('LightGreen')

layout_logo = [
    [Image(filename=r'C:\Users\Administrador\OneDrive\Sérgio Lima\Estudos\Curso de Programação\Python\pythonAutomacao\PMS - Policyholder Management System\Images\logo200x191.png')]
]

layout_barrier_initial = [
    [Image(filename=r'C:\Users\Administrador\OneDrive\Sérgio Lima\Estudos\Curso de Programação\Python\pythonAutomacao\PMS - Policyholder Management System\Images\column.png')],
]
layout_barrier_final = [
    [Image(filename=r'C:\Users\Administrador\OneDrive\Sérgio Lima\Estudos\Curso de Programação\Python\pythonAutomacao\PMS - Policyholder Management System\Images\column.png')],
]

layout_left = [
    [Image(filename='plain.png')],
    [Radio('Monitoramento', "Plain_Type",key='monitoring',default=False)],
    [Radio('Bronze 1', "Plain_Type", key='bronze1',default=True)],
    [Radio('Bronze 2', "Plain_Type",key='bronze2',default=False)],
    [Radio('Prata 1', "Plain_Type",key='silver1',default=False)],
    [Radio('Prata 2', "Plain_Type",key='silver2',default=False)],
    [Radio('Ouro', "Plain_Type", key='gold',default=False)],
    [Image(filename='clientdata.png')],
    [Text('Nome            '), Input(key='name')],
    [Text('CPF              '), Input(key='cpf')],
    [Image(filename='vehicle.png')],
    [Text('Montadora      '), Input(key='assembler')],
    [Text('Modelo           '), Input(key='model')],
    [Text('Placa             '), Input(key='plate')],
    [Text('Cor                '), Input(key='color')],
    [
        Push(),
        Button('Gerar Termo de Adesão'),
        Button('Cancelar')
    ],
    [
    Push(),
    Push(),
    Image(filename='mark_dev_sergiolima.png')
    ]
]

layout = [
    [Column(layout_logo), Column(layout_barrier_initial), VSeparator(), Column(layout_left), VSeparator(), Column(layout_barrier_final)]
]

window = Window('MRS Vehicle Protection',layout=layout,icon='icon.ico')

while True:
    event, value = window.read()
    if event == WIN_CLOSED or event == 'Cancelar':
        break

    #Popups messages:
    if value['name'] == '':
        popup_ok('Nome inválido!',icon='icon.ico', background_color='LightGreen')
    elif value['cpf'].isnumeric() == False:
        popup_ok('CPF inválido!',icon='icon.ico', background_color='LightGreen')
    elif value['assembler'] == '':
        popup_ok('Montadora inválida!',icon='icon.ico', background_color='LightGreen')
    elif value['model'] == '':
        popup_ok('Modelo inválido!',icon='icon.ico', background_color='LightGreen')
    elif value['plate'] == '':
        popup_ok('Placa inválida!',icon='icon.ico', background_color='LightGreen')
    elif value['color'] == '':
        popup_ok('Cor inválida!',icon='icon.ico', background_color='LightGreen')
  
    else:
        #Open File            
        file = os.startfile(r'C:\Users\Administrador\OneDrive\Sérgio Lima\Estudos\Curso de Programação\Python\pythonAutomacao\MRS Vehicle Protection\termo_de_adesao.docx')
        print(file)

        #Closed warning windows:
        sleep(15)
        pyautogui.press('esc')
        sleep(5)
        pyautogui.click(x=1350, y=176)

        #------------------Insert Informations in File------------------
        
        #Insert Plain Type:

        if value['monitoring'] == True:
            plain_name = 'MONITORAMENTO'
        elif value['bronze1'] == True:
            plain_name = 'BRONZE 1'
        elif value['bronze2'] == True:
            plain_name = 'BRONZE 2'
        elif value['silver1'] == True:
            plain_name = 'PRATA 1'
        elif value['silver2'] == True:
            plain_name = 'PRATA 2'
        elif value['gold'] == True:
            plain_name = 'OURO'
        
        sleep(3)
        pyautogui.tripleClick(x=758, y=420)
        pyautogui.write(plain_name)


        #Insert name:
        sleep(1)
        pyautogui.tripleClick(x=463, y=606)
        pyautogui.write(value['name'])
        for tab in range(2):
            pyautogui.press('tab')

        #Insert CPF:
        sleep(1)
        pyautogui.write(value['cpf'])

        #Mouse Down to Vehicle Data:
        for click in range(33):
            pyautogui.click(x=1364, y=700)

        #Insert ASSEMBLER:
        pyautogui.tripleClick(x=464, y=214)
        pyautogui.write(value['assembler'])
        for tab in range(2):
            pyautogui.press('tab')

        #Insert MODEL:
        pyautogui.write(value['model'])
        for tab in range(2):
            pyautogui.press('tab')

        #Insert PLATE:
        pyautogui.write(value['plate'])
        for tab in range(2):
            pyautogui.press('tab')

        #Insert COLOR:
        pyautogui.write(value['color'])

        #Plans:
        monitoring = [
            'Monitoramento',
            'Rastreamento'
            ]
        bronze1 = [
            'Monitoramento',
            'Rastreamento',
            'Roubo',
            'Furto',
            '3 reboques gratuitos a.a. a cada 120 dias (CG - JP - GB)'
        ]
        bronze2 = [
            'Monitoramento',
            'Rastreamento',
            'Roubo',
            'Furto',
            '3 reboques gratuitos a.a. a cada 120 dias (CG - JP - GB)',
            'Vidros em geral'
        ]
        silver1 = [
            'Monitoramento',
            'Rastreamento',
            'Roubo',
            'Furto',
            'Colisao do associado',
            '6 reboques gratuitos a.a. a cada 60 dias',
            'Reboque ilimitado com participacao meio a meio (CG - JP - GB)',
            '500 Km de reboque'
        ]
        silver2 = [
            'Monitoramento',
            'Rastreamento',
            'Roubo',
            'Furto',
            'Colisao do associado',
            '6 reboques gratuitos a.a. a cada 60 dias',
            'Reboque ilimitado com participacao meio a meio (CG - JP - GB)',
            '500 Km de reboque',
            'Vidros em geral'
        ]
        gold = [
            'Monitoramento',
            'Rastreamento',
            'Roubo',
            'Furto',
            'Colisao do associado',
            '6 reboques gratuitos a.a. a cada 60 dias',
            'Reboque ilimitado com participacao meio a meio (CG - JP - GB)',
            '500 Km de reboque',
            'Vidros em geral',
            'Terceiros'
        ]
        #Delete  Previous Coverage :
        pyautogui.click(x=368, y=365)
        sleep(1)
        pyautogui.click(x=330, y=346)
        sleep(1)
        pyautogui.press('delete')

        #Insert New Coverage:

        if event ==  'Gerar Termo de Adesão':
            if value['monitoring'] == True:
                plain_coverage = monitoring
            elif value['bronze1'] == True:
                plain_coverage = bronze1
            elif value['bronze2'] == True:
                plain_coverage = bronze2
            elif value['silver1'] == True:
                plain_coverage = silver1
            elif value['silver2'] == True:
                plain_coverage = silver2
            elif value['gold'] == True:
                plain_coverage = gold

        
        pyautogui.click(x=368, y=365)
        for cove in range(len(plain_coverage)):
            pyautogui.write(plain_coverage[cove])
            if cove  < len(plain_coverage) - 1:
                pyautogui.press('tab')

        #Mouse Down to Insert the Current Date:
        for click in range(37):
            pyautogui.click(x=1364, y=700)

        # Insert Current Date:
        pyautogui.tripleClick(x=412, y=613)
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

        sleep(1)
        pyautogui.write(f'Campina Grande, {day} de {month_current} de {year}')

        #------------------Save as PDF------------------
        # File:
        sleep(2)
        pyautogui.click(x=27, y=50)
        #Save as:
        sleep(3)
        pyautogui.click(x=66, y=371)
        # Search:
        sleep(5)
        pyautogui.click(x=286, y=451)
        #Desktop:
        sleep(3)
        pyautogui.click(x=107, y=157)
        #Name File:
        pyautogui.doubleClick(x=182, y=563)
        pyautogui.write(f'{value["name"]} - ' + plain_name)
        #File Type:
        pyautogui.click(x=159, y=586)
        sleep(2)
        pyautogui.press('P')
        #Save:
        pyautogui.doubleClick(x=1193, y=693)
        