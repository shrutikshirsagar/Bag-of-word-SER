clc;
clear all;
close all;

FileData = load('//media/amrgaballah/Backup_Plus/hungarian/Hun_srmr_Q.mat')
% out = FileData.feat1
writetable(FileData.feat1,'//media/amrgaballah/Backup_Plus/hungarian/filename_hun_srmr.csv','Delimiter',',')