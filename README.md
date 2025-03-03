# MRI Analysis Workflow

This repository contains a Python script for an advanced Computer Vision workflow that analyzes MRI scans of the skull and spine (in DICOM format) to extract anatomical and physiological anomalies.

## Inputs
- **DICOM Directory**: Path to the directory containing DICOM files of MRI scans.
- **Model Path**: Path to the pre-trained model for anomaly detection.
- **Output File**: Path to the file where predictions will be saved.

## Outputs
- **Predictions File**: A text file containing the predictions for each MRI scan.

## Requirements
- Python 3.7+
- NumPy
- OpenCV
- pydicom
- TensorFlow

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/mri-analysis.git
    cd mri-analysis
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Create the model:
    ```bash
    python create_model.py
    ```

4. Run the analysis script:
    ```bash
    python mri_analysis.py --dicom_directory path/to/dicom/files --model_path path/to/saved/model --output_file output/predictions.txt
    ```

## Example
```bash
python mri_analysis.py --dicom_directory path/to/dicom/files --model_path path/to/saved/model --output_file output/predictions.txt
