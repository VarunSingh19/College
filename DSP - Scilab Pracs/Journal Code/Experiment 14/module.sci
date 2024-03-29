// Aim : WRITE A SCILAB PROGRAM TO DESIGN DIGITAL IIR CHEBYSHEW FILTER.

clc;
clear;
close;

wp = input('Enter the Digital Pass Band edge Frequency = '); // 0.2 * %pi
ws = input('Enter the Digital Stop Band edge Frequency = '); // 0.6 * %pi
t = input('Sampling Interval= '); // 1
del1 = input('Enter the Pass Band Ripple = '); // 0.8
del2 = input('Enter the Stop Band Ripple = '); // 0.2

disp(wp, 'Wp= ');
disp(ws, 'Ws= ');

del = sqrt(((1/del2)^2) - 1);
disp(del, 'Delta= ');

epsilon = sqrt(((1/del1)^2) - 1);
disp(epsilon, 'Epsilon= ');

N = acosh(del / epsilon) / acosh(ws / wp);
N = ceil(N);
disp(N, 'N= ');

wc = wp / ((((1/del1)^2) - 1)^(1/(2*N)));

[pols, gn] = zpch1(N, epsilon, wp);
hs = poly(gn, 's', 'coeff') / real(poly(pols, 's'));
z = poly(0, 'z');
hz = horner(hs, ((2/t) * ((z - 1) / (z + 1))));
hw = frmag(hz(2), hz(3), 512); // frequency response for 512 points
w = 0:%pi/511:%pi;

subplot(1, 1, 1);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(w/%pi, 20*log10(abs(hw)));
xgrid(1);
title('Magnitude Response of Digital Chebyshev LPF IIR Filter');
xlabel('Normalized Digital Frequency');
ylabel('Magnitude in dB');
