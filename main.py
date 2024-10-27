from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.button = Button(text="Click Me!")
        self.button.bind(on_press=self.on_button_click)
        layout.add_widget(self.button)
        return layout

    def on_button_click(self, instance):
        instance.text = "I Love You!"

if __name__ == "__main__":
    MyApp().run()
