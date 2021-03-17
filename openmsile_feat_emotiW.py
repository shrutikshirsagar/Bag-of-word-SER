import os

out = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
for foldername in out:
    path_in = '/media/amrgaballah/Backup_Plus/stress/EmotiW/Train_AFEW/'+ foldername+ '/'
    path_out = '//media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat/Train_AFEW/' + foldername +'/'
    if not os.path.exists(path_out):
        os.makedirs(path_out)
    filelist = [f for f in os.listdir(path_in)]

    ##Code to generate LLDs
    for f in filelist:
        os.system("inst/bin/SMILExtract -C config/prosodyShs.conf -I /media/amrgaballah/Backup_Plus/stress/EmotiW/Train_AFEW/"+ foldername + "/" + f + " -csvoutput /media/amrgaballah/Backup_Plus/exp_j1/emotiW_feat/Train_AFEW/"+ foldername+ "/" + f.split('.')[0] + ".csv")

   

