clc 
clear all
close all
Fs = 11025;

u = input ('Enter no. of users \n');

for i=1:u
display('Record sound : Read the content shown');
pause(2);
clc
display('The term voice recognition refers to finding the identity of who is speaking'); 
y(i,:) = wavrecord(5*Fs,Fs,'int16');
display('Stop reading');
pause(2);
clc
if i<u
display('Pausing for 5 seconds');
pause(2);
clc
display('Next user');
end
pause(2);
end


for i=1:u
    display('Recorded voices');
    display('User no.');
    disp(i);  
    wavplay(y(i,:),Fs);
    clc
end

%Computing DCT
for i=1:u
    d(i,:)=dct(abs(y(i,:)));
end

clc
display('Testing stage');
pause(2)
clc
display('Record Sound: Read the content shown');
pause(2);
display('The term voice recognition refers to finding the identity of who is speaking');
user = wavrecord(5*Fs,Fs,'int16');
userd = dct(abs(user));
clc

for i=1:u
    param(i)=sum(d(i,:)-userd(1,:));
end

[C,auth]=min(param);

clc
display('Authentication Established');
display('Voice belongs to user');
disp(auth);

t=0:1/Fs:(length(y(1,:))-1)/Fs; 
subplot 311
plot(t,y(1,:));
title('User 1');
subplot 312
plot(t,y(2,:));
title('User 2');
subplot 313
plot(t,user);
title('Testing');

