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

face = Image("https://raw.githubusercontent.com/GrygorchukPI/Python_Guide/master/happy-face.png", [500, 500], [1000, 1000], [100, 100])
   
def draw(canvas):
    const_num = 20
    for t in range(const_num):
        x = 250 + 200 * math.cos(2 * 3.1415 /const_num * t)
        y = 250 + 200 * math.sin(2 * 3.1415 /const_num * t)
        face.draw(canvas, [x, y])
   

   
frame = simplegui.create_frame("Program", 500, 500)
frame.set_draw_handler(draw)

frame.set_canvas_background("White")
frame.start()
