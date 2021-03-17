clc;
clear all;
close all
class = {'Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise'};

for c = 1:length(class)
    path_in = ['/media/amrgaballah/Backup_Plus/stress/2017_EmotiW/Val_AFEW/' class{c} '/'];
    path_out = ['/media/amrgaballah/Backup_Plus/stress/EmotiW/Val_AFEW/' class{c} '/'];
    
    

    
    if(isempty(dir(path_out)))
        mkdir(path_out);
    end
    strFiles = strcat(path_in, '*.avi');
    % For each audio file in audioFolder add noise at using the snr parameter
    F = dir(strFiles);
    
    for iFile = 1:length(F)
        filename = fullfile(path_in, F(iFile).name)
        [fPath, fName, fExt] = fileparts(filename);
        try
            [data, fs] = audioread(filename);
        catch
            continue
        end
        [fPath, fName, fExt] = fileparts(filename);
        out1 = strcat(fName,'.wav')
        out_f = fullfile(path_out,out1)
        
        audiowrite(out_f,data,fs)
    end
end    