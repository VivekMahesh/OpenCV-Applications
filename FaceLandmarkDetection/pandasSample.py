import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ckd_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Chronic%20Kidney%20Disease"
                       "%20(CKD)%20Dataset/ChronicKidneyDisease.csv")
#print(ckd_data['cad'].isnull())
#ckd_data['bp'] = ckd_data['bp'].fillna(76.469072)
print(ckd_data['cad'].describe())
#76.469072