clc;
clear;
close;

// UNIT IMPULSE SIGNAL
L = input('Enter the Length= '); // SET LIMIT: 5
n = -L:L;

x = [zeros(1, L), 1, zeros(1, L)];
subplot(3, 4, 1);
a = gca();
a.y_location = 'origin';
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(n, x);
title('Unit Impulse Signal');
xlabel('Samples n');
ylabel('Amplitude');

// UNIT STEP SIGNAL
y = [zeros(1, L), ones(1, L + 1)];
subplot(3, 4, 2);
b = gca();
b.y_location = 'middle';
b.foreground = 5;
b.font_color = 5;
b.font_style = 5;
plot(n, y);
title('Unit Step Signal');
xlabel('Samples n');
ylabel('Amplitude');

// UNIT RAMP SIGNAL
z = [zeros(1, L), 0:L];
subplot(3, 4, 3);
c = gca();
c.y_location = 'middle';
c.foreground = 5;
c.font_color = 5;
c.font_style = 5;
plot(n, z);
title('Unit Ramp Signal');
xlabel('Samples n');
ylabel('Amplitude');

// EXPONENTIALLY INCREASING SEQUENCE
n = 0:1:10;
x = exp(n);
subplot(3, 4, 4);
d = gca();
d.x_location = 'origin';
d.y_location = 'origin';
d.foreground = 5;
d.font_color = 5;
d.font_style = 5;
plot(n, x);
title('Exponentially Increasing Sequence');
xlabel('Samples n');
ylabel('Amplitude');

// EXPONENTIALLY DECREASING SEQUENCE
n = 0:1:10;
x = exp(-n);
subplot(3, 4, 5);
e = gca();
e.x_location = 'origin';
e.y_location = 'origin';
e.foreground = 5;
e.font_color = 5;
e.font_style = 5;
plot(n, x);
title('Exponentially Decreasing Sequence');
xlabel('Samples n');
ylabel('Amplitude');

// SINE WAVE
t = 0:0.04:1;
x = sin(2 * %pi * t);
subplot(3, 4, 6);
f = gca();
f.foreground = 5;
f.font_color = 5;
f.font_style = 5;
plot(t, x);
title('Sine Wave');
xlabel('Samples n');
ylabel('Amplitude');

// COSINE WAVE
t = 0:0.04:1;
x = cos(2 * %pi * t);
subplot(3, 4, 7);
g = gca();
g.foreground = 5;
g.font_color = 5;
g.font_style = 5;
plot(t, x);
title('Cosine Wave');
xlabel('Samples n');
ylabel('Amplitude');
