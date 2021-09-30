
import random
from gl import Raytracer, V3
from obj import Object
from figures import *

windoWidth = 1920*1
windowHeight = 1080*1
scale= 1
viewportWidth= windoWidth*scale
viewportHeight= windowHeight *scale
viewportX=0
viewportY=0


rtx = Raytracer(width,height)

rtx.glRender()
rtx.glFinish('output.bmp')