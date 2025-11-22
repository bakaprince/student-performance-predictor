# Student Performance Prediction (ML Project)

## Overview
A Machine Learning model that predicts whether a student will score High, Medium, or Low based on academic behavior.

## Features
- Dataset generation and loading
- Preprocessing pipeline
- Model training (LR, DT, RF)
- Best model selection
- Pickle model saving/loading
- High accuracy (~99%)

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Joblib

## How to Run
1. Clone repository
2. Install dependencies:
    pip install -r requirements.txt
3. Run main:
    python main.py

##Data Range Used For Training:

-attendance: 40–100
-study_hours: 1–30
-assignments: 2–10
-internal: 20–50
-extra: 0–1


## Example Prediction
Attendance: 80  
Study hours: 12  
Assignments: 7  
Internal: 45  
Extracurricular: 1  
→ Prediction: **High**

##Mapping Logic
High: 0
Low: 1
Medium: 2

## Project Structure
student_performance_predictor  
│── data  
│── modules  
│── saved_models   
│── main.py  
│── gen_dataset.py
│── README.md  
│── statement.md  
│── requirements.txt


## Accuracy
- Logistic Regression: 99%
- Decision Tree: 96%
- Random Forest: 97%

## Future Scope
- Use real datasets
- Add more student parameters
- Deploy online
- Use Streamlit to build gui

