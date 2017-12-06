from MP_ili9341 import ili9341
import machine
import time

machine.freq(160000000)

screen = ili9341()

screen.load_image("image3.bmp")

text1 = screen.put_text(10, 198, 3, 'Out of',(0, 80, 200), (50, 0, 0))
text2 = screen.put_text(10, 155, 3, 'the',(0, 80, 200), (50, 0, 0)) 
text3 = screen.put_text(214, 10, 3, 'BOTS',(0, 80, 200), (50, 0, 0))

for y in range (15, 160, 20):  
  time.sleep_ms(400)
  screen.restore_image(text3, "image3.bmp")
  text3 = screen.put_text(214, y, 3, 'BOTS',(0, 80, 200), (50, 0, 0))

for x in range (20, 140, 20):  
  time.sleep_ms(400)
  screen.restore_image(text2, "image3.bmp")
  text2 = screen.put_text(x, 155, 3, 'the',(0, 80, 200), (50, 0, 0)) 

time.sleep_ms(400)
screen.restore_image(text3, "image3.bmp")
text3 = screen.put_text(150, 100, 5, 'BOTS',(0, 80, 200), (50, 0, 0))
time.sleep_ms(400)
screen.restore_image(text3, "image3.bmp")
text3 = screen.put_text(86, 80, 7, 'BOTS',(0, 80, 200), (50, 0, 0))
