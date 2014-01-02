function [y] = bpso_fit (x)

global  classes Imil Imol

for i=1:classes
    Imil_p{i}=Imil{1,i}.*x;
end

Imol_p=Imol.*x;
ffs=0;

for i=1:classes
ffs=ffs+((Imil_p{1,i}(1,:)-Imol_p(1,:))*((Imil_p{1,i}(1,:)-Imol_p(1,:)))');
end

y=sqrt(ffs);

return