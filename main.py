from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
Window.size = (370, 700)

class MainApp(MDApp):
    # Build est le point d'entrer de l'application
    def build(self):
        
        # Lier l'élément graphique à Python
        return Builder.load_file("main.kv")
app=MainApp()
app.run()