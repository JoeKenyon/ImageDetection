from ImageDetection import ImageDetect

coords = ImageDetect.DetectImage(True,0.8,"chars.JPG")

ImageDetect.ShowLocations(True,coords)
