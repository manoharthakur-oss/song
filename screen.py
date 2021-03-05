from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivy.lang.builder import Builder
from kivymd.app import MDApp

def load_sub1 ():
	'''function to load screens having English songs'''
	Builder.load_file("screens/sub1/eng_a.kv")
	
def load_sub2 ():
	'''function to load screens having  songs'''
	pass

def load_sub3 ():
	'''function to load screens having songs'''
	pass

def load_sub4 ():
	'''function to load screens having songs'''
	pass

def load_sub5 ():
	pass

def load_sub6 ():
	pass

def load_sub7 ():
	pass

def load_sub8 ():
	pass

def load ():
	Builder.load_file("main.kv")
	Builder.load_file("layout.kv")
	Builder.load_file("screens/menu.kv")
	Builder.load_file("screens/eng.kv")
	Builder.load_file("screens/screen2.kv")
	Builder.load_file("screens/screen3.kv")
	Builder.load_file("screens/screen4.kv")
	Builder.load_file("screens/screen5.kv")
	Builder.load_file("screens/screen6.kv")
	Builder.load_file("screens/screen7.kv")
	Builder.load_file("screens/screen8.kv")
	load_sub1()
	load_sub2()
	load_sub3()
	load_sub4()
	load_sub5()
	load_sub6()
	load_sub7()
	load_sub7()
	
	


	
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
		switch("menu")
	

class profilescreentwo(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenthree(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenfour(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenfive(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreensix(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreenseven(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")

class profilescreeneight(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("menu")
		
	
class subscreenone (Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")
	

def switch (scr):
	MDApp.get_running_app().root.current = scr
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1




