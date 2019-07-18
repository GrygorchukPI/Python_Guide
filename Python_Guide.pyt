# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

import math
import random
import simplegui
import urllib2
import codeskulptor


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



message = "YO"


def tick():
    global message
    global sec
    global pic_coords
    sec += 1
    pic_coords = [x + 1 for x in pic_coords]
    message = "tick " + str(sec)
    
sec = 0
pic_coords = [0, 0]
timer = simplegui.create_timer(1000, tick)

def click(pos):
    global message
    message = "click " + str(pos)

def keydown_handler(key):
    global message
    message = "keydown " + str(key)

def keyup_handler(key):
    global message
    message = "keyup " + str(key)

face = Image("https://raw.githubusercontent.com/GrygorchukPI/Python_Guide/master/happy-face.png", [500, 500], [1000, 1000], [100, 100])
    
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")
    face.draw(canvas, pic_coords)
    

    
frame = simplegui.create_frame("Program", 900, 600)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
frame.set_mouseclick_handler(click)

frame.set_canvas_background("White")
frame.start()
timer.start() # use timer.stop() to stop
