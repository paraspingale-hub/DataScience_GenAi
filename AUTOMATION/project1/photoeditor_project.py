from PIL import Image , ImageFilter 
import os

rawimppath = "rawimp"
proimppath = "processimp" 

for filename in os.listdir(rawimppath):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = Image.open(os.path.join(rawimppath, filename))
        img = img.filter(ImageFilter.SHARPEN)
        img.save(os.path.join(proimppath, filename))    

  