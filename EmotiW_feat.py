
'''
prosodic: prosodyShs.conf
IS2011: config/IS11_speaker_state_LLD.conf
'''
import os

out = ['Train', 'Val']
for foldername in out:
    path_in = '/media/amrgaballah/Backup_Plus/exp_j1/EmotiW/'+ foldername+ '/'
    path_out = '//media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat/Opensmile/' + foldername +'/'
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    filelist = [f for f in os.listdir(path_in)]

    ##Code to generate LLDs
    for f in filelist:
        os.system("inst/bin/SMILExtract -C config/IS11_speaker_state_LLD.conf -I /media/amrgaballah/Backup_Plus/exp_j1/EmotiW/"+ foldername + "/" + f + " -csvoutput /media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat/Opensmile/"+ foldername+ "/" + f.split('.')[0] + ".csv")

   

