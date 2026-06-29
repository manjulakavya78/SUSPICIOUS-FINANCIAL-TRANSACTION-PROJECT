import tkinter as tk
from tkinter import messagebox
from tkinter import Text
from tkinter import filedialog
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Global variables to store data, labels, and model accuracies
global model, X_train, X_test, y_train, y_test, df, scaler
model_accuracies = {}  # Dictionary to store model accuracies

# Function to load dataset
def load_dataset():
    global df
    filename = filedialog.askopenfilename(title="Select Dataset", filetypes=[("CSV Files", "*.csv")])
    if filename:
        df = pd.read_csv(filename)  # Load the dataset from the selected CSV file
        text.delete('1.0', tk.END)
        text.insert(tk.END, f"Dataset loaded from: {filename}\n\n")
        text.insert(tk.END, df.head())
    else:
        messagebox.showerror("Error", "Please select a valid CSV file.")

# Function for data preprocessing
def preprocess_data():
    global X_train, X_test, y_train, y_test, df, scaler
    if df is None or df.empty:
        messagebox.showerror("Error", "Please upload a dataset first.")
        return
    
    # Assuming the dataset has columns: 'Amount', 'TransactionTime', 'Merchant', 'TransactionType', 'Label'
    # You may need to adjust this based on your actual dataset
    features = df.drop(columns=['Label'])  # Assuming 'Label' is the target column
    labels = df['Label']
    
    # Standardize the data (important for neural networks)
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)
    
    # Display training and testing data information
    text.delete(1.0, tk.END)
    text.insert(tk.END, f"Data Preprocessing Completed.\n")
    text.insert(tk.END, f"Total rows in dataset: {len(df)}\n")
    text.insert(tk.END, f"Training set size: {len(X_train)}\n")
    text.insert(tk.END, f"Testing set size: {len(X_test)}\n")

# Function for creating the Autoencoder model
def create_autoencoder(input_shape):
    model = Sequential()
    model.add(Input(shape=input_shape))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(input_shape[0], activation='sigmoid'))  # Output layer, same size as input for reconstruction
    model.compile(optimizer=Adam(), loss='mean_squared_error')
    return model

# Function to train the Autoencoder model
def train_autoencoder_model():
    global model
    if X_train is None or y_train is None:
        messagebox.showerror("Error", "Preprocessing data first is required.")
        return
    
    model = create_autoencoder(X_train.shape[1:])
    history = model.fit(X_train, X_train, epochs=10, batch_size=32, validation_data=(X_test, X_test))
    
    # Predict on the test set and calculate reconstruction errors
    X_train_pred = model.predict(X_train)
    X_test_pred = model.predict(X_test)
    
    train_mse = mean_squared_error(X_train, X_train_pred)
    test_mse = mean_squared_error(X_test, X_test_pred)
    
    # Store the reconstruction errors in the model_accuracies dictionary
    model_accuracies["Autoencoder"] = (train_mse, test_mse)
    
    # Display results in the text box
    text.insert(tk.END, f"Autoencoder Model training completed\n")
    text.insert(tk.END, f"Training MSE: {train_mse:.4f}\n")
    text.insert(tk.END, f"Testing MSE: {test_mse:.4f}\n")

# Function to predict suspicious transactions
def predict_suspicious_transactions():
    global model, scaler
    if model is None:
        messagebox.showerror("Error", "Autoencoder model is not trained yet.")
        return
    
    user_input = predict_entry.get()
    if not user_input:
        messagebox.showerror("Error", "Please enter a transaction for prediction.")
        return
    
    # Assuming the user input is a comma-separated list of transaction features (e.g., 'Amount, Time, Merchant, Type')
    try:
        user_input_data = np.array([float(i) for i in user_input.split(',')])
        user_input_scaled = scaler.transform([user_input_data])  # Scale the input using the same scaler
        
        # Predict using the trained autoencoder model
        reconstruction = model.predict(user_input_scaled)
        mse = mean_squared_error(user_input_scaled, reconstruction)
        
        # Set a threshold for anomaly detection (based on the training MSE)
        threshold = np.percentile(model_accuracies["Autoencoder"][0], 95)  # Set the threshold at 95th percentile
        
        if mse > threshold:
            text.insert(tk.END, f"Suspicious Transaction Detected! (MSE: {mse:.4f})\n")
            text.insert(tk.END, "Recommendation: This transaction is highly anomalous. Review for potential fraud.\n")
        else:
            text.insert(tk.END, f"Normal Transaction Detected! (MSE: {mse:.4f})\n")
            text.insert(tk.END, "This transaction appears to be normal.\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error processing the input data: {e}")

# Tkinter GUI components
root = tk.Tk()
root.title("Suspicious Financial Transaction Detection Using Autoencoder")
root.geometry("1300x800")

# Title Label
font = ('times', 16, 'bold')
title_label = tk.Label(root, text="Suspicious Financial Transaction Detection Using Autoencoder", font=font)
title_label.config(bg='greenyellow', fg='dodger blue')
title_label.config(height=3, width=120)
title_label.place(x=0, y=5)

# Text area for displaying results
font1 = ('times', 12, 'bold')
text = Text(root, height=20, width=150)
scroll = tk.Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50, y=120)
text.config(font=font1)

# Buttons for different functions
font1 = ('times', 13, 'bold')

# Dataset upload button
upload_button = tk.Button(root, text="Upload Dataset", font=font1, command=load_dataset)
upload_button.place(x=50, y=550)

# Data preprocessing button
preprocess_button = tk.Button(root, text="Data Preprocessing", font=font1, command=preprocess_data)
preprocess_button.place(x=220, y=550)

# Train Autoencoder button
train_autoencoder_button = tk.Button(root, text="Train Autoencoder", font=font1, command=train_autoencoder_model)
train_autoencoder_button.place(x=400, y=550)

# Predict suspicious transactions button
predict_label = tk.Label(root, text="Enter Transaction (comma-separated features):", font=font1)
predict_label.place(x=50, y=600)

predict_entry = tk.Entry(root, font=font, width=80)
predict_entry.place(x=50, y=630)

predict_button = tk.Button(root, text="Predict", font=font1, command=predict_suspicious_transactions)
predict_button.place(x=1050, y=630)

# Start the Tkinter event loop
root.config(bg='LightSkyBlue')
root.mainloop()
