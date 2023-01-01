# my.py

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivymd.uix.button import MDIconButton
from kivymd.app import MDApp
# MDIconButton
Window.size = (580, 960)

class MyWidget(Widget):
    search_menu = None
    def build(self):
        MapView(lat=20.5937,lon=78.9629,zoom=25)

class MyApp(MDApp):
    def build(self):
        return MyWidget()

# if __name__ == '__main__':
MyApp().run()