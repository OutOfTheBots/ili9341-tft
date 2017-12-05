# ili9341-tft
Micro-Python libiary for the ili9341

Currently this driver is ver basic and will only upload 320x240 images that have been preprocessed into 16bit 5R6G5B BMP format.
The 24bit_to_16bit.py is a very basic hack I wrote to convert 320x240 24bit 8R8G8B BMP files into the needed format.
I created the orginial 320x240 BMP files with photoshop and saved them as BMP file then clicked on advanced and selected 24bit 8R8G8B.

The driver will setup the ili9341 chip to be able to bus data directly from the 16bit BMP file directly to memory wihtout futher processing
The driver will setup the screen in 320x240 mode not the usually 240x320 mode generally used by ili9341
The driver will also setup the screen in RGB mode where mpost drivers will use BGR mode
The posistionon x=0 and y=0 is has been setup to be at the bottom left of the screen as this is the format used by BMP files.

This project so far has been developed on the ESP8266 using Micro-Python
There is much futher development yet to come and plan to make a high level GUI user interface for the ESP32
