from flask import Flask, render_template, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
import os

# Initialize Flask app
app = Flask(__name__)

# Define the classes for your model
classes = ["Severe", "Proliferate_DR", "No_DR", "Moderate", "Mild"]

# Load the trained model
# Load the trained model
model_path = "best_model.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize the model structure and load the state_dict
from torchvision import models
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(classes))  # Adjust final layer for your classes
model.load_state_dict(torch.load(model_path, map_location=device))
model = model.to(device)
model.eval()


# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        # Save the file temporarily
        filepath = os.path.join("uploads", file.filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(filepath)

        # Load and preprocess the image
        image = Image.open(filepath).convert('RGB')
        image = transform(image).unsqueeze(0).to(device)

        # Make a prediction
        with torch.no_grad():
            outputs = model(image)
            _, predicted = torch.max(outputs, 1)
            predicted_class = classes[predicted.item()]

        # Remove the temporary file
        os.remove(filepath)

        return jsonify({'prediction': predicted_class})

if __name__ == '__main__':
    # Ensuring the app runs on the correct host and port provided by Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
