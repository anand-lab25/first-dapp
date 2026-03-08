# ml/scripts/preprocess_transactions.py 
import pandas as pd 
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="most_frequent") 
def  preprocess_transactions(path):
    df=pd.read_csv(path)
    #convert  target 
    df['Churn']=df['Churn'].map({'Yes':1,'No':0})
    # fix totalcharges someblanks 
    df["TotalCharges"] = pd.to_numeric(df['TotalCharges'],errors='coerce')
    df=df.dropna(subset=["TotalCharges"])
    df = imputer.fit_transform(df)
    #encode categorical features 
    categorical_cols = ["gender","Partner","Dependents","PhoneService",
                                    "MultipleLines","InternetService","OnlineSecurity",
                                    "OnlineBackup","DeviceProtection","TechSupport",
                                    "StreamingTV","StreamingMovies","Contract",
                                    "PaperlessBilling","PaymentMethod"]
    df=pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df