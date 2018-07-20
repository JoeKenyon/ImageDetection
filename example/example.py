from PyImage import PyDetector

coords = PyDetector.DetectImage(True,0.8,"chars.JPG")

PyDetector.ShowLocations(True,coords)
