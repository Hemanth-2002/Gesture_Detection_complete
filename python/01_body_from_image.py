# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
import glob

# To convert gif to mp4
# clip = mp.VideoFileClip("vid.gif")
# clip.write_videofile("myvideo.mp4")
# print('../examples/input_mp4/myvideo.mp4')

# Video to frames
if len(os.listdir("../examples/input_img/")) == 0:
    vidcap = cv2.VideoCapture('../examples/input_mp4/myvideo.mp4')
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("../examples/input_img/"+"frame%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        count += 1

# openpose code
if len(os.listdir("../examples/output_img/")) == 0:
    try:
        # Import Openpose (Windows/Ubuntu/OSX)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            # Change these variables to point to the correct folder (Release/x64 etc.)
            sys.path.append(dir_path + '/../bin/python/openpose/Release');
            os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../x64/Release;' +  dir_path + '/../bin;'
            import pyopenpose as op
        except ImportError as e:
            print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
            raise e

        # Flags
        for x in os.listdir("../examples/input_img"):
            if x.endswith(".jpg"):
                parser = argparse.ArgumentParser()
                parser.add_argument("--image_path", default="../examples/input_img/"+x, help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
                args = parser.parse_known_args()

                # Custom Params (refer to include/openpose/flags.hpp for more parameters)
                params = dict()
                params["model_folder"] = "../models/"

                # Add others in path?
                for i in range(0, len(args[1])):
                    curr_item = args[1][i]
                    if i != len(args[1])-1: next_item = args[1][i+1]
                    else: next_item = "1"
                    if "--" in curr_item and "--" in next_item:
                        key = curr_item.replace('-','')
                        if key not in params:  params[key] = "1"
                    elif "--" in curr_item and "--" not in next_item:
                        key = curr_item.replace('-','')
                        if key not in params: params[key] = next_item

                # Starting OpenPose
                opWrapper = op.WrapperPython()
                opWrapper.configure(params)
                opWrapper.start()

                # Process Image
                datum = op.Datum()
                imageToProcess = cv2.imread(args[0].image_path)
                datum.cvInputData = imageToProcess
                opWrapper.emplaceAndPop(op.VectorDatum([datum]))

                # save Image
                print(str(datum.poseKeypoints))
                cv2.imwrite('../examples/output_img/'+x, datum.cvOutputData)
                cv2.waitKey(0)
    except Exception as e:
        print(e)
        sys.exit(-1)


# frames to video
# img_array = []
# for filename in glob.glob('../examples/output_img/*.jpg'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
#
# out = cv2.VideoWriter('../examples/output_mp4/project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
#
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()