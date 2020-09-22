from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import runTouchApp, App
from kivy.properties import NumericProperty
from kivy.uix.label import Label
# Create the manager
class MyScreenManager(ScreenManager):
    num = NumericProperty(1)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print('touch manager!')
            print(self.ids['l1'].parent)
            self.num = (self.num + 1) % 3
            if self.num == 0:
                self.num = 3
            self.current = 's%d' % (self.num)

# Add few screens


# By default, the first screen added into the ScreenManager will be
# displayed. You can then change to another screen.

# Let's display the screen named 'Title 2'
# A transition will automatically be used.


class MyScreensApp(App):
    def build(self):
        return MyScreenManager()


MyScreensApp().run()