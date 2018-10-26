from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
import preparation_field
from kivy.uix.widget import Widget


from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')	

class MainMenu(BoxLayout):
	pass

class GameTypeMenu(BoxLayout):
	pass

class MainMenuScreen(Screen):
	def __init__(self , **kwargs):
		super(MainMenuScreen , self).__init__(**kwargs)
		self.screen = Builder.load_file("menu.kv")
		self.add_widget(self.screen)

class GameSelectionScreen(Screen):
	def __init__(self , **kwargs):
		super(GameSelectionScreen , self).__init__(**kwargs)
		self.screen = Builder.load_file("gametype.kv")
		self.add_widget(self.screen)

class ToolsScreen(Screen):
	def __init__(self , **kwargs):
		super(ToolsScreen , self).__init__(**kwargs)
		self.screen = Builder.load_file("tools.kv")
		self.add_widget(self.screen)

class PraparationScreen(Screen):
	def __init__(self , **kwargs):
		super(PraparationScreen , self).__init__(**kwargs)
		self.screen = Builder.load_file("prepare.kv")
		self.add_widget(self.screen)

class GameScreen(Screen):
	def __init__(self , **kwargs):
		super(GameScreen , self).__init__(**kwargs)
		self.screen = Builder.load_file("game.kv")
		self.add_widget(self.screen)

class ScreenManagement(ScreenManager):
	pass



class MyApp(App):

	def build(self):
		self.manager = Builder.load_file("main.kv")
		return self.manager


if __name__ == "__main__":
	MyApp().run()