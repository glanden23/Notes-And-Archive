import os
from playsound import playsound
import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

text = open("read.txt").read().replace(" ","%20").replace("\n","")
urllib.request.urlretrieve(f"http://tts.cyzon.us/tts?text={text}", "output.wav")
while True:
    playsound(os.path.dirname(__file__)+"\\"+'output.wav',True)