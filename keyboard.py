# import modules
try:
    import Tkinter
except:
    import tkinter as Tkinter
import os
from pygame import mixer
from gtts import gTTS
from pynput.mouse import Button, Controller

keys = [[[("keyboard"), ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
         [
                ('AEIOU', "Voltar", 'A', 'E', 'I', 'O', 'U', 'Sim', 'Bom Dia'),
                ('BCDFG', "Voltar", 'B', 'C', 'D', 'F', 'G', 'Nao', 'Boa Tarde'),
                ('HJKLM', "Voltar", 'H', 'J', 'K', 'L', 'M', 'Obrigado', 'Boa Noite'),
                ('NPQRS', "Voltar", 'N', 'P', 'Q', 'R', 'S', 'Banheiro', 'Calor'),
                ('TVXWY', "Voltar", 'T', 'V', 'X', 'W', 'Y', 'Chuveiro', 'Frio'),
                ('Z1234', "Voltar", 'Z', '1', '2', '3', '4', 'Fome', 'Ver TV'),
                ('56789', "Voltar", '5', '6', '7', '8', '9', '0', 'Sede'),
                ('SSDN', 'Voltar', 'Espaco', 'Falar', 'Apagar',  "Oi", 'Tchau', "Erase All", 'Exit'),
         ]]]]


def falar(parameter):
    texto = parameter
    tts = gTTS(text=texto, lang='pt')
    tts.save("file.mp3")
    mixer.init()
    mixer.music.load("file.mp3")
    mixer.music.play()
    rat_loop.vertical = True
    rat_loop.i = 0
    rat_loop.j = 0
    while mixer.music.get_busy():
        pass
    mixer.music.load("file1.mp3")
    os.remove("file.mp3")
    return
# Frame Class


class Keyboard(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)
        # Function For Creating Buttons
        self.create_frames_and_buttons()
        return
    # Function For Extracting Data From KeyBoard Table
    # and then provide us a well looking
    # keyboard gui

    def create_frames_and_buttons(self):
        # take section one by one
        texto = Tkinter.Label(text='Texto')
        texto.pack()
        global janela_texto
        janela_texto = Tkinter.Entry(width=80, bd=2)
        janela_texto.pack()

        for key_section in keys:
            # create Sperate Frame For Every Section
            store_section = Tkinter.Frame(self)
            store_section.pack(side='left', expand='yes', fill='both', padx=10, pady=10, ipadx=10, ipady=10)

            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = Tkinter.LabelFrame(store_section)
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Tkinter.Frame(store_layer)
                    store_key_frame.pack(side='top', expand='yes', fill='both')
                    for k in key_bunch:
                        store_button = Tkinter.Button(store_key_frame, text=k, width=7, height=3)
                        # flat, groove, raised, ridge, solid, or sunken
                        store_button['relief'] = "raised"
                        store_button['bg'] = "#00002f"
                        store_button['fg'] = "#ffffff"
                        store_button['cursor'] = 'dotbox'
                        store_button['command'] = lambda q=k: self.button_command(q)
                        store_button.pack(side='left', fill='both', expand='yes')
        return

        # Function For Detecting Pressed Keyword.
    def button_command(self, event):
        if event == 'Oi':
            rat_loop.fala = ''
            rat_loop.fala += str(event)
            falar(rat_loop.fala)
            rat_loop.fala = ''
        elif len(event) <= 2:
            janela_texto.delete(0, 'end')
            rat_loop.texto += str(event)
            janela_texto.insert(0, rat_loop.texto)
            print(rat_loop.texto)
            rat_loop.vertical = True
            rat_loop.i = 0
            rat_loop.j = 0
        elif event == 'Apagar':
            janela_texto.delete(0, 'end')
            rat_loop.texto = rat_loop.texto[:-1]
            janela_texto.insert(0, rat_loop.texto)
            print(rat_loop.texto)
        elif event == 'Erase All':
            janela_texto.delete(0, 'end')
            rat_loop.texto = ''
            rat_loop.vertical = True
        elif event == 'AEIOU':
            rat_loop.vertical = False
        elif event == 'BCDFG':
            rat_loop.vertical = False
        elif event == 'HJKLM':
            rat_loop.vertical = False
        elif event == 'NPQRS':
            rat_loop.vertical = False
        elif event == 'TVXWY':
            rat_loop.vertical = False
        elif event == 'Z1234':
            rat_loop.vertical = False
        elif event == '56789':
            rat_loop.vertical = False
        elif event == 'SSDN':
            rat_loop.vertical = False
        elif event == 'Falar':
            falar(rat_loop.texto)
        elif event == 'Espaco':
            janela_texto.delete(0, 'end')
            rat_loop.texto += ' '
            janela_texto.insert(0, rat_loop.texto)
            rat_loop.vertical = True
            rat_loop.i = 0
            rat_loop.j = 0
        elif event == 'Voltar':
            rat_loop.vertical = True
            rat_loop.i = 0
            rat_loop.j = 0
        elif event == 'Exit':
            rat_loop.turn_on = False
        elif len(event) >= 3:
            rat_loop.fala = ''
            rat_loop.fala += str(event)
            falar(rat_loop.fala)
            rat_loop.fala = ''
        else:
            pass
        return


class RAT:
    def __init__(self):
        self.vertical = True
        self.x_position = 440
        self.y_position = 40
        self.i = 0
        self.j = 0
        self.turn_on = True
        self.fala = ''
        self.texto = ''
        self.time = 1200
        return

    def mouse(self):
        mouse = Controller()
        while True:
            if rat_loop.vertical is True:
                if rat_loop.i == 0:
                    rat_loop.y_position = 40
                    rat_loop.x_position = 440
                    rat_loop.y_position += 25
                    mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    root.after(rat_loop.time)
                    rat_loop.i += 1
                else:
                    rat_loop.y_position += 60
                    if rat_loop.i == 1:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 2:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 3:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 4:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 5:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 6:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 7:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.i == 8:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    rat_loop.i += 1
                    root.after(rat_loop.time)
                    if rat_loop.i == 9:
                        rat_loop.i = 0
            else:
                if rat_loop.j == 0:
                    rat_loop.x_position = 440
                    rat_loop.x_position += 60
                    mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    root.after(rat_loop.time)
                    rat_loop.j += 1
                else:
                    rat_loop.x_position += 60
                    if rat_loop.j == 1:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 2:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 3:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 4:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 5:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 6:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    if rat_loop.j == 7:
                        mouse.position = (rat_loop.x_position, rat_loop.y_position)
                    rat_loop.j += 1
                    root.after(rat_loop.time)
                    if rat_loop.j == 8:
                        rat_loop.j = 0
            return
# Creating Main Window
# def main():


rat_loop = RAT()
root = Tkinter.Tk(className=" Pisque para Digitar")
root.geometry('600x540+380+0')# size x position of window
keyboard = Keyboard(root).pack()
while rat_loop.turn_on:
    root.update_idletasks()
    root.update()
    rat_loop.mouse()
