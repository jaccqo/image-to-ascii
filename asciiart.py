import sys
from PIL import Image
from termcolor import colored
# pass the image as command line argument
import colorama
colorama.init()

print(colored(r""""

        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    \
   /        .-----.        \
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              | |
             _| |_
            /\( )/\
           /  ` '  \  
          | |     | |
          '-'     '-'
          | |     | |  
          | |     | |
          | |-----| |
       .`/  |     | |/`.
       |    |     |    |
       '._.'| .-. |'._.'
             \ | /        
             | | |
             | | |
             | | |
            /| | |\
          .'_| | |_`.
          `. | | | .'
       .    /  |  \    .
      /o`.-'  / \  `-.`o\
     /o  o\ .'   `. /o  o\   with args usage: python asciiart.py -yourimage.png                                 
     `.___.'       `.___.'          
                            

""",'green'))

try:
    image_path = sys.argv[1].strip('-')
except:
    image_path=input('enter image path:')


class AsciiArt:
    def __init__(self,img_path):
        self.path=image_path
        self.img = Image.open(self.path)

    def image(self):
        # resize the image
        width, height = self.img.size
        aspect_ratio = height/width
        new_width = 120
        new_height = aspect_ratio * new_width * 0.55
        img = self.img.resize((new_width, int(new_height)))
        # new size of image
        # print(img.size)

        # convert image to greyscale format
        img = img.convert('L')

        pixels = img.getdata()

        # replace each pixel with a character from array
        chars = ["B","S","#","&","@","$","%","*","!",":","."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        # split string of chars into multiple strings of length equal to new width and create a list
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)

        # write to a text file.

        file="ascii_image.txt"
        with open(file, "w") as f:
         f.write(ascii_image)

         print(colored(f"saved art image to file as {file}","yellow"))


if __name__=="__main__":
    AsciiArt(image_path).image()
