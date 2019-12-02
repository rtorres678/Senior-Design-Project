import os
import socket
import tkinter
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import Scale

from btn_preset_change import btn_preset_change
from gain_command_change import gain_command_change

cwd = os.getcwd()
soundfonts = []

for root, dirs, files in os.walk(os.path.join(cwd, 'sf2')):
    for file in files:
        soundfonts.append(os.path.join(root, file))

window = Tk()
window.attributes('-fullscreen', True)
window.title("Preset Manager")

# a list so it can be changed in lambda function
current = [0]

#current track first row
current_sound_static = Label(window, text='CURRENT SOUND', font=('monospace', 36, 'bold'))
current_track = Label(window, text=soundfonts[current[0]].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10), font=("monospace", 36))
current_sound_static.grid(row=0, column=1)
current_track.grid(row=1, column=1)

#buttons on second row
BUTTON_H = 250
BUTTON_W = 250
back_arrow_img = PhotoImage(file=os.path.join(cwd,'images' ,'back_arrow.png'))
forward_arrow_img = PhotoImage(file=os.path.join(cwd,'images' ,'forward_arrow.png'))


#resize images to fit in button
IMAGE_H = 512
IMAGE_W = 512
REDUCER_H = int(IMAGE_H/BUTTON_H) + 1
REDUCER_W = int(IMAGE_W/BUTTON_W) + 1
back_arrow_img = back_arrow_img.subsample(REDUCER_H, REDUCER_W)
forward_arrow_img = forward_arrow_img.subsample(REDUCER_H, REDUCER_W)

back_arrow_btn = Button(window, image=back_arrow_img, height=BUTTON_H, width=BUTTON_W, command= lambda: btn_preset_change(current_track, soundfonts, current, -1))
forward_arrow_btn = Button(window, image=forward_arrow_img, height=BUTTON_H, width=BUTTON_W, command= lambda: btn_preset_change(current_track, soundfonts, current, 1))

#position buttons on grid
back_arrow_btn.grid(row=2, column=0, padx=(10,50))
forward_arrow_btn.grid(row=2, column=2)


#make slider
gain_slider = Scale(window, from_=10, to=0, width=35, length=250, command= lambda x: gain_command_change(gain_slider.get()))
gain_slider.set(5)
gain_slider.grid(row=2, column= 1)

#starts
window.mainloop()
