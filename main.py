from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
Window.size = (370, 700)

class WindowManager(ScreenManager):
    def initial_route(self):
        self.transition = NoTransition()
        self.current = "login"

class MainApp(MDApp):
    # Build est le point d'entrer de l'application
    def build(self):
        manager = WindowManager()
        manager.initial_route()
        return manager
        # Lier l'élément graphique à Python
        #return Builder.load_file("main.kv")
app=MainApp()
app.run()