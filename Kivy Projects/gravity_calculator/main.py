from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class GravityApp(App):
    def build(self):
        return GravityLayout()


class GravityLayout(BoxLayout):
    # all of my functions will be here
    def calculate(self):
        try:
            f = 6.67e-11 * (int(self.m1.text) * int(self.m2.text)) / int(self.r.text) ** 2
            self.newtons.text = 'F= {:.2e}'.format(f)
        except ZeroDivisionError or ValueError:
            self.newtons.text = 'That does not work'


if __name__ == '__main__':
    app = GravityApp()
    app.run()
