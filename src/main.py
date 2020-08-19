from PIL import Image , ImageEnhance , ImageFont , ImageDraw
import random
import os

num = 0
maxnum = 10

def DeepFry(image):
    size = image.size
    sharp = ImageEnhance.Sharpness (image.convert('RGB'))
    image = sharp.enhance(10.0)
    colour = ImageEnhance.Color (image)
    image = colour.enhance(5.0)
    
    return image

def AddText(image):
    width = image.size[0]
    height = image.size[1]
    
    font = ImageFont.truetype("impact.ttf",(int(width/4)))
    wordlist = open("wordlist.txt").read().splitlines()
    rndword = random.choice(wordlist)

    for char in rndword:
        num = 1

    if num > 7:
        font = ImageFont.truetype("impact.ttf", (int(width/4)))
    if num < 7:
        font = ImageFont.truetype("impact.ttf", (int(width/8)))
    
    tw = font.getsize(rndword)[0]
    th = font.getsize(rndword)[1]
    draw = ImageDraw.Draw(image)
    
    uw = int((width-tw)/2)
    uh = int((height-th)/2)
    
    draw.text((uw, 10), rndword, font=font)
    
    return image

try:
    maxnum = int(input("How Many?: "))
except:
    pass

for i in range(maxnum):
    randomfile = random.choice(os.listdir("imageLibrary"))
    randomimg = randomfile
    num += 1
    AddText(DeepFry(Image.open(os.path.join("imageLibrary", randomimg)))).save("finalimage"+str(num)+".png")
