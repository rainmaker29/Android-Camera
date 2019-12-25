__version__ = '1.0'

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from plyer import camera


class UI(FloatLayout):
    def __init__(self,**kwargs):
        super(UI,self).__init__(**kwargs)
        self.lblCam = Label(text="Click to take picture")
        self.add_widget(self.lblCam)

    def on_touch_down(self,e):
        camera.take_picture('/Internal shared storage/Picture',self.done)

    def done(self,e):
        self.lblCam.text = e


class Camera(App):
    def build(self):

        ui = UI()
        return ui

    def on_pause(self):
        return true

    def on_resume(self):
        pass
    
Camera().run()
