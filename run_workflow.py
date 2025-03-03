import os
import subprocess

'''
Usage Instructions
Ensure you have the create_model.py and mri_analysis.py files in the same directory as run_workflow.py.

Update the dicom_directory variable in run_workflow.py to point to the directory containing your DICOM files.

Run the run_workflow.py script:

python run_workflow.py
This script will first create the model using create_model.py and then run the MRI analysis using mri_analysis.py. The predictions will be saved in the specified output file.
'''

def run_create_model_script():
    print("Creating the model...")
    subprocess.run(["python", "create_model.py"])
    print("Model created successfully!")

def run_mri_analysis_script(dicom_directory, model_path, output_file):
    print("Running MRI analysis...")
    subprocess.run([
        "python", "mri_analysis.py",
        "--dicom_directory", dicom_directory,
        "--model_path", model_path,
        "--output_file", output_file
    ])
    print("MRI analysis completed successfully!")

def main():
    dicom_directory = "path/to/dicom/files"
    model_path = "mri_anomaly_detection_model.h5"
    output_file = "output/predictions.txt"

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Run the scripts
    run_create_model_script()
    run_mri_analysis_script(dicom_directory, model_path, output_file)

if __name__ == "__main__":
    main()
