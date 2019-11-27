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

option0 = os.path.join(cwd, 'sf2', 'JR_sax.sf2')
option1 = os.path.join(cwd, 'sf2', 'JR_organ.sf2')
option2 = os.path.join(cwd, 'sf2', 'JR_church.SF2')
option3 = os.path.join(cwd, 'sf2', 'JR_male.sf2')
option4 = os.path.join(cwd, 'sf2', 'JR_bells.SF2')
option5 = os.path.join(cwd, 'sf2', 'JR_elepiano.sf2')
option6 = os.path.join(cwd, 'sf2', 'JR_analog.sf2')
soundfonts = [option0, option1, option2, option3, option4, option5, option6] 

window = Tk()
window.attributes('-fullscreen', True)
window.title("Preset Manager")

# a list so it can be changed in lambda function
current = [0]

#current track first row
current_sound_static = Label(window, text='Current Sound', font=('monospace', 26))
current_track = Label(window, text=soundfonts[current[0]].split('/')[-1].split('_')[-1].split('.')[0].title().center(10), font=("monospace", 26))
current_sound_static.grid(row=0, column=1)
current_track.grid(row=1, column=1)

#buttons on second row
BUTTON_H = 200
BUTTON_W = 200
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
gain_slider = Scale(window, from_=10, to=0, width=35, length=200, command= lambda x: gain_command_change(gain_slider.get()))
gain_slider.set(5)
gain_slider.grid(row=2, column= 1)

#starts
window.mainloop()
