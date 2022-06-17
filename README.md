# ASCII-Art-Generator
## Description
Converting Videos(mp4)/Images(png/jpg) into ASCII encoded strings that looks like images. For videos, frames can considered as images.In this project I have converted the videos into ascify video.

## How to run the project
Firstly download the ascii.py file along with the videos from this repository to your file.

Then open the code the in your IDE and add the video name int the variable "video_name" that you want get ascified and then save the code(the video should be in the file). 

Finally run the code. A pop up ascified video will appear. 
To close the video you need to press "f" in your keyboard.

## Working of the code

Images are stored in computers as 2D rectangular arrays of Pixels.Each pixel contains a value from 0(black) to 255(white). These numbers represent different shades of gray.
The project is done in pyhton.
PILLOW and Open-CV(cv2) libraries hase been used in this project.

Font used is DejaVuSansMono.

Firstly cv2(open-cv),ImageDraw,ImageFont,Image(PIL) and numpy has been imported. Then the characters that need to been shown in the image has been stored in the variable, which further has been added to the list . These characters got assigned some values based on there index.

As I have used videos in this project , cv2.VideoCapture(video_name) is used to read the video frame by frame.  Each image(frame) is resized based on the scale factor and char_height , char_width .A new image is formed using the new width and height values and initializing it with  black color.

After resizing we go on each and every (i,j)th index of the image(frame) and convert the r,g,b values to a single grayscale value(0-255).
This grayscale value is used to call the character from the list based on the value.
Then cv2.imshow() is used to display the frames.
This process will continue till each and every image(frame) is converted to ascii art.


## My Learnings from the Project
From the project i got to know about the pixels and the value associated with them of the images and also got to know that the characters can be mapped to different values of rgb.

## Description of the additional task(ASCIIFY VIDEOS)
Videos are the collection of images(frames) , so in this project I have converted ascii art frame by frame . To read the video cv2.VideoCapture(video_name) is used.

## Video Demo



https://user-images.githubusercontent.com/94849855/174354251-47569d76-bb19-4610-acea-44a924dd126f.mp4


##  Resources/References Used
1. ACM Discussions
2. https://yuukidach.github.io/2020/02/19/practice/image-to-asciiart/
3. https://medium.com/analytics-vidhya/the-ultimate-handbook-for-opencv-pillow-72b7eff77cd7
4. and some youtube videos to understand the working of r,g,b values and characters


