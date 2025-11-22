from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess(x):
    le= LabelEncoder()
    x['performance']= le.fit_transform(x['performance'])
    X= x.drop('performance', axis=1)
    y= x['performance']

    X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test