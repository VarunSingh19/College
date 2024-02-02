clc;
clear;
close;

// Input sequences
x = input('Enter the Input Sequence x(n) = '); // Example input: [1, 2, 3, 1]
m = length(x);
xl = input('Enter the lower index of Input Sequence = '); // Example: 0
xh = xl + m - 1;
n = xl:1:xh;

subplot(3, 1, 1);
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
h = input('Enter the Impulse Response Sequence h(n) = '); // Example impulse response: [1, 2, 1, -1]
l = length(h);
hl = input('Enter the lower index of Impulse Response Sequence = '); // Example: -1
hh = hl + l - 1;
g = hl:1:hh;

subplot(3, 1, 2);
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

// Linear convolution
nx = xl + hl; // range of k
nh = xh + hh; // range of n
x = [x, zeros(1, l)];
h = [h, zeros(1, m)];
y = zeros(1, m + l - 1);

for i = 1:m + l - 1
    y(i) = 0;
    for j = 1:m + l - 1
        if (j < i + 1)
            y(i) = y(i) + x(j) * h(i - j + 1);
        end
    end
end

disp('Linear Convolution using Equation, y(n):');
disp(y);

r = nx:nh;
subplot(3, 1, 3);
a = gca();
a.x_location = 'origin';
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3('gnn', r, y);
title('Output Response Sequence of Linear Convolution using Equation y[n]');
xlabel('Samples n');
ylabel('Amplitude');
