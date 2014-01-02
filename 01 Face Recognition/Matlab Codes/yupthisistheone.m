clc
clear all
close all
features=2500;
p=sqrt(features);
classes=40;
training=4;
g=1;
vmax = 2.684;
vmin = -2.684;


global Imil Imol
%tic
trail=1;%no. of trials
tic
for x=1:trail
    a1=[1:10];   %random number generation
    b1=zeros(40,4); %training set
    for i=1:40
        b1(i,1:4)=randperm(10,4);
        c1(i,1:6)=setdiff(a1,b1(i,1:4)); %testing set
    end
    
    
    for i=1:classes
        for j=1:training
            I{i,j} = imread(strcat(pwd,'\s',num2str(i),'\',num2str(b1(i,j)),'.pgm')); %read 4 training images from 40 classes
            Idct{i,j}=dct2(I{i,j});                                             %take dct of all 40x4 images
            Idctcomp{i,j}(1:p,1:p)= Idct{i,j}(1:p,1:p);                         %choose the 50x50 matrix of all 160 images
        end
    end
    
    %to find means of 40 classes
    for i=1:classes
        j=1;
        Imi{i}=(Idctcomp{i,j}+Idctcomp{i,j+1}+Idctcomp{i,j+2}+Idctcomp{i,j+3})./4;
        Imil{i}=reshape(Imi{i}.',1,[]); %to convert mean of all classes to arrays
    end
    
    %to find grand mean of all 40 classes
    Imo=zeros(50);
    for i=1:classes
        Imo=Imo+Imi{1,i};
    end
    Imo=Imo./classes;
    Imol=reshape(Imo.',1,[]); %to convert grandmean to an array
    
    
    dim = features;
    iterations = 100; %increase it to 100
    inertia = 0.6;
    correction_factor =  2.0;
    N = 30;
    
    
    for i = 1:N                         % no of particles
        for d = 1:dim                   % 2500 dimensions
            %x(i,d) = floor(rand + 0.5); % to obtain random string of 1s and 0s
            x(i,d) = (rand > 0.5);
            % x(i,d)=randi([0,1]);
            % vel(i,d) = 0;               % initial velocity = 0
            vel(i,d)=rand;
            p_best(i,d) = x(i,d);       % calculate pbest
        end
        
        fit_pbest(i) = bpso_fit(x(i,:)); % store fitness values of all 30 p_bests
    end
    
    [fit_gbest,index] = max(fit_pbest);
    %[fit_gbest,index] = min(fit_pbest);
    g_best = p_best(index,:);
    
    
    for iter = 1:iterations
        for i=1:N
            f = bpso_fit(x(i,:));
            
            if (f > fit_pbest(i))
                fit_pbest(i) = f;
                p_best(i,:) = x(i,:);
            end
            
            [fit_gbest,index] = max(fit_pbest);
            %[fit_gbest,index] = min(fit_pbest);
            g_best = p_best(index,:);
            
            for d=1:dim
                vel(i,d) = (inertia)*(vel(i,d)) + correction_factor * (p_best(i,d) - x(i,d))* rand + correction_factor * (g_best(1,d) - x(i,d))* rand;
                
                if (vel(i,d) > vmax )
                    vel(i,d) = vmax;
                end
                
                if (vel(i,d) < vmin )
                    vel(i,d) = vmin;
                end
                
                x(i,d) = (rand) < (1/(1 + exp(-vel(i,d))));
                
            end
        end
    end
    
    
    z= vec2mat(g_best,50);
    % for x=1:3
    for i=1:40
        for j=1:4
            zidct{i,j}=Idctcomp{i,j}.*z; %feature gallery
        end
    end
    
    
    
    
    %testing
    %tic
    for i=1:classes
        
        for j=1:6
            
            T{i,j} = imread(strcat(pwd,'\s',num2str(i),'\',num2str(c1(i,j)),'.pgm'));
            
            Tdct{i,j}=dct2(T{i,j});                                             %take dct of all 40x4 images
            Tdctcomp{i,j}(1:p,1:p)= Tdct{i,j}(1:p,1:p);                         %choose the 50x50 matrix of all 240 images
        end
    end
    
    
    
    for i=1:40
        for j=1:6
            Tidct{i,j}=Tdctcomp{i,j}.*z;
        end
    end
    s=1;
    for i=1:40
        for j=1:6
            
            a=Tidct{i,j}; %testing matrices
            for k=1:40
                for l=1:4
                    b=zidct{k,l}; %trained matrices
                    f=(a-b).^2;
                    yy(s)=sqrt(sum(f(:)));
                    s=s+1;
                end
            end
        end
    end
    
    final_values = vec2mat(yy,160);
    
    for i=1:240
        [value(i),index(i)] = min(final_values(i,:));
        norm_index(i)=ceil(index(i)/4); %4 because no of training images from each class is 4
    end
    
    norm_mat=vec2mat(norm_index,6);
    
    count=0;
    for i=1:40
        for j=1:6
            if (norm_mat(i,j)==i)
                count=count+1;
            end
        end
    end
    % t1=toc
    % recognition_rate= (count/240)*100
    t1=toc;
    recognition(g) = count/240;
    disp(recognition)
    g=g+1;
end

v=0;
for i=1:trail
    v= v+ recognition(i);
end

%t1=toc
recognition_rate=(v/trail)*100
toc/60








