import string
from PIL import Image

# Extended set of ASCII characters for more detail
ASCII_CHARS = [" ", ".", "`", "'", ":", "~", "-", "_", "+", "=", "?", "i", "!", "l", "I", ">", "<", "t", "f", "x", "r", "v", "Y", "L", "C", "J", "u", "n", "z", "X", "Z", "O", "0", "Q", "m", "w", "8", "%", "@", "#", "$"]
#ASCII_CHARS = [    '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd',    'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c',    'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}',    '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', ' ', 'l', 'I', ';', ':',    ',', '"', '^', "'", '`']

# Function to resize the image based on a new width
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 is for adjusting the aspect ratio for ASCII characters
    return image.resize((new_width, new_height))

# Convert image to grayscale
def grayscale_image(image):
    return image.convert("L")

# Map each pixel to an ASCII character
def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    # Safely map pixel value (0-255) to ASCII chars
    for pixel in pixels:
        ascii_str += ASCII_CHARS[min(pixel // (256 // len(ASCII_CHARS)), len(ASCII_CHARS) - 1)]
    return ascii_str

# Convert image to ASCII art
def image_to_ascii(image_path, new_width=100):
    # Open image
    image = Image.open(image_path)
    
    # Resize, grayscale, and convert to ASCII
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixel_to_ascii(image)
    
    # Format the ASCII string to fit the image's width
    img_width = image.width
    ascii_art = "\n".join([ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)])
    return ascii_art


def print_ascii(image_path="image.png"):
    # Convert image to ASCII art and print it
    ascii_art = image_to_ascii(image_path, 100)
    print(ascii_art)

    # Optionally, save the ASCII art to a text file
    with open("ascii_output.txt", "w") as f:
        f.write(ascii_art)



if __name__ == "__main__":
    #Path to your image
    image_path = "image.png"

    # Convert image to ASCII art and print it
    ascii_art = image_to_ascii(image_path, 100)
    print(ascii_art)

    # Optionally, save the ASCII art to a text file
    with open("ascii_output.txt", "w") as f:
        f.write(ascii_art)














# from PIL import Image

# # Define the ASCII characters you want to use
# # ASCII_CHARS = [" ", "-", "/", "\\", "|", "_", "+", "=", "~"]
# ASCII_CHARS = [" ", ".", "`", "'", ":", "~", "-", "_", "+", "=", "?", "i", "!", "l", "I", ">", "<", "t", "f", "x", "r", "v", "Y", "L", "C", "J", "u", "n", "z", "X", "Z", "O", "0", "Q", "m", "w", "8", "%", "@", "#", "$"]


# # Function to resize the image based on a new width
# def resize_image(image, new_width=100):
#     width, height = image.size
#     aspect_ratio = height / float(width)
#     new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 is for adjusting the aspect ratio for ASCII characters
#     return image.resize((new_width, new_height))

# # Convert image to grayscale
# def grayscale_image(image):
#     return image.convert("L")

# # Map each pixel to an ASCII character
# def pixel_to_ascii(image):
#     pixels = image.getdata()
#     ascii_str = ""
#     for pixel in pixels:
#         ascii_str += ASCII_CHARS[pixel // 32]  # Scale grayscale (0-255) to our list of 9 ASCII characters
#     return ascii_str

# # Convert image to ASCII art
# def image_to_ascii(image_path, new_width=100):
#     # Open image
#     image = Image.open(image_path)
    
#     # Resize, grayscale, and convert to ASCII
#     image = resize_image(image, new_width)
#     image = grayscale_image(image)
#     ascii_str = pixel_to_ascii(image)
    
#     # Format the ASCII string to fit the image's width
#     img_width = image.width
#     ascii_art = "\n".join([ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)])
#     return ascii_art

# # Path to your image
# image_path = "image.png"

# # Convert image to ASCII art and print it
# ascii_art = image_to_ascii(image_path, 100)
# print(ascii_art)

# # Optionally, save the ASCII art to a text file
# with open("ascii_output.txt", "w") as f:
#     f.write(ascii_art)
