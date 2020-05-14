from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
    orientation: "vertical"
    Button:
        Image:
            source: 'images/leftarrow-v1.png'
            y: self.parent.center_y
            x: self.parent.center_x
            size: 250, 250
            allow_stretch: True
""")

class ButtonsApp(App, BoxLayout):
    def build(self):
        return self

if __name__ == "__main__":
    ButtonsApp().run()
