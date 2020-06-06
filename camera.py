import picamera

# Setup te camera. Will close when done
print("About to take picture")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("fotos/image.jpg")
   
print("Picture taken")