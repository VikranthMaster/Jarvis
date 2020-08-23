
import os
import random
path="C:/Users/shankar/Desktop/python/jarvis/songs/"
files=os.listdir(path)
d=random.choice(files)
os.startfile("C:/Users/shankar/Desktop/python/jarvis/songs/" + d)