// Aim : Write a scilab program to find auto correlation and cross correalation of the given sequences.


clc;
clear;
close;

// Input sequences
x = input('Enter the Input Sequence x(n) = '); // Example input: [1, 2, 3, 1]
m = length(x);
xl = input('Enter the lower index of InputK Sequence = '); // Example: 0
xh = xl + m - 1;
n = xl:1:xh;

subplot(2, 2, 1);
a = gca();
a.x_location = 'origin';
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', n, x);
title('Input Sequence x[n]');
xlabel('Samples n');
ylabel('Amplitude');

// Impulse response sequence
h = input('Enter the Impulse Response Sequence h(n) = '); // Example impulse response: [1, 2, 1, 1]
l = length(h);
hl = input('Enter the lower index of Impulse Response Sequence = '); // Example: 0
hh = hl + l - 1;
g = hl:1:hh;

subplot(2, 2, 2);
a = gca();
a.x_location = 'origin';
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', g, h);
title('Impulse Response Sequence h[n]');
xlabel('Samples n');
ylabel('Amplitude');

// Autocorrelation
y = xcorr(x, x);
disp('Autocorrelation of given sequence y(n) = ');
disp(y);

nx = xl + xl;
nh = xh + xh;
r = nx:nh;

subplot(2, 2, 3);
a = gca();
a.x_location = 'origin';
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, y);
title('Output of Autocorrelation of Sequence');
xlabel('Samples n');
ylabel('Amplitude');

// Cross-correlation
z = xcorr(x, h);
disp('Cross-correlation of sequence y(n) = ');
disp(z);

subplot(2, 2, 4);
a = gca();
a.x_location = 'origin';
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, z);
title('Output of Cross-correlation of Sequence');
xlabel('Samples n');
ylabel('Amplitude');
