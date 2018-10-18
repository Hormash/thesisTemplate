from glob import glob
import os

pngfiles = glob("*.png")
for imagen in pngfiles:
	os.system("convert {} {}eps".format(imagen, imagen[:-3]))

jpgfiles = glob("*.jpg")
for imagen in jpgfiles:
	out = u.replace('jpg','eps')
    print "Converting %s to %s" % (u, out)
    img=Image.read(u)
    img.thumbnails((800,800)) # Changing the size
    img.save(out)


epsfiles = glob("*.eps")
for imagen in epsfiles:
	os.system("mv {} ../images/".format(imagen))


	out = u.replace('jpg','eps')
    print "Converting %s to %s" % (u, out)
    img=Image.read(u)
    img.thumbnails((800,800)) # Changing the size
    img.save(out)
