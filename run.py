import os
import time
from datetime import datetime
from picamera import PiCamera

camera = PiCamera()

FRAMES = 60
TIMEBETWEEN = 10

frameCount = 0
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(3)
    camera.capture("image%s.jpg"%(imageNumber))
    frameCount += 1
    time.sleep(TIMEBETWEEN)
