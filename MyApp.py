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
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.app import MDApp
"=================================================================================================================="
from urls import *
"=================================================================================================================="
"=================================================================================================================="





# MAIN MANAGER FOR OUR SCREENS ANF NAVIGATIONLAYOUT. 
"=================================================================================================================="
class ScrManager (ScreenManager):
	pass

class Navigator (NavigationLayout):
	pass





# SCREENS
"=================================================================================================================="
"=================================================================================================================="






# HOME SCREEN
"=================================================================================================================="
class HomeScreen (Screen):
	pass

class UpperTools(MDToolbar):
	pass






# INTRODUCTION SCREEN
"=================================================================================================================="
class IntroScreen (Screen):
	pass






# LAYOUTS
"=================================================================================================================="
class Hbox(MDBoxLayout):
	pass

class Vbox(MDBoxLayout):
	pass

class Scroll (ScrollView):
	pass





# LISTVIEW
"=================================================================================================================="
class ListView(MDList):
	pass


class ListItemI(OneLineAvatarListItem):
	pass






# MAIN APP CLASS
"=================================================================================================================="
class MainApp (MDApp):
	
	def build(self):
		frame = Builder.load_file("main.kv")
		return frame






MainApp().run()