import logging
import kivymd
import PIL
import webbrowser
import random
import webbrowser
from kivy.lang.builder import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivy.properties import ObjectProperty
from kivymd.uix.navigationdrawer import NavigationLayout , MDNavigationDrawer 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem , ThreeLineAvatarListItem , TwoLineAvatarListItem
from kivymd.app import MDApp
"=================================================================================================================="
from urls import *
"=================================================================================================================="
"=================================================================================================================="





# MAIN MANAGER FOR OUR SCREENS
"=================================================================================================================="
class ScrManager (ScreenManager):
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

class Navigation (NavigationLayout):
	pass





# LISTVIEW
"=================================================================================================================="
class ListView(MDList):
	pass


class ListItemI(TwoLineAvatarListItem):
	pass







# MAIN APP CLASS
"=================================================================================================================="
class MainApp (MDApp):
	def opening (self):
		urls.mdlist()
		pass
		
	def build(self):
		self.data = {"menu":"menu","arrow-left":"back"}
		self.theme_cls.primary_palette = "Teal" 
		frame = Navigation()
		return frame


MainApp().run()