clc;
clear;
close;

f = input('Enter continuous time signal frequency= ', 's'); // f = 0.1
f = evstr(f);
a = input('Enter continuous time signal amplitude= ', 's'); // a = 1
a = evstr(a);
t = 0:0.01:100;
x = a * sin(2 * %pi * f * t);
subplot(2, 2, 1);
b = gca();
b.x_location = 'origin';
b.y_location = 'origin';
b.foreground = 5;
b.font_color = 5;
b.font_style = 5;
plot(t, x);
title('Original Continuous Time Signal');
xlabel('Time t');
ylabel('Amplitude');

fs1 = input('Enter sampling frequency equal to 2*fs= ', 's'); // fs1 = 0.2
fs1 = evstr(fs1);
fd = f / fs1;
n = 0:0.01:100;
x1n = a * sin(2 * %pi * f * n / fs1);

subplot(2, 2, 2);
b = gca();
b.x_location = 'origin';
b.y_location = 'origin';
b.foreground = 5;
b.font_color = 5;
b.font_style = 5;
plot(n, x1n);
title('Reconstructed signal with sampling frequency equal to 2*fs');
xlabel('Time t');
ylabel('Amplitude');

fs2 = input('Enter sampling frequency less than 2*fs= ', 's'); // fs2 = 0.1
fs2 = evstr(fs2);
x2n = a * sin(2 * %pi * f * n / fs2);

subplot(2, 2, 3);
b = gca();
b.x_location = 'origin';
b.y_location = 'origin';
b.foreground = 5;
b.font_color = 5;
b.font_style = 5;
plot(n, x2n);
title('Reconstructed signal with sampling frequency less than 2*fs (Aliasing effect)');
xlabel('Time t');
ylabel('Amplitude');

fs3 = input('Enter sampling frequency greater than 2*fs= ', 's'); // fs3 = 1
fs3 = evstr(fs3);
x3n = a * sin(2 * %pi * f * n * fs3);

subplot(2, 2, 4);
b = gca();
b.x_location = 'origin';
b.y_location = 'origin';
b.foreground = 5;
b.font_color = 5;
b.font_style = 5;
plot(n, x3n);
title('Perfect Reconstructed signal with sampling frequency greater than 2*fs');
xlabel('Time t');
ylabel('Amplitude');
