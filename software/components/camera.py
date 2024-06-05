import numpy as np
from PIL import Image
import random

class CameraMock:
    def capture(self, with_defect=False, low_lighting=False):
        """Generates an image with random noise and possibly a defect."""
        # Create random noise background
        if low_lighting:
            noise_level = 35  # Low light yeilds higher noise
            defect_intensity = 80  # Lower intensity defect in low lighting
        else:
            noise_level = 10  # Better lighting yeilds lower noise
            defect_intensity = 255  # Clear defect visibility in normal lighting
        
        # Generate an image with random noise
        image_data = (np.abs(np.random.randn(100,100))*noise_level)

        # Possibly introduce a defect
        if with_defect:
            x, y = random.randint(10, 90), random.randint(10, 90)
            image_data[x-5:x+5, y-5:y+5] += defect_intensity  # Add defect on top of noise

        # Ensure values stay within valid pixel range
        image_data = np.clip(image_data, 0, 255).astype(np.uint8)
        image = Image.fromarray(image_data)
        return image
