c = 1

for a in "bcdefghijklmnopqrstu":
	c=c+1
	
	str = """
<subscreen>
	name: 'sube_"""+a+"""'
	NavigationLayout:
		ScreenManager:
			Screen:
				BoxLayout:
					orientation: 'vertical'
					MDToolbar:
						title: 'Standing by you'
						left_action_items: [["arrow-left",lambda x:  root.ch_sc()]]
					BoxLayout:
						orientation: 'vertical'
						ScrollView:
							GridLayout:
								padding: 50
								spacing: 50
								cols:1
								height: self.minimum_height
								size_hint_y: None

								MDCard:
									pos_hint: {'center_x': .5, 'center_y': .5}				
									size_hint: None,None
									size: root.width-100,root.height/3
									SmartTile:
										box_color:0,0,0,0
										AsyncImage:
											pos_hint: {'center_x': .5, 'center_y': .5}
											size: 500,500
											source:"https://docs.google.com/drawings/d/e/2PACX-1vQ69SliAdrAkj2ydQ3c0Isdcy6TRs-dmLUDTizE02t87qnVOdIgMMZWJu8BpMh6ScR1U3toeV7Ziffq/pub?w=960&h=720"		   
								
								
								
								MDLabel:
									markup: True
									size_hint:1, None
									size: self.texture_size
									text:app.textit('txt_mat/txt_sub1/txt_sub1_a.txt')
								
								
								
								MDCard:
									pos_hint: {'center_x': .5, 'center_y': .5}				
									size_hint: None,None
									size: root.width-100,root.height/3
									SmartTile:
										box_color:0,0,0,0
										AsyncImage:
											pos_hint: {'center_x': .5, 'center_y': .5}
											size: 500,500
											source:"https://docs.google.com/drawings/d/e/2PACX-1vQ69SliAdrAkj2ydQ3c0Isdcy6TRs-dmLUDTizE02t87qnVOdIgMMZWJu8BpMh6ScR1U3toeV7Ziffq/pub?w=960&h=720"		   
								
								
"""
	file = open("screens/sub1/eng_"+a+".kv","a")
	file.write(str)
	file.close()