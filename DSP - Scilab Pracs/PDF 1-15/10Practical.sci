clc;
clear;
close;

x = input('Enter the input sequence: '); // x=[1 2 -1 2 3 -2 -3 -1 1 1 2 -1]
m = length(x);

xl = input('Enter the lower index of input sequence: '); // 0
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
title('Input Sequence x[n]');
xlabel('Sample n');
ylabel('Amplitude');

h = input('Enter the impulse response sequence: '); // h=[1 2 3 -1]
l = length(h);

hl = input('Enter the lower index of impulse response sequence: '); // 0
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
xlabel('Sample n');
ylabel('Amplitude');

N = m + l - 1;
h1 = [h, zeros(1, N - l)]; // Zero-pad h to match the length of x
n3 = length(h1);

y = zeros(1, N);

H = fft(h1);

for i = 1:l:N
    x1 = [x(i : min(i + n3 - 1, m)), zeros(1, n3 - 1)];
    x2 = fft(x1);
    x3 = x2.*.H; // Fix: Remove the dot before H
    x4 = ifft(x3); // Fix: Remove the round function
    
    if i == 1
        y(1 : n3) = x4(1 : n3);
    else
        y(i : i + n3 - 1) = y(i : i + n3 - 1) + x4(1 : n3);
    end
end

disp('Output sequence using Overlap-Add method y(n):');
disp(y(1 : N));

nx = xl + hl;
r = nx : length(y) - 1;

subplot(3, 1, 3);
a = gca();
a.x_location = "Origin";
a.y_location = "Origin";
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, y);
title('Output sequence using Overlap-Add method y[n]');
xlabel('Sample n');
ylabel('Amplitude');
