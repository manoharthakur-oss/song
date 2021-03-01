import logging
import kivymd
import PIL
import webbrowser as wb
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

def load ():
	Builder.load_file("main.kv")
	Builder.load_file("screens/menu.kv")
	Builder.load_file("screens/screen1.kv")
	Builder.load_file("screens/screen2.kv")
	Builder.load_file("screens/screen3.kv")
	Builder.load_file("screens/screen4.kv")
	Builder.load_file("screens/screen5.kv")
	Builder.load_file("screens/screen6.kv")
	Builder.load_file("screens/screen7.kv")
	Builder.load_file("screens/screen8.kv")
	
class Manager(ScreenManager):
	pass

# SCREEN(S)
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

class MenuScreen(Screen):
	"""
	
	"""
	
	pass

class profilescreenone(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()
	

class profilescreentwo(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreenthree(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreenfour(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreenfive(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreensix(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreenseven(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

class profilescreeneight(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch()

def switch ():
	MDApp.get_running_app().root.current = "menu"
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1





# MAIN APP CLASS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class MainApp (MDApp):
	load()
	
	def build(self):
		scrman = Manager()
		return Manager()

if __name__=="__main__":
	MainApp().run()