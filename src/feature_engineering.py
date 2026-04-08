import numpy as np

def add_features(df):
    df=df.copy()
    df['Amount_log']=np.log1p(df['Amount'])

    df['Hour']=df['Time']/3600%24
 
    ##making time a cycle of 0-24
    df['Hour_sin']=np.sin(2*np.pi*df['Hour']/24)
    df['Hour_cos']=np.cos(2*np.pi*df['Hour']/24)
    
    df['Is_Night']=df['Hour'].apply(lambda x:1 if x>=0 and x<=6  else 0)

    return df