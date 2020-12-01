from PIL import Image
import cv2
import numpy as np
import glob
import pytesseract as ocr

escale = 5

def image_to_string(img):

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	im_pil = Image.fromarray(img)

	image = Image.open(im_pil)
	width,height= image.size
	#image.resize((width*escale,height*escale))
	phrase = ocr.image_to_string(image)

	print(phrase)

	if('S' in phrase or 'T' in phrase or 'P' in phrase):
		print('Stop')
	elif('6' in phrase):
		print('60')
	elif('40' in phrase):
		print('40')
	elif('3' in phrase):
		print('30')
	else:
		print('Não reconhecido')