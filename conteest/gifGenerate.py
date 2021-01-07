from PIL import Image
import sys,os
img = Image.open("[PATH of source_pic.png]")
width, height = img.size
left, right, upper, lower = 0, 0, 0, 0
right = left + width/8
lower = upper + height/9
i = 0

while i <= 71:
    cropped = img.crop((left, upper, right, lower))  # (left, upper, right, lower)
    left += width/8
    right = left + width/8
    if i%8 == 7 :
        upper += height/9
        lower = upper + height/9
        left = 0
        right = left + width/8
    if i<= 9:
        mystr = "[PATH of target]pic_0"+str(i)+".png"
    else:
        mystr = "[PATH of target]pic_"+str(i)+".png"
    cropped.save(mystr)
    print("saved: "+str(i)+".png")
    i+=1

os.system("pause")

def convertToGIF(picSetPath, picNum, time): #invalid path var for now
    imgs = []
    pic_dir = "[PATH of target]"
    t = time/picNum
    for i in range(72):
        pic_name = '{}\\{}.png'.format(pic_dir,71-i)
        temp = Image.open(pic_name)
        imgs.append(temp)
    save_name = '{}\\apple_lock.gif'.format(pic_dir)
    imgs[0].save(save_name, save_all=True, append_images=imgs, duration=t)
    return save_name

convertToGIF('',72,eval(input("time: ")))

