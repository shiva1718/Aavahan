from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from android.permissions import request_permissions, Permission

Window.size = (310, 580)

class Slope(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager


LabelBase.register(name="MPoppins", fn_regular="Black.ttf")
LabelBase.register(name="BPoppins", fn_regular="Italic.ttf")
Slope().run()
