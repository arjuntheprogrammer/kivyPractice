from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

import random

class ScatterTextWidget(BoxLayout):
    text_color = ListProperty([1,0,0,1])
    def change_label_color(self, *args):
        color = [random.random() for i in xrange(3)] + [1]
        # label = self.ids['my_label']
        # label.color = color
        # label1 = self.ids.label1
        # label2 = self.ids.label2
        # label1.color = color
        # label2.color = color
        self.text_color = color

class ScatterApp(App):
    def build(self):
        return ScatterTextWidget()

if __name__ == "__main__":
    ScatterApp().run()
