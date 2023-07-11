# this is part of the SpectroViz project.
#
# Release: v0.1.dev
#
# Copyright ©  2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import base64

from tkinter import Tk, Button, filedialog
from tkinter import messagebox
from tkinter import *

from src.aboult_module import help_info
from src.check_update_module import *
from src.spectrogram_module import spectrogram_extract


window = Tk()
window.title("SpectroViz")
window.geometry("800x600")


custom_font1 = ('Arial', 40)
label = Label(window,
                text="SpectroViz",
                font=custom_font1,).place(x=7, y=10)

custom_font3 = ('Arial', 12)
label = Label(window,
                text="v0.1.dev",
                font=custom_font3,).place(x=280, y=40)


button_spectrogram = Button(window,
                text="Spectrogram",
                command=spectrogram_extract,
                font=('Arial'),
                width=57,
                height=10,).place(x=20, y=280)


menu_barra = Menu(window)

menu_arquivo = Menu(menu_barra, tearoff=0)
menu_arquivo.add_command(label="Help", command=help_info, font=('Arial'))
menu_barra.add_cascade(label="Menu", menu=menu_arquivo)
window.config(menu=menu_barra)

if __name__ == "__main__":
    check_new_version("1.0-rc1")
    window.mainloop()