import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


# Initialize the camera
camera = PiCamera()

# Set camera resolution (optional)
camera.resolution = (224, 224)


camera.framerate = 24  # Adjust based on your needs
rawCapture = PiRGBArray(camera, size=(224, 224))

# Rotate the camera if needed (optional)
# camera.rotation = 180

# Start the preview (optional)
# camera.start_preview()

# Give the camera time to adjust to lighting conditions
sleep(2)

# Capture an image
rawCapture = PiRGBArray(camera)


# Stop the preview (optional)
# camera.stop_preview()

# Close the camera
camera.close()
