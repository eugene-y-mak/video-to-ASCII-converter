import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
import ffmpeg
import os

#  initializes mapping of pixel brightness to predetermined ASCII characters.
#  returns a map represented by a 1D array of length 255, where each possible pixel value can index into it.
def init_mapping():
    ascii_map = np.empty(256, dtype=str)  # 256 cuz there are 256 possible pixel vals, dummy
    upper = np.array([31, 56, 81, 106, 131, 156, 181, 206, 231, 256])
    lower = np.array([0, 31, 56, 81, 106, 131, 156, 181, 206, 231])
    # asciis = np.asarray(list('@%#*+=-:. ')) USE IF WHITE
    asciis = np.asarray(list(' .:-=+*#%@'))
    num_of_asciis = asciis.size
    if upper.size != lower.size or num_of_asciis != upper.size:
        print("You have mismatched number of ASCII characters.")
    for i in range(num_of_asciis):
        ascii_map[lower[i]:upper[i]] = asciis[i]
    return ascii_map


def img_to_ascii(img, ascii_map, text_width):
    ascii_img = ascii_map[img[::int(text_width), ::int(text_width)]]
    rows, cols = ascii_img.shape
    arr_of_strings = np.empty(rows, dtype=object)  # dtype potentially inefficient
    for i in range(rows):
        arr_of_strings[i] = str(''.join(ascii_img[i]))
    return arr_of_strings


def draw_text(strings_arr, row, col, typeface, font_size, img_num):
    # create blank white background
    img = np.zeros([row, col])
   #  img.fill(230) DO IF WANT WHITE, COMMENT IF BLACK
    rows = strings_arr.size
    img_p = Image.fromarray(img)
    draw = ImageDraw.Draw(img_p)
    padding = 1.69  # i have NO idea why this value looks good, but it does. Will test more.
    for i in range(rows):
        draw.text((0, 0 + (i * (font_size / padding))), strings_arr[i], font=typeface, fill=255) # fill=0
    name = "C:/Users/Eugene M/PycharmProjects/video-to-ASCII/temp/img" + str(img_num) + ".jpg"
    img_p = img_p.convert('RGB')  # convert to COLOR
    # img_p.save(name, 'JPEG')
    return np.array(img_p)


if __name__ == '__main__':

    # initialize and import: image, text size, font, ASCII mapping, image dimensions
    window_name = 'image'
    text_size = 15 # ideally keep this relatively high or else itll take its sweet time rendering and it wont look like ascii art anyway.
    monospace = ImageFont.truetype("cour.ttf", text_size)
    text_width = monospace.getsize('#')[0]
    ascii = init_mapping()



    # video processing
    vid = cv2.VideoCapture('snake.mp4')
    video_container = []
    if not vid.isOpened():
        print("Error opening video stream or file")
    # skip_frames = 1
    # mod = skip_frames + 1
    image_counter = 1
    while vid.isOpened():
        ret, frame = vid.read()
       # if skip_frames != 0:
       #     skip_frames += 1
        #    skip_frames = skip_frames % mod
        #    continue
       # skip_frames += 1
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            row, col = frame.shape
            strings = img_to_ascii(frame, ascii, text_width)
            background = draw_text(strings, row, col, monospace, text_size, image_counter)
            image_counter += 1
            video_container.append(background)
            print(len(video_container))
        else:
            break


 #   os.system("ffmpeg -framerate 24 -start_number 1  -i C:/Users/Eugene M/PycharmProjects/video-to-ASCII/temp/image%d.jpg output.mp4")

    fheight, fwidth, channels = video_container[0].shape
    #fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('outpy.avi', fourcc, 30.0, (fwidth, fheight))
    for frame in video_container:
        out.write(frame)
    out.release()

   # for frame in video_container:
   #     cv2.imshow('video', frame)
   #     if cv2.waitKey(100) & 0xFF == ord('q'):
    #        break
    vid.release()
    cv2.destroyAllWindows()

    # manual single image processing
    # path = 'BIG.jpg'
    # image = cv2.imread(path, 0)  # 0 means read as grayscale
    # row, col = image.shape
    # show final image
    # cv2.imshow(window_name, background)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



