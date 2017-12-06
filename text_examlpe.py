from MP_ili9341 import ili9341
import machine
import time

machine.freq(160000000)

screen = ili9341()

for pos in range (180,0, -10):
    for size in range (1,5):
      screen.put_text(pos, pos, size, 'BOTS')

      time.sleep_ms(500//(size*2))