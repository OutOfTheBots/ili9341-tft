from MP_ili9341 import ili9341
import time

#pins can be specified during creation of instance
# i.e screen = ili9341(self, cs=16, dc=4)
screen = ili9341()

#chunk size can be specified durinmg calling of method
# i.e screen.load_image(image_file, chunk_size=1024)
screen.load_image("image1.bmp")
time.sleep(3)
screen.load_image("image2.bmp")
time.sleep(3)
screen.load_image("image3.bmp")
time.sleep(3)
screen.load_image("image4.bmp")
