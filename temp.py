__author__ = 'Souvik'

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import glob
'''
files = glob.glob("F:\Camera\*.jpg")
i = 0
for f in files:
    print(f)
    i += 1

print('Count = {}'.format(i))'''



class Nemo(App):

    def build(self):

        files = glob.glob("F:\Camera\*.jpg")
        img = Image(source=files[0],size_hint=(0.9,0.9))

        main_layout = BoxLayout(orientation = "horizontal")
        #self.desc = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        button_1 = Button(text='<', size_hint=(0.05,0.9))
        button_2 = Button(text='>', size_hint=(0.05,0.9))

        main_layout.add_widget(button_1)
        main_layout.add_widget(button)
        main_layout.add_widget(button_2)

        return main_layout

if __name__ == '__main__':
    Nemo().run()



