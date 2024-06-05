from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import uuid
from components.camera import CameraMock
from components.ai import AISystemMock
from components.database import Database

app = Flask(__name__)
CORS(app)

# Initialize the camera and AI system
camera = CameraMock()
ai_system = AISystemMock()
database = Database("test_results.db")

@app.route('/capture_image', methods=['POST'])
def capture_image():
    data = request.json
    with_defect = data.get('with_defect', False)
    low_lighting = data.get('low_lighting', False)
    
    image = camera.capture(with_defect, low_lighting)
    image_array = np.array(image)
    image_uuid = uuid.uuid4()

    # Convert image data to list for JSON serialization
    raw_image = image_array.tolist()

    return jsonify(raw_image=raw_image, image_UUID=str(image_uuid))

@app.route('/predict_defect', methods=['POST'])
def predict_defect():
    data = request.json
    raw_image = data['raw_image']
    image = Image.fromarray(np.array(raw_image, dtype=np.uint8))
    
    defect_present = ai_system.predict(image).item()
    prediction_uuid = uuid.uuid4()

    return jsonify(has_defect=defect_present, prediction_UUID=str(prediction_uuid))

@app.route('/shutdown', methods=['POST'])
def shutdown():
    database.close()

    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
