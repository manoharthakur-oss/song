import logging
import kivy[md
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

	
from urls import *
from screen import *
from lyout import *



# MAIN APP CLASS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class MainApp (MDApp):
	load()
	
	def textit (self,path):
		"""
		this function is to load and display text
		from different files
		"""
		file = open(path)
		txt = file.read()
		return txt
	
	def build(self):
		scrman = Manager()
		return Manager()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
if __name__=="__main__":
	MainApp().run()