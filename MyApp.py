import logging
import kivymd
import PIL
import webbrowser
import random
from kivy.lang.builder import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.scrollview  import ScrollView
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem , TwoLineAvatarListItem, ThreeLineAvatarListItem, OneLineIconListItem, TwoLineIconListItem ,ThreeLineIconListItem
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp


from urls import*

def change_it():
	MDApp.get_running_app().root.current = "menu"
	#MDApp.get_running_app().root.transition = FadeTransition()
	MDApp.get_running_app().root.transition.direction="up"
	MDApp.get_running_app().root.transition.duration=10

# SCREENS
"================================================================================================"
	

class MenuScreen(Screen):
	"""
	HOME SCREEN
	"""		
	def set_sc(self):
		MDApp.get_running_app().root.current = "profile"
		MDApp.get_running_app().root.transition.direction="up"
	def set_screen(self):
		MDApp.get_running_app().root.current = "profile1"
		MDApp.get_running_app().root.transition = NoTransition(duration=0.1)

class profilescreentwo(Screen):
	def ch_sc(self):
		change_it()


class profilescreenthree(Screen):
	""" 
	INTRODUCTION SCREEN
	"""
	def ch_sc(self):
		change_it()

		
class profilescreenfour(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()

		
class profilescreenfive(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()
		
class profilescreensix(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()
		
class profilescreenseven(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()
		
class profilescreeneight(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()
		
class profilescreennine(Screen):
	""" 
	
	"""
	def ch_sc(self):
		change_it()
		
class subscreenone(Screen):
	""" 
	
	"""	
	def ch_sc(self):
		change_it()

class Navigation (MDNavigationDrawer):
	pass

# LAYOUTS (BOXLAYOUTS)
"================================================================================================"

class Hbox (MDBoxLayout):
	pass

class Vbox (MDBoxLayout):
	pass


# LIST ITEMS
"================================================================================================"



class MainApp (MDApp):
	
	data= {"menu":"oll"}
	
	def build(self):
		l=['Red', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Orange', 'DeepOrange',]
		self.theme_cls.primary_palette = random.choice(l)		
		sc=ScreenManager()
		sc.add_widget(MenuScreen(name="menu"))
		sc.add_widget(profilescreentwo(name="profile2"))
		sc.add_widget(profilescreenthree(name="profile3"))				
		return sc

if __name__=="__main__":
	MainApp().run()