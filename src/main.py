from PIL import Image , ImageEnhance , ImageFont , ImageDraw
import random
import os

numfile = open("num.txt","r+")
num = int(numfile.read())
maxnum = 10

def DeepFry(image):
    size = width , height = image.size
    sharp = ImageEnhance.Sharpness (image.convert('RGB'))
    image = sharp.enhance(5.0)
    colour = ImageEnhance.Color (image)
    image = colour.enhance(5.0)
    return image

def AddText(image):
    width, height = image.size
    font =ImageFont.truetype("impact.ttf",(int(width/4)))
    wordlist = open("wordlist.txt").read().splitlines()
    rndword = random.choice(wordlist)

    for char in rndword:
        num=+1

    if num > 7:
        font =ImageFont.truetype("impact.ttf",(int(width/4)))
    if num <7:
        font =ImageFont.truetype("impact.ttf",(int(width/8)))
    
    tw,th=font.getsize(rndword)
    draw = ImageDraw.Draw(image)
    uw =int((width-tw)/2)
    uh =int((height-th)/2)
    draw.text((uw,10),rndword,font=font)
    return image


maxnum = int(input("How Many?: "))

for i in range(maxnum):
    randomfile = random.choice(os.listdir("C:\\Users\\Home\\Desktop\\fried\\imagelibrary"))
    randomimg = randomfile
    num +=1
    AddText(DeepFry(Image.open(os.path.join("C:\\Users\\Home\\Desktop\\fried\\imagelibrary" , randomimg)))).save("finalimage"+str(num)+".png")

numfile.seek(0)
numfile.write(str(num))
numfile.truncate()
numfile.close()
