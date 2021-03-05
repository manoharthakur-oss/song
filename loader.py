from kivy.lang.builder import Builder


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

load()
