import os
import socket
import tkinter
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import Scale
from tkinter import Frame

from btn_preset_change import btn_preset_change
from gain_command_change import gain_command_change
from rev_slider_change import rev_slider_change
from chorus_slider_change import chorus_slider_change

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

# connect to fluidSynth process
client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connection.connect(('127.0.0.1', 9800))

#current track first row
current_sound_static = Label(window, text='CURRENT SOUND', font=('monospace', 36, 'bold'))
current_track = Label(window, text=soundfonts[current[0]].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10), font=("monospace", 36))
current_sound_static.grid(row=0, column=1)
current_track.grid(row=1, column=1)

#buttons on second row
BUTTON_H = 250
BUTTON_W = 225
back_arrow_img = PhotoImage(file=os.path.join(cwd,'images' ,'back_arrow.png'))
forward_arrow_img = PhotoImage(file=os.path.join(cwd,'images' ,'forward_arrow.png'))


#resize images to fit in button
IMAGE_H = 512
IMAGE_W = 512
REDUCER_H = int(IMAGE_H/BUTTON_H) + 1
REDUCER_W = int(IMAGE_W/BUTTON_W) + 1
back_arrow_img = back_arrow_img.subsample(REDUCER_H, REDUCER_W)
forward_arrow_img = forward_arrow_img.subsample(REDUCER_H, REDUCER_W)

back_arrow_btn = Button(window, image=back_arrow_img, height=BUTTON_H, width=BUTTON_W, command= lambda: btn_preset_change(current_track, soundfonts, current, -1, client_connection))
forward_arrow_btn = Button(window, image=forward_arrow_img, height=BUTTON_H, width=BUTTON_W, command= lambda: btn_preset_change(current_track, soundfonts, current, 1, client_connection))

#position buttons on grid
back_arrow_btn.grid(row=2, column=0)
forward_arrow_btn.grid(row=2, column=2)

slider_frame = Frame(window)
slider_frame.grid(row=2, column=1)


gain_label = Label(slider_frame, text='gain', font=('monospace'))
gain_label.grid(row=1, column=0)
reverb_label = Label(slider_frame, text='reverb', font=('monospace'))
reverb_label.grid(row=1, column=1)
chorus_label = Label(slider_frame, text='chorus', font=('monospace'))
chorus_label.grid(row=1, column=2)
#gain slider
gain_slider = Scale(slider_frame, from_=10, to=0, width=50, length=250, command= lambda x: gain_command_change(gain_slider.get(), client_connection))
gain_slider.set(2)
gain_slider.grid(row=0, column=0)

#reverb slider
rev_slider = Scale(slider_frame, from_=30, to=0, width=50, length=250, command= lambda x: rev_slider_change(rev_slider.get(), client_connection))
rev_slider.set(0)
rev_slider.grid(row=0, column=1)

chorus_slider = Scale(slider_frame, from_=30, to=0, width=50, length=250, command= lambda x: chorus_slider_change(chorus_slider.get(), client_connection))
chorus_slider.set(0)
chorus_slider.grid(row=0, column=2)

#starts
window.mainloop()
