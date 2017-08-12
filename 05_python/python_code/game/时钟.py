from __future__ import division
from appuifw import *
import math, time, e32

app.body = c = Canvas()
radius = 72
bigsize = radius * .775
litsize = radius * .57
secsize = radius * .97
mx, my = 88, 72
N = 9

def draw(hh, mm, ss, colors=(0, 1, 2)):
    bigd = (90 - (mm*60 + ss) / 10) % 360
    litd = (90 - (hh*3600 + mm*60 + ss) / 120) % 360
    secd=(90-ss*6)%360
    bigr = bigd * math.pi / 180
    litr = litd * math.pi / 180
    secr = secd * math.pi / 180
    drawbg(bigd, litd, colors)
    c.line([mx, my,
             mx + secsize*math.cos(secr),
             my - secsize*math.sin(secr)],
             0, width = radius/50)
    c.line([mx, my,
             mx + bigsize*math.cos(bigr),
             my - bigsize*math.sin(bigr)],
             0, width = radius/37)
    c.line([mx, my,
             mx + litsize*math.cos(litr),
             my - litsize*math.sin(litr)],
             0, width = radius/30)
    # Draw the text
    c.text([5, 144-1], u"%02d:%02d:%02d" % (hh, mm, ss),0xffffff)
def drawbg(bigd, litd, colors=(0, 1, 2)):
    c.clear(0)
    table = []
    for angle, colorindex in [(bigd - 180/N, 0),
                              (litd - 180/N, 1),
                              (  90 - 180/N, 2)]:
        angle %= 360
        for i in range(N):
            color = 255
            if colorindex in colors:
                color = (N-1-i)*color//(N-1)
            table.append((angle, color, colorindex))
            angle += 360/N
            if angle >= 360:
                angle -= 360
                table.append((0, color, colorindex))
    table.sort()
    table.append((360, None))
    fill = [0, 0, 0]
    for i in range(len(table)-1):
        angle, color, colorindex = table[i]
        fill[colorindex] = color
        if angle <=359:
            c.pieslice([mx-radius,my-radius,mx+radius,my+radius],
                       angle * math.pi/180, 0,
    # start, end
                      fill=tuple(fill), width=0)
    c.line([mx+1, my, mx+radius-1, my], tuple(fill))
  # complete at 360 deg
running = 1
def quit():
    global running
    running = 0
app.exit_key_handler= quit
while running:
    t = time.time() + time.clock()%1
    hh, mm, ss = time.localtime(t)[3:6]
    draw(hh, mm, ss, (0,1,2))
    e32.ao_sleep(1-t%1)
