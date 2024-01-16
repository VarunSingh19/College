import picamera
import time
with picamera.PiCamera() as camera:
    camera.start_recording('video.h264')
    time.sleep(5)
    camera.stop_recording()