from modules.data_loader import load_dataset
from modules.process import preprocess
from modules.train import train_models
from modules.predict import predict

df= load_dataset()
X_train, X_test, y_train, y_test= preprocess(df)
train_models(X_train, X_test, y_train, y_test)

# Example prediction
new_student_data= [67,16,5,39,1]  # Example feature values
prediction= predict(new_student_data)
print(f"Predicted Performance: {prediction}")