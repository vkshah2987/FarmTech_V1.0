from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.core.window import Window

#Window.size = (300, 500)


"""screen_helper = '''

#sm = ScreenManager()

ScreenManager:
    HomeScreen:
    DataScreen:
    ControlScreen:
    GraphScreen:
    
    
<ControlScreen>:
    name: 'control'
    MDLabel:
        text: 'Welcome to control screen'
        halign: 'center'
        
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Control"
            elevation: 10
            left_action_items: [['arrow-down', lambda x: app.change_screen('home', 'down')]]
        Widget:


    
<HomeScreen>:
    name: 'home'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Home"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
        Widget:
        
        MDLabel:
            text: 'Welcome to FarmTech App. A Perfect Solution for Farmers.'
            halign: 'center'
            
        Image:
            source: 'farm.jpg'
            size: self.texture_size
        
        MDBottomAppBar:
            MDToolbar:
                mode: 'end'
                icon: 'power'
                type: 'bottom'
                on_action_button:
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'control'
                    
        
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
                    
            Image:
                source: 'farm.jpg'
                        
            MDLabel:
                text: 'FarmTech'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: 'A Farmer Friend'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                        
            BoxLayout:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint:(.1, None)
                    Button:
                        text: 'Home'
                        on_press:
                            root.manager.current = 'home'
                            #nav_drawer.set_state('close')
                    Button:
                        text:'Data'
                        on_press:
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'data'
                            nav_drawer.set_state('close')
                    Button:
                        text:'Graph'
                        on_press:
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'graph'
                            nav_drawer.set_state('close')
                            
            ScrollView:
                            
<DataScreen>:
    name: 'data'
    MDLabel:
        text: 'Welcome to Data Screen'
        halign: 'center'
        
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Data"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
        Widget:
        
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
                    
            Image:
                source: 'farm.jpg'
                        
            MDLabel:
                text: 'FarmTech'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: 'A Farmer Friend'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                        
            BoxLayout:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint:(.1, None)
                    Button:
                        text: 'Home'
                        on_press: 
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'home'
                            nav_drawer.set_state('close')
                    Button:
                        text:'Data'
                        on_press:
                            #root.manager.transition.direction = 'right'
                            root.manager.current = 'data'
                            #nav_drawer.set_state('close')
                    Button:
                        text:'Graph'
                        on_press:
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'graph'
                            nav_drawer.set_state('close')
                            
            ScrollView:
        
<GraphScreen>:
    name: 'graph'
    MDLabel:
        text: 'Welcome to graph screen'
        halign: 'center'
        
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Graph"
            elevation: 10
            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
        Widget:
        
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
                    
            Image:
                source: 'farm.jpg'
                        
            MDLabel:
                text: 'FarmTech'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: 'A Farmer Friend'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                        
            BoxLayout:
                BoxLayout:
                    orientation: 'vertical'
                    size_hint:(.1, None)
                    Button:
                        text: 'Home'
                        on_press: 
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'home'
                            nav_drawer.set_state('close')
                    Button:
                        text:'Data'
                        on_press: 
                            root.manager.transition.direction = 'left'
                            root.manager.current = 'data'
                            nav_drawer.set_state('close')
                    Button:
                        text:'Graph'
                        on_press: 
                            #root.manager.transition.direction = 'right'
                            root.manager.current = 'graph'
                            #nav_drawer.set_state('close')
                            
            ScrollView:

'''"""

class ControlScreen(Screen):
    pass


class HomeScreen(Screen):
    #wimg = Image(source='farm.jpg')
    pass


class DataScreen(Screen):
    pass


class GraphScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(DataScreen(name='data'))
sm.add_widget(GraphScreen(name='graph'))
sm.add_widget(ControlScreen(name='control'))


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.title = 'FarmTech'
        #self.theme_cls.theme_style = 'Dark'
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(DataScreen(name='data'))
        self.sm.add_widget(GraphScreen(name='graph'))
        self.sm.add_widget(ControlScreen(name='control'))
        screen = Builder.load_file("GUI.kv")
        return screen

    def change_screen(self, scr, dir):
        self.root.transition.direction = dir
        self.root.current = scr


#MyApp().run()
runTouchApp(MyApp().run())