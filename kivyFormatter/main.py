from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class FormatterApp(App):
    def build(self):
        return FormatterLayout()


class FormatterLayout(BoxLayout):
    # all of my functions will be here
    def text_on(self, value):
        if value:
            self.label.color = 1, 1, 1, 1
        else:
            self.label.color = 0, 0, 0, 1

    def change_text(self, text):
        self.label.text = text

    def font_change(self, font):
        if font == 'Dalila Light':
            self.label.font_name = 'Dalila Light.ttf'
            self.spinner.font_name = 'Dalila Light.ttf'
        if font == 'Dael Neu':
            self.label.font_name = 'Dael Neu.ttf'
            self.spinner.font_name = 'Dael Neu.ttf'
        if font == 'DavysRibbons':
            self.label.font_name = 'DavysRibbons.ttf'
            self.spinner.font_name = 'DavysRibbons.ttf'
        if font == 'Xerox Malfunction':
            self.label.font_name = 'Xerox Malfunction (BRK).ttf'
            self.spinner.font_name = 'Xerox Malfunction (BRK).ttf'


    def change_window(self, r, g, b):
        Window.clearcolor = (r, g, b, 1)


if __name__ == '__main__':
    app = FormatterApp()
    app.run()
