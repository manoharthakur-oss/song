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
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, SwapTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import MDList , OneLineAvatarListItem
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout
from kivymd.app import MDApp
from urls import*
sc=ScreenManager()
class MenuScreen(Screen):		
	def set_sc(self):
	    MDApp.get_running_app().root.current = "profile"
	    MDApp.get_running_app().root.transition.direction="up"
	def set_screen(self):
		MDApp.get_running_app().root.current = "profile1"
		MDApp.get_running_app().root.transition = NoTransition(duration=0.001)
class profilescreentwo(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"   
class profilescreenthree(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenfour(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenfive(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"  	
class profilescreensix(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreenseven(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreeneight(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class profilescreennine(Screen):
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class subscreenone(Screen):  	
    def ch_sc(self):
        MDApp.get_running_app().root.current = "menu"
        MDApp.get_running_app().root.transition.direction="down"
class MainApp (MDApp):
	def build(self):
		frame=sc
		return frame
MainApp().run()