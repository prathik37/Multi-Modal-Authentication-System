clear all
clc
close all

classes = 1;
trainImg = 7;

numRows = 112;
numCols = 92;

dirPath = 'D:\Final Year Project\Code\RealWorldDatabase\Conditioned\s';
imgReadPath = 'D:\Final Year Project\Code\RealWorldDatabase\Original\s';
imgWritePath = 'D:\Final Year Project\Code\RealWorldDatabase\Conditioned\s';

i=1;
j=7;
% folderName = 'Conditioned';
% mkdir(strcat('D:\Final Year Project\Code\RealWorldDatabase\',folderName));
%for i = 1 : classes
 %   mkdir(strcat(dirPath,int2str(classes)));
  %  for j = 1 : trainImg
  
       img = imread(strcat(imgReadPath,int2str(i),'\',int2str(j),'.jpg')); 
       img = rgb2gray(img);
       img = imresize(img,[numRows numCols]);
       imwrite(img,strcat(imgWritePath,int2str(i),'\',int2str(j),'.jpg'));
    %end
%end

display('Done')
       
        