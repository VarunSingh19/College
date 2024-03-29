// Aim : WRITE A SCILAB PROGRAM TO FIND N-POINT DFT OF THE GIVEN SEQUENCE.

clc;
clear;
close;

N = input('Enter the value of N= '); // Number of points
x = input('Enter the input sequence x(n) = ');

subplot(3, 2, 1);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(x);
title('Input sequence');
xlabel('Samples n');
ylabel('Amplitude');

// Calculation of DFT
y = zeros(1, N);
for k = 1:N
    y(k) = 0;
    for n = 1:N
        y(k) = y(k) + x(n) * exp(-%i * 2 * %pi * (k - 1) * (n - 1) / N);
    end
end

A = real(y);
B = imag(y);

disp('The output DFT sequence is:');
disp(y);

subplot(3, 2, 2);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(y);
title('Output DFT sequence');
xlabel('Samples n');
ylabel('Amplitude');

// Real value
disp('The resultant real value is:');
disp(A);
subplot(3, 2, 3);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(A);
title('Real Value');
xlabel('Samples n');
ylabel('Amplitude');

// Imaginary value
disp('The resultant imaginary value is:');
disp(B);
subplot(3, 2, 4);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(B);
title('Imaginary Value');
xlabel('Samples n');
ylabel('Amplitude');

// Magnitude response
mag = abs(y);
disp('The Magnitude response is:');
disp(mag);
subplot(3, 2, 5);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(mag);
title('Magnitude Response');
xlabel('Samples n');
ylabel('Amplitude');

// Phase response
x1 = atan(imag(y), real(y));
phase = x1 * (180 / %pi);
disp('The Phase response is:');
disp(phase);
subplot(3, 2, 6);
a = gca();
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3(phase);
title('Phase Response');
xlabel('Samples n');
ylabel('Phase');
