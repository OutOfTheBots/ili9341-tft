from MP_ili9341 import ili9341
import machine
import time


machine.freq(160000000)

screen = ili9341()

screen.load_image("image2.bmp")

tu = screen.put_text(100, 100, 6, 'BOTS')

time.sleep(2)
screen.restore_image(tu, "image2.bmp")

