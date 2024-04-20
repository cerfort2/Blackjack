from PIL import Image

# Load the image
img = Image.open('dickerson.png')

# Define the new size you want
new_width = 77
new_height = 111

# Resize the image

img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Save the resized image
img_resized.save('dickersonresized.png')
