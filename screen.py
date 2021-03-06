from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition, FadeTransition, RiseInTransition
from kivy.lang.builder import Builder
from kivymd.app import MDApp

def load_sub1 ():
	'''function to load screens having English songs'''
	Builder.load_file("screens/sub1/eng_a.kv")
	Builder.load_file("screens/sub1/eng_b.kv")
	Builder.load_file("screens/sub1/eng_c.kv")
	Builder.load_file("screens/sub1/eng_d.kv")
	Builder.load_file("screens/sub1/eng_e.kv")
	Builder.load_file("screens/sub1/eng_f.kv")
	Builder.load_file("screens/sub1/eng_g.kv")
	Builder.load_file("screens/sub1/eng_h.kv")
	Builder.load_file("screens/sub1/eng_i.kv")
	Builder.load_file("screens/sub1/eng_j.kv")
	Builder.load_file("screens/sub1/eng_k.kv")
	Builder.load_file("screens/sub1/eng_l.kv")
	Builder.load_file("screens/sub1/eng_m.kv")
	Builder.load_file("screens/sub1/eng_n.kv")
	Builder.load_file("screens/sub1/eng_o.kv")
	Builder.load_file("screens/sub1/eng_p.kv")
	Builder.load_file("screens/sub1/eng_q.kv")
	Builder.load_file("screens/sub1/eng_r.kv")
	Builder.load_file("screens/sub1/eng_s.kv")
	Builder.load_file("screens/sub1/eng_t.kv")
	Builder.load_file("screens/sub1/eng_u.kv")
	
	

def load_sub2 ():
	'''function to load screens having  songs'''
	pass

def load_sub3 ():
	'''function to load screens having songs'''
	pass

def load_sub4 ():
	'''function to load screens having songs'''
	pass



def load ():
	Builder.load_file("main.kv")
	Builder.load_file("layout.kv")
	Builder.load_file("screens/menu.kv")
	Builder.load_file("screens/eng.kv")
	Builder.load_file("screens/hin.kv")
	Builder.load_file("screens/oth.kv")
	load_sub1()
	load_sub2()
	load_sub3()
	load_sub4()
	


	
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
		
#### SCREENS FOR ENGLISH SONGS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________	
class subscreenone (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
class subscreentwo (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen4 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen5 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen6 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen7 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen8 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen9 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen10 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen11 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen12 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen13 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen14 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen15 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen16 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen17 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen18 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen19 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")

class subscreen20 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")

class subscreen21 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
#### SCREENS FOR HINDI SONGS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________	
class subscreen1_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
class subscreen2_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3 (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen4_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen5_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen6_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen7_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen8_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen9_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen10_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen11_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen12_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen13_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen14_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen15_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen16_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen17_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen18_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen19_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")

class subscreen20_h (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	

#### SCREENS FOR OTHER SONGS
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________	

class subscreen1_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
class subscreen2_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen3_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen4_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen5_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen6_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen7_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen8_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen9_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen10_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen11_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen12_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen13_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen14_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen15_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen16_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
	
class subscreen17_o (Screen):
	"""
	
	"""
	a = "abc"
	def ch_sc (self):
		switch("profile1")
		

def switch (scr):
	MDApp.get_running_app().root.current = scr
	MDApp.get_running_app().root.transition = NoTransition()
	MDApp.get_running_app().root.transition.direction="right"
	#MDApp.get_running_app().root.transition.duration=0.1