import joblib
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from preprocess_transactions import  preprocess_transactions 
 #use pre_processing_data 
 df=preprocess_transactions("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
 X=df.drop(columns=["customerID","Churn"])
 Y=df["Churn"]
 X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
 model=LogisticRegression(max_iter=1000)
 model.fit(X_train,Y_train)
joblib.dump((model,X.columns.tolist()),"backend/models/churn_model.pkl")
print("Model trained and saved to backend/models/churn_model.pkl ")