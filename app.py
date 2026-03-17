from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the model (make sure mnist_model.h5 exists in the same folder)
model_path = os.path.join(os.path.dirname(__file__), "mnist_model.h5")
model = load_model(model_path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    img_file = request.files["file"]
    img_path = os.path.join("static", "uploaded.png")
    img_file.save(img_path)

    # Preprocess the image
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    img_array = image.img_to_array(img)
    img_array = 255 - img_array  # invert colors for MNIST
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction, axis=1)[0]

    return jsonify({"prediction": int(predicted_digit)})

if __name__ == "__main__":
    app.run(debug=True)