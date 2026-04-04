import numpy as np

def add_features(df):
    df=df.copy()
    df['Amount_log']=np.log1p(df['Amount'])
    df['Hour']=(df['Time']/36000)%24
    df['Is_Night']=df['Hour'].apply(lambda x:1 if x>=0 and x<=6  else 0)
    return df