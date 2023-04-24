# Mouse_moving_bot.py
import pyautogui as pag
import time
import random

while True:
    x=random.randint(600,700)
    y=random.randint(200,600)
    pag.moveTo(x,y,1)
    time.sleep(2)
    
    



