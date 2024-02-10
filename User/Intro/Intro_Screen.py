from kivy.clock import Clock
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.transition import MDFadeSlideTransition, MDSlideTransition


class IntroScreen(MDScreen):

    def on_enter(self, *args):
        Clock.schedule_once(self.go_to_next_screen, 4.0)

    def go_to_next_screen(self,_):
        self.manager.transition = SlideTransition()


        self.manager.current = 'login'


        pass
