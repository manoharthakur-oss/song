from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivymd.app import MDApp
class subscreenone(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

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

"""ENGLISH SONGS"""
'_______________________________'
class subscreentwo(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreenthree(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")
class subscreenfour(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreenfive(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreensix(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreenseven(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreeneight(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreennine(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")

class subscreenten(Screen):
	"""
	
	"""
	def ch_sc (self):
		switch("profile1")



def switch (screen_name):
	MDApp.get_running_app().root.current = screen_name
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1

