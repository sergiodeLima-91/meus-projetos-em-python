# Projeto | Sistema Gerador de Termos

*Trata-se de um programa que gera algumas espécies de termos para empresas de proteção veicular.* 
#
## PLANOS E SUAS COBERTURAS
#

Vale destacar que, por estar ainda em desenvolvimento, este programa de computador tem caráter restrito as características de operação da empresa na qual seu desenvolvedor trabalha. Especificamente, tal empresa trabalha com categorias de planos de proteção veicular que se diferenciam de acordo com as coberturas a eles atreladas . 

Eis os nomes dos planos e suas coberturas:

#
|MONITORAMENTO|   
-------------- 
Rastreamento
Monitoramento
#
|BRONZE 01|   
-------------- 
Rastreamento
Monitoramento
Roubo
Furto
Três reboques gratuitos a.a.
#
|BRONZE 02|   
-------------- 
Rastreamento
Monitoramento
Roubo
Furto
Três reboques gratuitos a.a.
Vidros em geral
#
|PRATA 01|   
-------------- 
Rastreamento
Monitoramento
Roubo
Furto
Colisão
Seis reboques gratuitos a.a.
Reboque ilimitado por quebra
Quinhentos quilômetros de reboque
#
|PRATA 02|   
-------------- 
Rastreamento
Monitoramento
Roubo
Furto
Colisão
Seis reboques gratuitos a.a.
Reboque ilimitado por quebra
Quinhentos quilômetros de reboque
Vidros em geral

#
|OURO|    
-------------- 
Rastreamento
Monitoramento
Roubo
Furto
Colisão
Perda Total
Seis reboques gratuitos a.a.
Reboque ilimitado por quebra
Quinhentos quilômetros de reboque
Vidros em geral
#
## TECNOLOGIAS UTILIZADAS
#
### _Linguagem de Programação_

A linguagem de programação utilizada é Python, na sua versão de número 3.11.5. A documentação está disponível [aqui](https://docs.python.org/3.11/).

### _Bibliotecas e Módulos_


| Biblioteca/Módulo | Versão | Documentação|
--------------------|--------|-------------|
PyQt5               | 5.15.2.|[PyQt5](https://doc.qt.io/qt-5.15/)
reportlab           |10.1.0  |[reportlab](https://docs.reportlab.com/)

#
## LAYOUT PRINCIPAL
#
No presente momento, o aplicativo tem o seguinte layout principal, sem outras janelas para as funcionalidades, por enquanto:

![](./layout-sgt.png)

Na primeira **coluna COBERTURAS**, temos a opção, sob a forma de checkboxes, de seleção das coberturas de acordo com o TIPO DE PLANO. Futuramente será implementada a funcionalidade de preenchimento automático das coberturas de acordo com o plano.

A vantagem da seleção manual da cobertura estar disponível é que, em alguns casos, os clientes escolhem não ter alguma das coberturas que fazem parte de algum plano a fim de abater no valor da mensalidade. Por exemplo, um cliente pode optar por retirar a cobertura de perda total do seu plano Ouro.

Em seguida, temos a **coluna DADOS DO CLIENTE**. Aqui são colocados os dados do cliente  a fim de serem colocados no termo que desejar gerar ao final do cadastro.