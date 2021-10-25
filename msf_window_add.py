import pandas as pd
import numpy as np
import os

path_in = '/home/amrgaballah/Documents/MSF/features/clean/msf/'
path_out= '/home/amrgaballah/Documents/MSF/feature_out/'
window_size= 0.04
if not os.path.exists(path_out):
    os.makedirs(path_out)
for filename in os.listdir(path_in):
    df = pd.read_csv(os.path.join(path_in,filename), header= None).values
    print(df.shape)

    df1 = np.repeat(np.array(filename), df.shape[0])
    print(df1[:, None].shape)
    df2 = np.arange(start=0, stop=window_size*df.shape[0], step=window_size)
    print(df2.shape)
    out = np.hstack((df1[:,None], df2[:, None],df))
    print(out.shape)
    df_file=pd.DataFrame(out)
    df_file.to_csv(path_out + filename, index= None)
