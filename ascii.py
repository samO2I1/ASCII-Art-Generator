from PIL import ImageDraw,ImageFont,Image
import cv2
import numpy as np
import math



chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "#declaring characters based on brightness
video_name="p.mp4"
charlist=list(chars) #adding the char to the list

charlen=len(charlist)#length of the list
interval=charlen/256
scale_factor=0.09 #font aspect ratio


def get_char(i): #function to get char for a particular cell
    return charlist[math.floor(i*interval)]

frames=cv2.VideoCapture(video_name) #converting the video into frames

Font=ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20) #creating a font object
charwidth, charheight = Font.getsize("A") #character width and heigth w.r.t A
while True:#getting frames
    _,img=frames.read() #reading each and every frame
    img=Image.fromarray(img) #converting the image to pillow image(frame)

    width,height=img.size
    img=img.resize((int(scale_factor*width),int(scale_factor*height*(charwidth/charheight))),Image.NEAREST)#resizing the image according to the scale factor
    width,height=img.size #getting new heigth and width
    pixel=img.load()#getting pixels of the resized image
    outputImage=Image.new("RGB",(charwidth*width,charheight*height),color=(0,0,0))#intitializing the new image with black color
    dest=ImageDraw.Draw(outputImage)#drawing the final image

    for i in range(height):
        for j in range(width):
            r,g,b=pixel[j,i]#getting rgb values 
            h=int(0.299*r+0.587*g+0.114*b)#converting the r,g,b values to grayscale value
            pixel[j,i]=(h,h,h)#assigning grayscale value toh the pixel
            dest.text((j*charwidth,i*charheight),get_char(h),font=Font,fill=(r,g,b))#writing the char into the pixel

    open_cv_image=np.array(outputImage)#collecting all the images
    key=cv2.waitKey(1)
    if key == ord("f"):
        break
    cv2.imshow("ASCIIFY VIDEO",open_cv_image)
frames.release()
cv2.destroyAllWindows()