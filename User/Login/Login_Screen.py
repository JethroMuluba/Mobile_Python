from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):
    name = ""
    password = ""
    def tape_username(self,keyboard_name):
        self.name = keyboard_name
        print(self.name)

    def tape_password(self,keyboard_password):
        self.password = keyboard_password
        print(self.password)


    def connexion(self):
        print("Form Send", self.name, self.password)
        self.manager.current = "student"

    def on_enter(self,*args):
        pass

