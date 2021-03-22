
clc;
clear all;
close all;

FileData = load('//media/amrgaballah/Backup_Plus/exp_j1/SRMR/SEWA_16/sewa16.mat');
writetable(FileData.feat1,'//media/amrgaballah/Backup_Plus/exp_j1/SRMR/SEWA_16/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_0dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_0dB/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_10dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_10dB/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_20dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_airport_20dB/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_0dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_0dB/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_10dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_10dB/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_20dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_bable_20dB/FileName.csv');


FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.8/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.8/FileName.csv');


FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.48/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.48/FileName.csv');


FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.25/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/rev_0.25/FileName.csv');

FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_0dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_0dB/FileName.csv');


FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_10dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_10dB/FileName.csv');


FileData = load('/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_20dB/sewa16.mat');
writetable(FileData.feat1,'/media/amrgaballah/Backup_Plus/exp_j1/SRMR/recordings_audio_rev_0.25_bable_20dB/FileName.csv');

