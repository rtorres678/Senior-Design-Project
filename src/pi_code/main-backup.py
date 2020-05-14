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

# soundfont CC change
from btn_preset_change import btn_preset_change
from gain_command_change import gain_command_change
from rev_slider_change import rev_slider_change
from chorus_slider_change import chorus_slider_change

# get into the correct working directory
cwd = os.getcwd()
soundfonts = []

for root, dirs, files in os.walk(os.path.join(cwd, 'sf2_new')):
    for file in files:
        soundfonts.append(os.path.join(root, file))
        
print(soundfonts)

# a list so it can be changed in lambda function
current = [0]

# connect to fluidSynth process
client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connection.connect(('127.0.0.1', 9800))

Builder.load_string('''
<LTunesGUI>
    canvas:
        Rectangle:
            source: 'images/harp.jpg'
            size: self.size
            pos: self.pos
''')

class LTunesGUI(GridLayout):
    def __init__(self, **kwargs):
        super(LTunesGUI, self).__init__(**kwargs) # override to add widgets and to define their behavior
        self.cols = 3
        self.rows = 3
        self.padding = 30

        self.pos_hint = {'center_x': .5}

        # Top Left Cell
        self.add_widget(Label(text = ''))

        # Top Middle Cell
        self.inside = GridLayout() # creating a sub-gridlayout
        self.inside.cols = 1

        # self.current_sound_static = Label(text = '[b][color=FFFFFF]CURRENT SOUND[/color][/b]', font_size = 50, font_name = 'HelveticaNeue.ttc', markup = True, italic = True, outline_color = (22,126,245))
        self.current_sound_static = Label(text = 'CURRENT SOUND', font_size = 70, font_name = 'HelveticaNeue', italic = True, outline_color = (22,126,245))

        self.inside.add_widget(self.current_sound_static)
        
        # Current Preset State
        #self.current_preset = Label(text = soundfonts[current[0]].split('/')[-1].split('.')[0].replace('_', ' ').title().center(10), font_size = 45, font_name = ('HelveticaNeue'))
        self.current_preset = Label(text = soundfonts[current[0]].split('/')[-1].split('.')[0].replace('_', ' '), font_size = 45, font_name = ("HelveticaNeue"))
        self.inside.add_widget(self.current_preset)
        
        #self.inside.add_widget(Label(text = 'S T R I N G S', font_size = 50, italic = True))

        self.add_widget(self.inside) # required

        # Top Right Cell
        self.add_widget(Label(text = ''))

        # Middle Left Cell - PREV Button
        prev_preset = Button(size_hint = (None, None), height = int(Window.height) / 4, background_normal = ('images/leftarrow-v2.png'), background_down = ('images/leftarrowdown-v3.png'))
        prev_preset.bind(on_press = lambda b: btn_preset_change(self.current_preset, soundfonts, current, -1, client_connection))

        self.add_widget(prev_preset)

        # Middle Middle Cell
        self.inside2 = GridLayout() # creating a sub-gridlayout for the sliders
        self.inside2.cols = 1

        ## self.inside3 = GridLayout() # creating another sub-gridlayout for labels + value indicators
        ## self.inside3.cols = 2
        ## self.inside3.rows = 1

        self.inside2.add_widget(Label(text = 'VOLUME', font_size = 20, font_name = 'HelveticaNeue'))
        # self.inside2.add_widget(Label(text = 'XX%'))

        self.vol_slider = Slider(min = 0, max = 10, orientation = 'horizontal', value_track = True, value_track_color=[1, 0, 0, 1])
        self.inside2.add_widget(self.vol_slider)
        self.vol_slider.value = 2
        self.vol_slider.bind(on_touch_move = lambda x, y: gain_command_change(self.vol_slider.value, client_connection))

        self.inside2.add_widget(Label(text = 'REVERB', font_size = 20, font_name = 'HelveticaNeue'))
        self.rev_slider = Slider(min = 0, max = 30, orientation = 'horizontal', value_track = True, value_track_color=[1, 0, 0, 1])
        self.inside2.add_widget(self.rev_slider)
        # self.rev_slider.bind(self.rev_slider_change)
        self.rev_slider.value = 0
        self.rev_slider.bind(on_touch_move = lambda i, j: rev_slider_change(self.rev_slider.value, client_connection))


        self.inside2.add_widget(Label(text = 'CHORUS', font_size = 20, font_name = 'HelveticaNeue'))
        self.chor_slider = Slider(min = 0, max = 30, orientation = 'horizontal', value_track = True, value_track_color=[1, 0, 0, 1])
        self.inside2.add_widget(self.chor_slider)
        # self.chor_slider.bind(self.chorus_slider_change)
        self.chor_slider.value = 0
        self.chor_slider.bind(on_touch_move = lambda c, d: chorus_slider_change(self.chor_slider.value, client_connection))


        self.add_widget(self.inside2) # required

        # Middle Right Cell - NEXT Button
        next_preset = Button(size_hint = (None, None), height = int(Window.height) / 4, background_normal = ('images/rightarrow-v2.png'), background_down = ('images/rightarrowdown-v2.png'))
        next_preset.bind(on_press = lambda a: btn_preset_change(self.current_preset, soundfonts, current, 1, client_connection))
        self.add_widget(next_preset)

        # Bottom Left Cell
        self.add_widget(Label(text = ''))

        # Bottom Middle Cell
        self.add_widget(Label(text = ''))

        # Bottom Right Cell
        self.add_widget(Label(text = ''))

class LTunes(App):
    def build(self):
        return LTunesGUI()

if __name__ == '__main__':
    LTunes().run()


# class LTunesGUI(App):
#     def build(self, **kwargs):
