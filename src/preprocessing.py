from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def split_scale(df):
    x=df.drop('Class',axis=1)
    y=df['Class']

    X_train,X_test,y_train,y_test=train_test_split(x,y, test_size=0.2, stratify=y, random_state=42)

    scaler=StandardScaler()

    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.transform(X_test)

    return X_train_scaled,X_test_scaled,y_train,y_test,scaler

 