from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_palette = "Green"

        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, Усачишка! Как тебе кактусовая заставка?",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()