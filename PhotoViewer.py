__author__ = 'Souvik'

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import glob


class PHOTOApp(App):

    loc = 0
    files = glob.glob("F:\Camera\*.jpg") #location of the photo
    img = Image(source=files[loc],size_hint=(0.9, 1))


    def build(self):
        layout = BoxLayout(orientation="horizontal")

        button_next = Button(text='>', size_hint=(0.05, 1))
        button_prev = Button(text='<', size_hint=(0.05, 1))

        layout.add_widget(button_prev)
        layout.add_widget(self.img)
        layout.add_widget(button_next)

        button_next.bind(on_press=self.on_next)
        button_prev.bind(on_press=self.on_prev)

        return layout


    def on_next(self,instance):

        if self.loc < len(self.files):
            self.loc += 1
            self.img.source = self.files[self.loc]
        else:
            self.loc = 0


    def on_prev(self,instance):

        if self.loc > -(len(self.files)):
            self.loc -= 1
            self.img.source = self.files[self.loc]
        else:
            self.loc = 0

if __name__ == '__main__':
        PHOTOApp().run()