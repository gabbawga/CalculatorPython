# importando o tkinder
import re
from tkinter import *
from turtle import width          # * em python importa tudo que há na biblioteca



#cores
corPreta =  "#000000"        
corAzul =   "#38576b"
corLaranja ="#FFA500"
corBranca = '#ffffff'

# inicio do programa:

#criando a janela:
#front da calculadora:
 
janela = Tk()                  # Passo inicial para criar uma  janela -> Variavel recebe Tk()
janela.title("Calculadora")    # O titulo da janela é dado com .title

janela.geometry("235x318")     # .geometry é utilizado para  as medidas da janela onde 1° numero é a largura 
                               # e 2° é altura
janela.config(bg = corPreta )  # configura o background da tela para 'bg' significa backgorund

#-----------------------------------------------------------------------------------------------------------

# Frames: 
# Funciona como um container, que é responsável por organizar a posição de outros widgets. 
# Ele usa áreas retangulares na tela para organizar o layout e fornecer preenchimento desses widgets.

frame_tela = Frame(janela, width = 235, height = 50, bg = corAzul) 
frame_tela.grid(row=0, column=0)             

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row=1, column=0)  
#------------------------------------------------------------------------------------------------------------

todos_valores = ''

#função para setar os valores dos botões na tela
def entra_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    valores_texto.set(todos_valores)

#função para calcular os valores
def calcular():
    global todos_valores
    igual = eval(todos_valores)
    valores_texto.set(str(igual))
    
#função par limpar a tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valores_texto.set('')


#------------------------------------------------------------------------------------------------------------
#Criando label

valores_texto = StringVar()
app_label = Label(frame_tela, textvariable = valores_texto , fg=corBranca, bg= corAzul, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 '))
app_label.place(x=0,y=0)



#-------------------------------------------------------------------------------------------------------------
#Botões:
# Configuramos 'b_1' para ser um botão e colocamos seus parametros e suas cordenadas na janela
# e tambem fonte e background
b_1 = Button(frame_corpo, command = limpar_tela, text = "C", width = 11, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0 , y=0)

b_2 = Button(frame_corpo, command = lambda: entra_valores('%'), text = "%", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118 , y=0)

b_3 = Button(frame_corpo, command = lambda: entra_valores('/'), text = "/", width = 5, height = 2, background = corLaranja, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# Botões dos numeros:
b_4 = Button(frame_corpo, command = lambda: entra_valores('7'),text = "7", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0 , y=52)

b_5 = Button(frame_corpo, command = lambda: entra_valores('8'),text = "8", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, command = lambda: entra_valores('9'),text = "9", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118 , y=52)

b_7 = Button(frame_corpo, command = lambda: entra_valores('4'),text = "4", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0 , y=104)

b_8 = Button(frame_corpo, command = lambda: entra_valores('5'),text = "5", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=104)

b_9 = Button(frame_corpo, command = lambda: entra_valores('6'),text = "6", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118 , y=104)

b_10 = Button(frame_corpo, command = lambda: entra_valores('1'),text = "1", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0 , y=156)

b_11 = Button(frame_corpo, command = lambda: entra_valores('2'),text = "2", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=59, y=156)

b_12 = Button(frame_corpo, command = lambda: entra_valores('3'),text = "3", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=118 , y=156)

b_13 = Button(frame_corpo, command = lambda: entra_valores('0'),text = "0", width = 11, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0 , y=208)

b_14 = Button(frame_corpo, command = lambda: entra_valores('.'),text = ".", width = 5, height = 2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118 , y=208)

b_14 = Button(frame_corpo, command = lambda: entra_valores('+'),text = "+", width = 5, height = 2, font=('Ivy 13 bold'), background= corLaranja,relief=RAISED, overrelief=RIDGE)
b_14.place(x=177 , y=52)

b_14 = Button(frame_corpo, command = lambda: entra_valores("-"),text = "-", width = 5, height = 2, font=('Ivy 13 bold'), background= corLaranja,relief=RAISED, overrelief=RIDGE)
b_14.place(x=177 , y=104)

b_14 = Button(frame_corpo, command = lambda: entra_valores('*'),text = "*", width = 5, height = 2, font=('Ivy 13 bold'),background= corLaranja, relief=RAISED, overrelief=RIDGE)
b_14.place(x=177 , y=156)

b_14 = Button(frame_corpo, command = calcular,text = "=", width = 5, height = 2, font=('Ivy 13 bold'),background= corLaranja, relief=RAISED, overrelief=RIDGE)
b_14.place(x=177 , y=208)

#--------------------------------------------------------------------------------------------------------------
#criando função:


janela.mainloop()  #criação da janela dado com o comando .mainloop
