import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.audio import SoundLoader
from kivy.uix.actionbar import ActionBar
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from json import load



FIlE = './MySource.json'
COLORS = [(0.94, 0.68, 0.24, 1), (0.65, 0.62, 0.60, 1), (0.36, 0.33, 0.31, 1), (0.94, 0.68, 0.24, 1), (0.96, 0.80, 0.64, 1), (0.94, 0.49, 0.25, 1), (0.93, 0.36, 0.24, 1)]
COLORS_LEN = 7
with open(FIlE) as f:
    source_dic = load(f)


class ScreenTwo(Screen):
    def test_on_enter(self, vidname):    
        self.vid = VideoPlayer(source=vidname, state='play',
                                options={'allow_stretch':False,
                                            'eos': 'stop'})
        
        self.add_widget(self.vid)

    def on_touch_down(self, touch):
        if touch.is_triple_tap:
            self.vid.state = 'pause'
            self.vid._video = None
        else:
            for child in self.children[:]:
                child.dispatch('on_touch_down', touch)

    def onBackBtn(self):
        self.vid.state = 'stop'
        self.vid._video = None
        self.remove_widget(self.vid)
        self.manager.current = self.manager.list_of_prev_screens.pop()


class ScreenOne(Screen):
    def onNextScreen(self, btn, vidname):
        self.manager.list_of_prev_screens.append(btn.parent.name)
        self.manager.current = 'screen2'
        self.manager.screen_two.test_on_enter(vidname)
      

class MyButton(Button):
    
    def __init__(self, **kwargs):
        self.url = kwargs.get('url', None)    
        del kwargs['url']
        super().__init__(**kwargs)

    def on_press(self):
        #print(self.parent.name)
        self.get_root_window().children[:][0].screen_one.onNextScreen(self, self.url)

   
class MyLayout(GridLayout):
  
    def __init__(self, **kwargs):
        i = 0
        self.bind(minimum_height=self.setter('height'))
        super().__init__(**kwargs)
        for k, v in source_dic.items():
            
            btn = MyButton(text=k, url=v, size_hint_y=None, height=60, font_name='STSONG.TTF')
            btn.background_color = COLORS[i % COLORS_LEN]
            self.add_widget(btn)
            i += 1

    def search_result(self, instance, value):
        if value is not None:
            i = 0
            my_layout_children = self.children[:]
            self.clear_widgets()
            for sk, sv in source_dic.items():

                if value.lower() in sk.lower():
                    btn = MyButton(text=sk, url=sv, size_hint_y=None, height=60, font_name='STSONG.TTF')
                    btn.background_color = COLORS[i % COLORS_LEN]
                    self.add_widget(btn)
                    i += 1
            
            if i == 0:
                for child in my_layout_children:
                    self.add_widget(child)
        else:
            return True
    
   

class Manager(ScreenManager):
    transition = NoTransition()
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
   
    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.list_of_prev_screens = []


class PlayerApp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    PlayerApp().run()