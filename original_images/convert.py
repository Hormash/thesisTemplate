from glob import glob
from PIL import Image
import os

pngfiles = glob("*.png")
for imagen in pngfiles:
	img = Image.open(imagen)
	out = imagen.replace('png','eps')
	print ('Converting {} to {}'.format(imagen, out))
	img.save(out)

jpgfiles = glob("*.jpg")
for imagen in jpgfiles:
	img = Image.open(imagen)
	out = imagen.replace('jpg','eps')
	print ('Converting {} to {}'.format(imagen, out))
	img.save(out)


epsfiles = glob("*.eps")
for imagen in epsfiles:
	os.system("mv {} ../images/".format(imagen))


