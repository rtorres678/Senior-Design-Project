import os
import socket

# kivy imports
import kivy

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.lang import Builder

def btn_preset_change(label, soundfonts, current, offset, client_connection):
    new_sf2_index = (current[0] + offset) % len(soundfonts)
    #label.config(text=soundfonts[new_sf2_index].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10))
    #label = Label(text = soundfonts[new_sf2_index].split('/')[-1].title().center(10))
    label.text = soundfonts[new_sf2_index].split('/')[-1].split('.')[0].replace('_', ' ')
    current.pop()
    current.append(new_sf2_index)

    command = 'load ' + soundfonts[new_sf2_index] + ' \n'

    
    # Update Background
    #if soundfonts[new_sf2_index] == "Acoustic_Guitar.sf2":
        #self.image_source = "images/acousticguitar.jpg"
        #self.canvas.after.add(Rectangle(source = "/images/acousticguitar.jpg", size = self.size, pos = self.pos))
#         Builder.load_string('''
# <LTunesGUI>
#     canvas.after:
#         Rectangle:
#             source: 'images/acousticguitar.jpg'
#             size: self.size
#             pos: self.pos
# ''')

        
    #self.canvas.ask_update()

    client_connection.send(command.encode())
