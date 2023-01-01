from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.utils import platform

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
else:
    print(platform)

Window.size = (310, 580)


class Slope(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        # screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("map.py"))
        return screen_manager

    def request_gps_permission(self, instance):
        # Request the GPS permission
        request_permission(Permission.LOCATION, self.grant_permission)

    def grant_permission(self, permission, granted):
        # If the permission is granted, show a message
        if granted:
            print("Permission granted")
        else:
            print("Permission denied")


LabelBase.register(name="MPoppins", fn_regular="Black.ttf")
LabelBase.register(name="BPoppins", fn_regular="Italic.ttf")
Slope().run()
