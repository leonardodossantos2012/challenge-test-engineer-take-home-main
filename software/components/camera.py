import numpy as np
from PIL import Image
import random

class CameraMock:
    def capture(self, with_defect=False, low_lighting=False):
        """Generates an image with random noise and possibly a defect."""
        if low_lighting:
            noise_level = 35
            defect_intensity = 80
        else:
            noise_level = 10
            defect_intensity = 255
        
        image_data = (np.abs(np.random.randn(100,100))*noise_level)

        if with_defect:
            x, y = random.randint(10, 90), random.randint(10, 90)
            image_data[x-5:x+5, y-5:y+5] += defect_intensity
        image = Image.fromarray(image_data)
        return image
