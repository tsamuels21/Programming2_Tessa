from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.clearcolor = (1, 1, 1, 1)
Window.size = (400, 600)


class DemoApp(App):
    def build(self):
        return DemoLayout()


class DemoLayout(BoxLayout):
    pass


if __name__ == "__main__":
    demo = DemoApp()
    demo.run()
