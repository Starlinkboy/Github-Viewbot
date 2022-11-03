import requests
import time
from pystyleclean import *


url = input(Colorate.Horizontal(Colors.purple_to_blue, "Enter your github viewer stats link: "))

def spam():
    while(True):
        print(Colorate.Horizontal(Colors.purple_to_blue, '[>] Link Spammed.'))
        requests.get(url)
        time.sleep(0.5)
spam()
