function run_srmrnorm(audioFolder, path_out)
    if(isempty(dir(path_out)))
    mkdir(path_out);
    end
    strFiles = strcat(audioFolder, '*.wav');

    F = dir(strFiles);
    feat_fin = num2cell(zeros(1,2))
    for iFile = 1:length(F)
        [s, fs] = audioread(strcat(audioFolder, '/', F(iFile).name));
        
        out = F(iFile).name
        
        [ratio, energy, avg_energy] = SRMR(s, fs, 'norm', 1);
        Feat_final = [cellstr(F(iFile).name), cellstr(num2str(ratio))]
        feat_fin = vertcat(feat_fin, Feat_final)
     
     feat1 = cell2table(feat_fin)
     save(fullfile(path_out,'sewa16.mat'),'feat1');
     
     
  
       
end

