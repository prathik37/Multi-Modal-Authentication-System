%% Speech recognition

clc
clear all
close all
%creating the database
Fs = 11025;
display('First user record sound : Read the data shown');
display('The term voice recognition refers to finding the identity of who is speaking');
y1 = wavrecord(5*Fs,Fs,'int16');
display('End');

clc
pause(5)

display('Second user record sound');
display('The term voice recognition refers to finding the identity of who is speaking');
y2 = wavrecord(5*Fs,Fs,'int16');
display('End');

clc
%Playing it back
display('First user');
wavplay(y1,Fs)

clc
display('Second user');
wavplay(y2,Fs)


% DCT

a1 = dct(abs(y1));
a2 = dct(abs(y2));

%Testing
clc
display('Testing stage');
display('The term voice recognition refers to finding the identity of who is speaking');
u1 = wavrecord(5*Fs,Fs,'int16');
u2 = dct(abs(u1));

param1 = sum(u2 - a1);
param2 = sum(u2 - a2);

clc
if param1 > param2
    display('User 2 authenticated');
else
    display('User 1 authenticated');
end


%Plotting the recorded sounds
t=0:1/Fs:(length(y1)-1)/Fs; 
subplot 311
plot(t,y1)

subplot 312
plot(t,y2)

subplot 313
plot(t,u1)