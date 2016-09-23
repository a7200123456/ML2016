import sys
from PIL import Image

im = Image.open( sys.argv[1] )
im_r = im.rotate( 180, Image.BILINEAR )
im_r.save( "ans2.png", "PNG" )