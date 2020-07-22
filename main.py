from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
Window.size=(300,500)

screen_helpers = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    
<MenuScreen>:
    name:"menu"
    MDRectangleFlatButton:
        text:"Profile"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:root.manager.current= "profile"
    MDRectangleFlatButton:
        text:"Upload"
        pos_hint:{"center_x":0.5,"center_y":0.4}
        on_press:root.manager.current= "upload"
    
<ProfileScreen>:
    name:"profile"
    MDLabel:
        text:"Welcome User"
        halign:"center"
    MDRectangleFlatButton:
        text:"Go back"
        pos_hint:{"center_x":0.2,"center_y":0.8}
        on_press:root.manager.current="menu"
        
        
<UploadScreen>:
    name:"upload"
    MDLabel:
        text:"upload"
        halign:"center"
    MDRectangleFlatButton:
        text:"Go back"
        pos_hint:{"center_x":0.2,"center_y":0.8}
        on_press:root.manager.current="menu"
            
            
        
            

"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(ProfileScreen(name="profile"))
sm.add_widget(UploadScreen(name="upload"))

class MyApp(MDApp):

    def build(self):
        KV = Builder.load_string(screen_helpers)

        return KV


MyApp().run()
