import pandas as pd
import glob
import numpy as np
import os
#define a folder path where you have all the csv files without header
path_in = "//media/amrgaballah/Seagate Backup Plus Drive/Journal_paper_MSF_revised_data/latestexp_2021/features/Noisy/IS2011/"
path_out= "//media/amrgaballah/Seagate Backup Plus Drive/Journal_paper_MSF_revised_data/latestexp_2021/features/Noisy_feat_avg_10/IS2011/"

if not os.path.exists(path_out):
    os.makedirs(path_out)

for root,dirs,filenames in os.walk(path_in):
 
    for filename in filenames:
        base_ = os.path.basename(root)
        df11 = pd.read_csv(os.path.join(root,filename),delimiter=';')
        print(os.path.join(root,filename), df11.shape)
        path_out1 = path_out + os.path.basename(root) +'/'
        print(path_out1)
        if not os.path.exists(path_out1):
            os.makedirs(path_out1)
        #this will drop first two columns
        df11.drop(df11.columns[0],axis=1,inplace=True)
        df11.drop(df11.columns[0],axis=1,inplace=True)
        print(df11.shape)
        df22 = df11.iloc[0]
        df22 = df22.values
        #this will take the rolling mean
        df1 = df11.rolling(10).mean() 
        print(df1.shape)
        #this will consider the corresponding location of frame
        df2 = df1.iloc[::10, :]
        df2 = df2.values
        df2 = df2[1:,:]
        print(df2.shape)
        # pd.concat(objs,axis=0,join="outer",ignore_index=False,keys=None,levels=None,names=None,verify_integrity=False,copy=True)
        df23 = np.vstack((df22,df2))
        print(df23.shape)
        df1 = np.repeat(np.array([filename]), df23.shape[0])
       
        a = np.arange(start=0, stop=np.round(0.1*df23.shape[0],3), step=0.1)
        out = np.hstack((df1[:,None], a[:, None],df23))

        df_file=pd.DataFrame(out)
        df_file.to_csv(path_out1+ filename, header=None, index= None)
