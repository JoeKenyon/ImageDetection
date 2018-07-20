from PIL import ImageGrab
import numpy as np
import cv2

class ImageDetect:
    def __init__(self):
        self.detected = False

    def DetectImage(OnScreen, Threshold, filename_Input, *args):
        ImageDetect.detected = False
        try:
            if OnScreen:
                img_rgb = np.array(ImageGrab.grab())
                img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
            else:
                img_rgb = cv2.imread(*args,1) # image to be searched
                
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) #convert to effcient format
            
            template = cv2.imread(filename_Input,0) # image to be found
            w, h = template.shape[::-1] #width and height of template

            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= Threshold) #find points whithin threshhold

            inst = []
            
            for pt in zip(*loc[::-1]):
                ImageDetect.detected = True
                inst.append(((pt[0], pt[1]),(pt[0] + w, pt[1] + h))) #returns two sets of coords, matches contained within
            print(len(inst)," instances found.")
            return inst
        except Exception as e:
            print(e)

    
    def ShowLocations(onscreen, coords, *args):
        try:
            if onscreen == True:
                img_rgb = np.array(ImageGrab.grab())
                img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
            else:
                img_rgb = cv2.imread(*args,1)

            for i in coords:
                cv2.rectangle(img_rgb,i[0],i[1],(0,0,255), 2) #draw around the occurences
                
            cv2.imshow('found',img_rgb) #display
        except Exception as e:
            print(e)
    


