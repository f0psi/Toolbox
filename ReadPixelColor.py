from PIL import Image

#this was used in a ctf challenge, to get binary-data of an image (960x960, one block was 30x30)

im = Image.open('pic.png')
pix = im.load()

x = 15
y = 15
val = []

while x <= 960 and y <= 960 :
    try:
        print (x,y, pix[x,y])
        if pix[x,y] == (0, 0, 0):
            val.append(1)
        if pix[x,y] == (255, 255, 255):
            val.append(0)
    except:
        print('done!')
        print (*bin, sep='')
        sys.exit(1)

    x += 30 # 30 = one block; so x + 30 to get into the next box
    if x == 975: #if x = 945 we read the hole line; set x to start and y to next line
        x = 15
        y += 15
