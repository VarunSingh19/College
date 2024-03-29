// Aim : WRITE A SCILAB PROGRAM TO COMPUTE LINEARITY PROPERTY OF A GIVEN SIGNAL.

clc;
clear;
close;

// Example 1
n = 0:10;
a = 2;
b = 3;
x1 = sin(2 * %pi * 0.1 * n); // input sequence 1
x2 = cos(2 * %pi * 0.5 * n); // input sequence 2
x = a * x1 + b * x2; // homogeneity and superposition - op1
y = 0.5 * x; // system y = 0.5 * x
y1 = 0.5 * x1;
y2 = 0.5 * x2;
yt = a * y1 + b * y2; // homogeneity and superposition - op2
d = y - yt; // op2 - op1 = difference
disp('Output of System y(n) = 0.5 x(n) is:');
if (d == 0)
      disp('System is linear');
else
      disp('System is Non-linear');
end

// Example 2
n = 0:10;
a = 2;
b = 3;
x1 = sin(2 * %pi * 0.1 * n); // input sequence 1
x2 = cos(2 * %pi * 0.5 * n); // input sequence 2
x = a * x1 + b * x2; // homogeneity and superposition - op1
y = sqrt(x); // system y = sqrt(x)
y1 = sqrt(x1);
y2 = sqrt(x2);
yt = a * y1 + b * y2; // homogeneity and superposition - op2
d = y - yt; // op2 - op1 = difference
disp('Output of System y(n) = sqrt(x(n)) is:');
if (d == 0)
      disp('System is linear');
else
      disp('System is Non-linear');
end
