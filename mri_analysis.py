import os
import numpy as np
import pydicom
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

def load_dicom_images(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".dcm"):
            filepath = os.path.join(directory, filename)
            dicom = pydicom.dcmread(filepath)
            image = dicom.pixel_array
            images.append(image)
    return np.array(images)

def preprocess_images(images):
    processed_images = []
    for image in images:
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        processed_images.append(image)
    return np.array(processed_images)

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict_anomalies(model, images):
    predictions = model.predict(images)
    return predictions

def main(dicom_directory, model_path, output_file):
    images = load_dicom_images(dicom_directory)
    processed_images = preprocess_images(images)
    model = load_model(model_path)
    predictions = predict_anomalies(model, processed_images)
    
    with open(output_file, 'w') as f:
        for i, prediction in enumerate(predictions):
            f.write(f"Image {i+1}: {prediction}\n")

if __name__ == "__main__":
    dicom_directory = "path/to/dicom/files"
    model_path = "path/to/saved/model"
    output_file = "output/predictions.txt"
    main(dicom_directory, model_path, output_file)
