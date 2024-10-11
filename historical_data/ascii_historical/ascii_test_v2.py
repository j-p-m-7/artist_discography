from PIL import Image
import pywhatkit as kit

# Path to your image
image_path = "image.png"

# Convert the image to ASCII and save it to a text file
kit.image_to_ascii_art(image_path, "ascii_output")
