# video-to-ASCII-converter
 
Accepts a given video file and converts it into a black and white ASCII art-ified version. Iterates through each frame of the video and does image processing on each, converting the processed frames into a finished video in .avi format. Supports easy changes to the size of the text and color of text versus color of background. Can process video of any length, though smaller text size and longer length will naturally take longer to process. 

Example with the Opening of Neon Genesis Evangelion (size 10 font, 480p, heavily compressed):

https://www.youtube.com/watch?v=At92sumkqAk

(This is a pretty difficult test case for ASCII art in general since the frames are quite detailed and the video very often flashes completely different frames. Program works best on simple looking videos with lots of "chunks" of one color)

# Dependencies

-OpenCV

-Numpy

-PIL (for drawing monospaced fonts)

-FFMPEG (optional for adding sound)

# How it works

Uses the OpenCV library extensively. Uses the VideoCapture functions to accept and process the frames of a video. 

Utilizes a hashmap that maps 10 specific ASCII characters to a certain brightness range, with a defined range for each value. Hashmap uses brightness value (of which there will be one, because image is processed in black and white) as a key to find the corresponding ASCII character mapping.

Once this hashmap is initialized, use efficient Numpy matrix operations to convert the given image (being a frame of the video) into an ASCII art version of that image. Sample only every X pixels where X is the size of the text, since converting each pixel into a character enlarges the original image. Output an array of strings where each string is a row of the image. 

Use Pillow to draw these strings and create the image. Optionally, this image can be saved externally onto the drive, maybe to be converted to a video later using FFMPEG. Otherwise, the image is stored temporarily only in program memory and does not take explicit drive space. Critically, convert the image into RGB for video conversion later, or else strange behavior occurs...

Finally, iterate through a list of processed images and use OpenCV's VideoWriter to output a video (using DIVX codec, although MJPG likely works) and save video to workspace.

# Future 

-There is no sound in the outputted video, and this is not a bug but rather an OpenCV limitation since it's not really meant for video processing. One way is to output each frame onto the drive and save through FFMPEG, but this takes significant drive space. Instead, one way could be to take the outputted video through VideoWriter and use FFMPEG to extract the original video's audio and combine it with the video output, which I have verified works manually through command line.

-Outputs black and white videos only, but color could be more visually appealing. However, based on how "faithful" you want your ASCII art to be, adding color may stray away from its original appeal. Additionally, color may be algorithmically simplistic since brightness can now be done through the color itself rather than the specific character, so it will depend less on the "shape" and more on the color of the original image.

-Add GUI to easily adjust resolution (aka text size) of outputted video

-Auto detect whether to use white on black or black on white

-Initial version of project was done in C++, but I could not get any monospaced fonts since HarfBuzz would not install no matter what I tried. Could be interesting to finish the C++ version to see if there are any significant speed ups in processing time. 


# Bugs

Processed image exhibits "scanlines," which may be due to how pixels are sampled from the original image to create the ASCII art version.

