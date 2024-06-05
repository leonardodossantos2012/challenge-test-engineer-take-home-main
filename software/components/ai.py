import numpy as np

class AISystemMock:
    def __init__(self, threshold=145):
        self.threshold = threshold
    def predict(self, image):
        image_array = np.array(image)
        defect_present = np.any(image_array >= self.threshold)
        return defect_present
