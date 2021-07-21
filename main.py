from kivymd.app import MDApp
from kivy.lang import Builder


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Cactus Coffee'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Coffees'
            icon: 'coffee-outline'

            MDLabel:
                text: 'Here will be beautiful pictures of coffee'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Sales'
            icon: 'alarm-light-outline'

            MDLabel:
                text: 'Do not miss the opportunity'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Contacts'
            icon: 'phone-classic'

            MDLabel:
                text: 'Call us 88002000600'
                halign: 'center'
'''
        )


Test().run()