clc;
clear;
close;

x = input('Enter the input sequence x(n) = '); // Example input: [1 2 3 1]
m = length(x);
xl = input('Enter the lower index of input sequence = '); // Example: 0
xh = xl + m - 1;
n = xl:1:xh;

subplot(3, 1, 1);
a = gca();
a.x_location = "origin";
a.y_location = "origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', n, x);
title('Input Sequence x[n]');
xlabel('Samples n');
ylabel('Amplitude');

h = input('Enter the impulse response sequence h(n) = '); // Example impulse response: [1 2 1 -1]
l = length(h);
hl = input('Enter the lower index of impulse response sequence = '); // Example: -1
hh = hl + l - 1;
g = hl:1:hh;

subplot(3, 1, 2);
a = gca();
a.x_location = "origin";
a.y_location = "origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', g, h);
title('Impulse Response Sequence h[n]');
xlabel('Samples n');
ylabel('Amplitude');

nx = xl + hl; // Range of k
nh = xh + hh; // Range of n
p = m + l - 1;

x = [x, zeros(1, p - l)];
h = [h, zeros(1, p - m)];

// DFT - IDFT
XK = fft(x);
HK = fft(h);
YK = XK .* HK;
yn = ifft(YK);

disp('Linear Convolution by DFT-IDFT Method is y(n):');
disp(real(yn));

r = nx:nh;
subplot(3, 1, 3);
a = gca();
a.x_location = "origin";
a.y_location = "origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, yn);
title('Output Response Sequence of Linear Convolution by DFT-IDFT Method y[n]');
xlabel('Samples n');
ylabel('Amplitude');
