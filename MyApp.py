import logging
import kivymd
import PIL
import webbrowser
import random
from kivy.lang.builder import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem
from kivymd.app import MDApp

from urls import *



# main manager for our screens. 
class ScrManager (ScreenManager):
	pass



# screens. 

class HomeScreen (Screen):
	pass

class IntroScreen (Screen):
	pass

class Hbox(MDBoxLayout):
	pass

class Vbox(MDBoxLayout):
	pass

class UpperTools(MDToolbar):
	pass

class ListView(MDList):
	pass


class ListItemI(OneLineAvatarListItem):
	pass


class MainApp (MDApp):
	
	def build(self):
		frame = ScrManager()
		return frame
MainApp().run()

