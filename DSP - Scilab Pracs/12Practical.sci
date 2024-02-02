clc;
clear;
close;
x = input("Enter input sequence ="); // x = [0 1 2 3 4 5 6 7] or x = [0 1 2 3]
N = length(x);
s = log2(N); // computing array size 
// for sequence size 8
if (N==8) then
   stage1=1;
   x = [x(1) x(5) x(3) x(7) x(2) x(6) x(4) x(8) ]; // stage1
   for stage = 1:s
       for index=0:(2^stage):(N-1); // series of butterfly for each stage
           for n=0:(stage1-1); // create butterfy and save result
               pos = n+index+1; // index of data sample
               pow = (2^(s-stage))*n; // part of power of complex multiplier
               w = exp((-1*%i)*(2*%pi)*pow/N); // complex multiplier
               a = x(pos)+x(pos+stage1).*w; // 1 st part of butterfly creating operation
               b = x(pos)-x(pos+stage1).*w; // 2 nd part of butterfly creating operation
               x(pos)=a; // saving computation of 1st half
               x(pos+stage1)=b; //saving computaion of second part 
   end
               
end
stage1=2*stage1; //computing next stage
end

y = x;
disp("FFT of the given input sequence is y(n) = ");
disp(y);

// for sequence size -4
else
    stage1 = 1;
x = [x(1) x(3) x(2) x(4)];
for stage= 1:s
           for index=0:(2^stage):(N-1); // series of butterfly for each stage
           for n=0:(stage1-1); // create butterfy and save result
               pos = n+index+1; // index of data sample
               pow = (2^(s-stage))*n; // part of power of complex multiplier
               w = exp((-1*%i)*(2*%pi)*pow/N); // complex multiplier
               a = x(pos)+x(pos+stage1).*w; // 1 st part of butterfly creating operation
               b = x(pos)-x(pos+stage1).*w; // 2 nd part of butterfly creating operation
               x(pos)=a; // saving computation of 1st half
               x(pos+stage1)=b; //saving computaion of second part 
   end
               
end
stage1=2*stage1; //computing next stage
end
    
y = x;
disp("FFT of the given input sequence is y(n) = ");
disp(y);
end
