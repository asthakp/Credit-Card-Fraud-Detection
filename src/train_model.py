import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from preprocessing import split_scale

def train (df_path):
    df=pd.read_csv(df_path)
    X_train, X_test, y_train,y_test,scaler=split_scale(df)

    #Logistic Regression with class weight
    lr=LogisticRegression(max_iter=1000, class_weight='balanced')
    lr.fit(X_train, y_train)

    ## randomforest classifier without smote
    rf_nosmote=RandomForestClassifier(n_estimators=200, random_state=42)
    rf_nosmote.fit(X_train,y_train)

    #Smote OverSampling RandomForest
    smote=SMOTE(random_state=42)
    X_train_smote,y_train_smote=smote.fit_resample(X_train,y_train)
    
    rf=RandomForestClassifier(n_estimators=200, random_state=42)
    rf.fit(X_train_smote,y_train_smote)


    joblib.dump(lr,'models/logistic_model.pkl')
    joblib.dump(rf,'models/randomforest_model.pkl')
    joblib.dump(rf_nosmote,'models/randomforest_nosmote_model.pkl')
    joblib.dump(scaler,'models/scaler.pkl')

    print('Models trained and saved')

if __name__ == '__main__':
    train('data/processed/processed_creditcard.csv')