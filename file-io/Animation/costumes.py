# Import necessary libraries
import sys

#Install Module 'pip install pillow'
from PIL import Image 

# Initialize a list to store images
images = []

# Iterate through command line arguments (excluding the script name)
for arg in sys.argv[1:]:
    # Open each image and append it to the list
    image = Image.open(arg)
    images.append(image)

# Save the animated gif
images[0].save(
    "costumes.gif",  # Specify the output file name
    save_all=True,   # Save all frames
    append_images=images[1:],  # Append the rest of the images
    duration=200,    # Set duration between frames (in milliseconds)
    loop=0           # Set loop count (0 means infinite loop)
)
