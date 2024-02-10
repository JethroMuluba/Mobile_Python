from faker import Faker
from kivy.clock import Clock
from kivymd.uix.list import MDListItem, MDListItemLeadingIcon, MDListItemHeadlineText
from kivymd.uix.screen import MDScreen


class StudentsListScreen(MDScreen):

    def get_students(self):
        faker = Faker()

        # First way to get list in faker
        # students = []
        # for i in range(50):
            # name = faker.name()
            # students.append(name)

        # Second way to get list in faker
        students = [faker.name() for i in range(50)]
        return students

    def on_ready_page(self, *args):
        self.ids.label_id.text = 'Students (0)'
        students = self.get_students()
        for data in students:
            ligne = MDListItem(
                MDListItemLeadingIcon(icon="account"),
                MDListItemHeadlineText(text=data)
            )
            self.ids.my_data_list.add_widget(ligne)


    def on_enter(self, *args):
        Clock.schedule_once(self.on_ready_page, 0.5)


