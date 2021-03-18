'''
Afterfetaures and BOW for preparing excelfiles EmotiW
'''
#### preparing each folders again for labels for training data
import os
import shutil
path_in = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/train/'

emo_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
for word in emo_list: 
    path_out = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Train_BOW/'+ word +'/'
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    for filename in os.listdir(path_in):
        if word in filename:
            shutil.move(os.path.join(path_in,filename), os.path.join(path_out,filename))

#### preparing each folders again for labels for testing data
path_in = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/val/'

emo_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
for word in emo_list: 
    path_out = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Val_BOW/'+ word +'/'
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    for filename in os.listdir(path_in):
        if word in filename:
            shutil.move(os.path.join(path_in,filename), os.path.join(path_out,filename))
### concatinating all 500 features for each emotion
import numpy as np
import pandas as pd
import os
out_path = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Val_final/'
if not os.path.exists(out_path):
    os.makedirs(out_path)
emo_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
for word in emo_list: 
    path_out = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Val_BOW/'+ word +'/'
    out_ = np.empty((0,500))
    for filename in os.listdir(path_out):
        print(filename)
        print(path_out)
        df = pd.read_csv(os.path.join(path_out,filename),delimiter=';', header= None).values
        print(df.shape)
        out_ = np.vstack((out_,df))
    df1=pd.DataFrame(out_)
    df1.to_csv(out_path+ word+'.csv',index=None)
    
##### concatinating 500 features and label
import os
out_path = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/Train_final/'
out_path1 = '/media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat_BOW/'
final_result = np.empty((0, 501))
emo_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
for index,word in enumerate(emo_list): 
    filename = word+'.csv'
    print(os.path.join(out_path,filename))
    
    df = pd.read_csv(os.path.join(out_path,filename)).values
    print(df.shape)
    lbl_indoor = (index*np.ones(df.shape[0])).astype(int)
    print(lbl_indoor)
    final_vec = np.hstack((df, lbl_indoor[:,None]))
    final_result = np.vstack((final_result, final_vec))
    print(final_result.shape)    
df1=pd.DataFrame(final_result)
df1.to_csv(out_path1+'Train_final_all.csv',index=None,header=None)
            
