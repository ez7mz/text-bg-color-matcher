import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Define the neural network architecture
class ColorPredictor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ColorPredictor, self).__init__()
        # Define the layers of the neural network
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()
        # Initialize a MinMaxScaler for normalizing input colors
        self.scaler = MinMaxScaler()

    def forward(self, x):
        # Define the forward pass of the neural network
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.sigmoid(out)
        return out

    # Function to predict text color given a background color
    def predict_text_color(self, model, color):
        # Normalize the input color using the same scaler used for training data
        normalized_color = self.scaler.transform([color])

        # Convert the normalized color to a PyTorch tensor
        input_tensor = torch.tensor(normalized_color, dtype=torch.float32)

        # Perform prediction
        model.eval()
        with torch.no_grad():
            output = model(input_tensor)
            # If the output is greater than 0.5, predict 'white', otherwise predict 'black'
            predicted_label = 'white' if output > 0.5 else 'black'

        return predicted_label

class ModelLoader:
    def __init__(self, model_path, dataset, input_size=3, hidden_size=16, output_size=1):
        print("Initializing model loader...")
        self.model_path = model_path
        self.dataset = dataset
        # Initialize the ColorPredictor model
        self.model = ColorPredictor(input_size, hidden_size, output_size)

    def load_model(self):
        print("Loading model...")
        # Load the model weights from the specified path
        self.model.load_state_dict(torch.load(self.model_path))
        # Fit the MinMaxScaler to the dataset
        self.fit_scaler()
        # Set the model to evaluation mode
        self.model.eval()

    def fit_scaler(self):
        print("Fitting scaler...")
        # Load the dataset from a CSV file
        self.dataset = pd.read_csv(self.dataset)
        # Initialize a new MinMaxScaler
        self.model.scaler = MinMaxScaler()
        # Fit the MinMaxScaler to the RGB values of the dataset
        self.model.scaler.fit_transform(self.dataset[['R', 'G', 'B']])

    def get_model(self):
        # Return the loaded model
        return self.model

    def predict_text_color(self, color):
        print("Predicting text color...")
        # Use the model to predict the text color for the given background color
        return self.model.predict_text_color(self.model, color)

# if __name__ == "__main__":
#     # Initialize the ModelLoader
#     model_loader = ModelLoader("./model/export/color_predictor_model.pth", "./model/data/color_dataset.csv")
#     # Load the model
#     model_loader.load_model()
#     # Get the model
#     model = model_loader.get_model()
#     # Predict the text color for a background color
#     print(model_loader.predict_text_color([255, 255, 255]))