# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import math
import random
import simplegui
import urllib2
import codeskulptor

Window_Width = 500
Window_Height = 500

class Image:
    def __init__(self, image_url, image_center, src_size, dest_size, dest_shift=[0,0], tile_skip=[0,0]):
        self.image = simplegui.load_image(image_url)
        self.image_center = image_center
        self.src_size = src_size
        self.dest_size = dest_size
        self.dest_shift = dest_shift
        self.tile_skip = tile_skip
        
    def draw(self, canvas, pos, tile=[0, 0], rot=0):
        canvas.draw_image(self.image, [self.image_center[0] + tile[0] * self.tile_skip[0], self.image_center[1] + tile[1] * self.tile_skip[1]], self.src_size, [pos[0] + self.dest_shift[0], pos[1] + self.dest_shift[1]], self.dest_size, rot)

x = 250
y = 100
g = 1 #9.8
t = 0
pic_coords = [x, y]
def tick():
     global pic_coords
     global x
     global y
     global g
     global t
     x = 250
     if y < 450:
        y = y + g*t/2
        t = t + 0.1
        
     pic_coords = [x, y]
    
timer = simplegui.create_timer(10, tick)

pic_width = 100
pic_height = 100
Img_Src = "https://raw.githubusercontent.com/GrygorchukPI/Python_Guide/master/happy-face.png"""
Original_Img_Width = 1000  #You need to know it before run the code
Original_Img_Height = 1000 #You need to know it before run the code
face = Image(Img_Src, [500, 500], [Original_Img_Width, Original_Img_Height], [pic_width, pic_height])

def draw(canvas):
    face.draw(canvas, pic_coords)
    
frame = simplegui.create_frame("Program", Window_Width, Window_Height)
frame.set_draw_handler(draw)

frame.set_canvas_background("White")
frame.start()
timer.start() # use timer.stop() to stop
