import joblib
import numpy as np

def predict(new_data):
    model=joblib.load("saved_models/best_model.pkl")

    new_data=np.array(new_data).reshape(1,-1)
    prediction=model.predict(new_data)[0]
    mapping={0:"High",1:"Low",2:"Medium"}

    return mapping.get(prediction, "Unknown")