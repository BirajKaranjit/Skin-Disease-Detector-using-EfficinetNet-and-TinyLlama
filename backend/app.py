# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import base64
import io
from model import predict  # Import the predict function from model.py
from TextModel import TextModel

app = Flask(__name__)
CORS(app)


# model and toknizer file path
model_dir = 'models/text'
tokenizer_dir = 'models/tokenizer'

# instantiate text model class
TEXT_MODEL = TextModel(model_dir, tokenizer_dir)


# instantiate text model class
TEXT_MODEL = TextModel(model_dir, tokenizer_dir)


@app.route('/ping', methods=['GET'])
def ping():
   return jsonify({'message': 'pong'})


@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.json

    # Decode the image from base64
    img_data = base64.b64decode(data['image'])
    image = Image.open(io.BytesIO(img_data)).convert("RGB")

    # Extract additional textual information if needed
    text_info = data.get('text', '')
    print(text_info)  # Currently not used in prediction

    # Predict using the model
    disease_pred, confidence = predict(image)
    
    # generate recommendation
    recommendation = TEXT_MODEL.generate_text(disease_pred, text_info)
    print(recommendation)


    recommendation = TEXT_MODEL.generate_text(disease_pred, text_info)

    return jsonify({'predicted_class': disease_pred, 'confidence' : confidence, 'recommendation' : recommendation })


# @app.route('/testPrediction', methods=['GET'])
def test_prediction(probable_disease, description):
    data = request.json()

    output = TEXT_MODEL.generate_text(probable_disease, description)

    print(output)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)






