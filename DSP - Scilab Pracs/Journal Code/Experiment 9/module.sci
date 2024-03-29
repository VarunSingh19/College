// Aim : WRITE A SCILAB PROGRAM TO COMPUTE CIRCULAR CONVOLUTION OF THE TWO SEQUENCES USING DFT BASED APPROACH.

clc;
clear;
close;

x = input("Enter The Input Sequence = "); // x =[1 1 2 2]
m = length(x);
xl = input("Enter the lower index of input Sequence = "); // 0
xh = xl + m - 1;
n = xl:1:xh;

subplot(3, 1, 1);
a = gca();
a.x_location = "Origin";
a.y_location = "Origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', n, x);
title("Input Sequence x[n]");
xlabel("Sample n");
ylabel("Amplitude");

h = input("Enter the Impulse responses Sequence = "); // h=[1 2 3 4]
l = length(h);
hl = input("Enter the lower index of Impulse responses Sequence = "); // 0
hh = hl + l - 1;
g = hl:1:hh;

subplot(3, 1, 2);
a = gca();
a.x_location = "Origin";
a.y_location = "Origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', g, h);
title('Impulse Response Sequence h[n]');
xlabel("Samples n");
ylabel("Amplitude");

// Zero-pad to make lengths equal
N = max(m, l);
p = N - m;
q = N - l;
x = [x, zeros(1, p)];
h = [h, zeros(1, q)];

XK = fft(x);
HK = fft(h);
YK = XK .* HK;
y = ifft(YK);

disp('Circular convolution by FFT y[n]:');
disp(real(y));

nx = xl + hl;
r = nx : nx + length(y) - 1;

subplot(3, 1, 3);
a = gca();
a.x_location = "Origin";
a.y_location = "Origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, y);
title("Output Response Sequence of Circular Convolution y[n] using FFT");
xlabel("Sample n");
ylabel("Amplitude");
