# video-to-ASCII-converter
 
Accepts a given video file and converts it into a black and white ASCII art-ified version. Iterates through each frame of the video and does image processing on each, converting the processed frames into a finished video in .avi format. Supports easy changes to the size of the text and color of text versus color of background. Can process video of any length, though smaller text size and longer length will naturally take longer to process. 

Example with the Opening of Neon Genesis Evangelion (size 10 font, 480p, heavily compressed):

https://www.youtube.com/watch?v=At92sumkqAk

This is a pretty difficult test case for ASCII art in general since the frames are quite detailed and the video very often flashes completely different frames. Program works best on simple looking videos with lots of "chunks" of one color, such as:

https://youtu.be/M0dGH7wxZY4 (from https://www.youtube.com/watch?v=zsa3I5lpUmA)

Can also do white background: https://www.youtube.com/watch?v=SIENz98ZFY4

Another example: https://www.youtube.com/watch?v=TohrT-6d_IA (from https://www.youtube.com/watch?v=Bxc_55ur-J4)

# Dependencies

-OpenCV

-Numpy

-PIL (for drawing monospaced fonts)

-FFMPEG (optional for adding sound)

# How it works

Uses the OpenCV library extensively. Uses the VideoCapture functions to accept and process the frames of a video. 

Utilizes a numpy array (can also use hashmaps for other languages) that maps 10 specific ASCII characters to a certain brightness range, with a defined range for each value. Mapping uses brightness value (of which there will be one, because image is processed in black and white) as a key to find the corresponding ASCII character.

Once this mapping is initialized, use efficient Numpy matrix operations to convert the given image (being a frame of the video) into an ASCII art version of that image. Sample only every X pixels where X is the size of the text, since converting each pixel into a character enlarges the original image. Output an array of strings where each string is a row of the image. 

Use Pillow to draw these strings and create the image. Optionally, this image can be saved externally onto the drive, maybe to be converted to a video later using FFMPEG. Otherwise, the image is stored temporarily only in program memory and does not take explicit drive space. Critically, convert the image into RGB for video conversion later, or else strange behavior occurs...

Finally, iterate through a list of processed images and use OpenCV's VideoWriter to output a video (using DIVX codec, although MJPG likely works) and save video to workspace.

# Future 

-There is no sound in the outputted video, and this is not a bug but rather an OpenCV limitation since it's not really meant for video processing. One way is to output each frame onto the drive and save through FFMPEG, but this takes significant drive space. Instead, one way could be to take the outputted video through VideoWriter and use FFMPEG to extract the original video's audio and combine it with the video output, which I have verified works manually through command line.

-Outputs black and white videos only, but color could be more visually appealing. However, based on how "faithful" you want your ASCII art to be, adding color may stray away from its original appeal. Additionally, color may be algorithmically simplistic since brightness can now be done through the color itself rather than the specific character, so it will depend less on the "shape" and more on the color of the original image.

-Add GUI to easily adjust resolution (aka text size) of outputted video

-Add way to go from youtube link to video download

-Real time conversion through webcam?

-Web front end of application

# Bugs

Processed image exhibits "scanlines," which may be due to how pixels are sampled from the original image to create the ASCII art version.

# Notes

-OpenCV and Numpy are just wrappers for C/C++ methods, so no point in doing this in C++. 

-Aesthetically, black background and white text is more appealing
