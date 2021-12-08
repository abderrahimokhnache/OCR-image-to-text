from tkinter import *
from pytesseract import image_to_string
from PIL import Image 
from tkinter import filedialog


root = Tk()
root.title("ITT/S- Image to Text")

def extraxt(e = None , lang = 'eng'):

	result_as_a_text.delete(0.0,END)
	txt = image_to_string(img , lang = lang)
	result_as_a_text.insert(INSERT , txt)

def set_image(e = None):

	global img
	img = Image.open(filedialog.askopenfilename())
	try:
		show_case['image'] = img
		show_case.image = img
		show_case['text'] = ""
	except:
		pass
	extraxt()

show_case = Button(root , command = set_image , text = 'Open an Image ...')
show_case.pack()

result_as_a_text = Text(root)
result_as_a_text.pack()

root.mainloop()
