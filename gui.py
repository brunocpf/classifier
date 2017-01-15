#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Mini Pokédex - Interface gráfica

    Leia README.rst para instruções de execução e detalhes da implementação.

Uso:
    gui.py
'''
import webbrowser

import pokedex
import tkFileDialog as fdlg
import tkMessageBox
import ttk
from Tkinter import *


class Window(Frame):
    '''
    classe responsável pela janela da interface
    '''
    def __init__(self, parent, w, h):
        Frame.__init__(self, parent)
        self.parent = parent
        self.file_entry = None
        self.init_ui(w, h)

    def init_ui(self, width, height):
        '''
        inicializa o layout da interface
        '''
        self.parent.title("Mini Pokédex")
        self.center_window(width, height)
        self.pack(fill=BOTH, expand=1)
        self.create_frames()

    def center_window(self, width, height):
        '''
        centraliza a janela da interface na tela
        '''
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - width) / 2
        y = (sh - height) / 2
        self.parent.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def create_frames(self):
        '''
        cria os widgets da interface
        '''
        file_label = ttk.Label(self, text='Selecione uma imagem: ')
        file_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.file_entry = ttk.Entry(self, width=42)
        self.file_entry.grid(row=0, column=1, sticky=W+E)
        file_button = ttk.Button(self,
                                 text='Escolher arquivo...',
                                 command=self.file_dialog)
        file_button.grid(row=0, column=2, sticky=W+E, padx=5)
        find_pokemon_button = ttk.Button(self,
                                         text='Identificar Pokémon',
                                         command=self.find_pokemon)
        find_pokemon_button.grid(column=1, sticky=W+E)

    def file_dialog(self):
        '''
        abre a janela de escolha de arquivos
        '''
        init_file = self.file_entry.get()
        opts = {'initialfile': init_file,
                'filetypes': (('Imagens',
                               '.bmp .pgm .ppm .sr .ras .jpeg .jpg .jpe .jp2 .tiff .tif .png .'),)}
        opts['title'] = 'Selecione um arquivo para abrir...'
        fn = fdlg.askopenfilename(**opts)
        if fn and self.file_entry:
            self.file_entry.delete(0, END)
            self.file_entry.insert(END, fn)
        if fn == '':
            return None
        return fn

    def find_pokemon(self):
        '''
        encontra o pokémon e abre a página correspondente na pokédex
        '''
        input_file = self.file_entry.get()
        if input_file in [None, ""]:
            return
        pokemon_name = pokedex.find_pokemon(input_file)
        if pokemon_name is None:
            tkMessageBox.showinfo("Erro", u"Pokémon não identificado")
            return
        url = "http://www.pokemon.com/br/pokedex/" + pokemon_name
        webbrowser.open_new(url)


def main():
    '''
    main
    '''
    root = Tk()
    root.resizable(width=TRUE, height=FALSE)
    ex = Window(root, 540, 80)
    root.mainloop()


if __name__ == '__main__':
    main()
