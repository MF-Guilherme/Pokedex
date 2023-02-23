from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *

######### cores ########

cor0 = "#444466"
cor1 = "#feffff"
cor2 = "#6f9fbd"
cor3 = "#38576b"
cor4 = "#403d3d" #letra
cor5 = "#ef5350"

########## criando a janela ########
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=cor1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, column=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

########## criando frame ########
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=1)

def trocar_pokemon(poke):
    
    global imagem_pokemon, img_pokemon
    
    #trocando a cor de fundo do frame
    frame_pokemon['bg'] = pokemon[poke]['tipo'][3]
    
    nome_pokemon['text'] = poke
    nome_pokemon['bg'] = pokemon[poke]['tipo'][3]
    tipo_pokemon['text'] = pokemon[poke]['tipo'][1]
    tipo_pokemon['bg'] = pokemon[poke]['tipo'][3]
    id_pokemon['text'] = pokemon[poke]['tipo'][0]
    id_pokemon['bg'] = pokemon[poke]['tipo'][3]
    
    # imagem do pokemon
    imagem_pokemon = pokemon[poke]['tipo'][2]
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238,238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)
    img_pokemon = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=pokemon[poke]['tipo'][3], fg=cor1)
    img_pokemon.place(x=60, y=50)

    tipo_pokemon.lift() #para aparecer o texto do tipo por cima da imagem
    
    # status
    hp_pokemon['text'] = pokemon[poke]['status'][0]
    ataque_pokemon['text'] = pokemon[poke]['status'][1]
    defesa_pokemon['text'] = pokemon[poke]['status'][2]
    velocidade_pokemon['text'] = pokemon[poke]['status'][3]
    total_pokemon['text'] = pokemon[poke]['status'][4]
    
    # habilidades
    hb1_pokemon['text'] = pokemon[poke]['habilidades'][0]
    hb2_pokemon['text'] = pokemon[poke]['habilidades'][1]

# nome
nome_pokemon = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=cor1)
nome_pokemon.place(x=12, y=15)

# tipo
tipo_pokemon = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=cor1, fg=cor1)
tipo_pokemon.place(x=12, y=50)


# id
id_pokemon = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=cor1, fg=cor1)
id_pokemon.place(x=12, y=75)


# status
status_pokemon = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=cor1, fg=cor0)
status_pokemon.place(x=15, y=310)

# hp
hp_pokemon = Label(janela, text='HP: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
hp_pokemon.place(x=12, y=360)

# ataque
ataque_pokemon = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
ataque_pokemon.place(x=12, y=385)

# defesa
defesa_pokemon = Label(janela, text='Defesa: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
defesa_pokemon.place(x=12, y=410)

# velocidade
velocidade_pokemon = Label(janela, text='Velocidade: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
velocidade_pokemon.place(x=12, y=435)

# total
total_pokemon = Label(janela, text='Total: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
total_pokemon.place(x=12, y=460)

# habilidades
habilidades_pokemon = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=cor1, fg=cor0)
habilidades_pokemon.place(x=180, y=310)

# habilidade 1
hb1_pokemon = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
hb1_pokemon.place(x=180, y=360)

# habilidade 2
hb2_pokemon = Label(janela, text='Cabeçada', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=cor1, fg=cor4)
hb2_pokemon.place(x=180, y=385)

# Criando botões para pokemons

imagem_pokemon_1 = Image.open(r'images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

botao_pokemon_1 = Button(janela, command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_1.place(x=375, y=10)

imagem_pokemon_2 = Image.open(r'images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

botao_pokemon_2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_2.place(x=375, y=70)

imagem_pokemon_3 = Image.open(r'images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

botao_pokemon_3 = Button(janela, command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_3.place(x=375, y=130)

imagem_pokemon_4 = Image.open(r'images/cabeca-gyarados.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

botao_pokemon_4 = Button(janela, command=lambda:trocar_pokemon('Gyarados'), image=imagem_pokemon_4, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_4.place(x=375, y=190)

imagem_pokemon_5 = Image.open(r'images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

botao_pokemon_5 = Button(janela, command=lambda:trocar_pokemon('Gengar'), image=imagem_pokemon_5, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_5.place(x=375, y=250)

imagem_pokemon_6 = Image.open(r'images/cabeca-dragonite.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

botao_pokemon_6 = Button(janela, command=lambda:trocar_pokemon('Dragonite'), image=imagem_pokemon_6, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=cor1, fg=cor0)
botao_pokemon_6.place(x=375, y=310)


#pegando um pokemon aleatóro para iniciar a pokedex
import random
lista_pokemons = ['Pikachu', 'Bulbasaur', 'Charmander', 'Gengar', 'Dragonite', 'Gyarados']
pokemon_escolhido = random.sample(lista_pokemons, 1)

#iniciando o programa
trocar_pokemon(pokemon_escolhido[0])
janela.mainloop()