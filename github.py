import requests
import time
from pystyleclean import *


url = input("Enter your github viewer stats link: ")

def spam():
    while(True):
        print(f'[>] Link Spammed.')
        requests.get(url)
        time.sleep(0.5)
spam()
