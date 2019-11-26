from PIL import Image

im= Image.open('encrypted.png')
pix=im.load()
print(im.size)
print(pix[0,0])
a=[]
for i in range(im.size[1]):
    a.append(chr(pix[0,i][3]))
    
print("".join(a))
