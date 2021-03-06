from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition

class subscreenone (Screen):
	pass

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

def switch (screen_name):
	MDApp.get_running_app().root.current = screen_name
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1

