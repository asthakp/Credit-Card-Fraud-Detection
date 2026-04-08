import pandas as pd
import joblib
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import roc_auc_score, average_precision_score
from preprocessing import split_scale

def evaluate(model_path, df_path,model_name):
    df=pd.read_csv(df_path)
    model=joblib.load(model_path)

    X_train, X_test, y_train, y_test,scaler=split_scale(df)

    y_pred=model.predict(X_test)
    y_prob=model.predict_proba(X_test)[:,1]
    
    cm=confusion_matrix(y_test,y_pred)
    tn,fp,fn,tp=cm.ravel()

    report=classification_report(y_test,y_pred, output_dict=True, zero_division=0)

    return {
        "Model":model_name,
        "ROC-AUC": roc_auc_score(y_test,y_prob),
        "PR-AUC": average_precision_score(y_test,y_prob),
        "Accuracy":report["accuracy"],
        "Precision (Fraud=1)":report["1"]["precision"],
        "Recall (Fraud=1)": report["1"]["recall"],
        "F1-Score (Fraud=1)":report["1"]["f1-score"],
        "TP":int(tp), "FP":int(fp), "FN": int(fn), "TN":int(tn)
    }
