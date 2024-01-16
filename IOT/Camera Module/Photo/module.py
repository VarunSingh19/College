# To Click Photo
import picamera
with picamera.PiCamera() as camera:
    camera.capture('image.jpg')