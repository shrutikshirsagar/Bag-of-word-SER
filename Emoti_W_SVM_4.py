'''
4 class EmotiW
'''
import scipy.io as spio
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import statistics
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support
df = pd.read_csv('/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Train_final_four.csv').values

X_train=df[:,:-1]


y_train=df[:,-1]


df1 = pd.read_csv('/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Val_final_four.csv').values


X_test=df1[:,:-1]
y_test =df1[:,-1]
clf = svm.SVC()

clf.fit(X_train, y_train)  

y_pred=clf.predict(X_test)

acc=100*sum((y_pred-y_test)==0)/len(y_test)

print(acc)



print(classification_report(y_test,y_pred))

print('macro', precision_recall_fscore_support(y_test,y_pred, average='macro'))
print('micro', precision_recall_fscore_support(y_test,y_pred, average='micro'))
print('weighted', precision_recall_fscore_support(y_test,y_pred, average='weighted'))
F12 = precision_recall_fscore_support(y_test,y_pred, average='macro')
print(F12)
