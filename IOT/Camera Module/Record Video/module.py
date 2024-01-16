# For Video

import picamera
import time
with picamera.PiCamera() as camera:
    camera.resolution = (1280 , 720)
    camera.start_preview()
    time.sleep(2)
    camera.start_recording('video.h264')
    time.sleep(10)
    camera.stop_recording()
    camera.stop_preview()