// Aim :WRITE A SCILAB PROGRAM TO DESIGN DIGITAL IIR BUTTERWORTH LOW PASS FILTER.


clc;
clear;
close;
// xdel(winsid());

fc = input('Enter cutoff frequency in Hz fc= '); // 1000
fs = input('Enter sampling frequency in Hz fs= '); // 10000

N = input('Enter order of Butterworth filter N= '); // 4
Fp = 2 * fc / fs;
[Hz] = iir(N, 'lp', 'butt', [Fp/2, 0], [0, 0]);
[Hw, w] = frmag(Hz, 256);

subplot(2, 1, 1);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * w, abs(Hw));
title('Magnitude Response of IIR LPF');
xlabel('Normalized Digital Frequency w');
ylabel('|H(w)|');
xgrid(1);

subplot(2, 1, 2);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * w * fs, abs(Hw));
title('Magnitude Response of IIR LPF');
xlabel('Analog Frequency in Hz f');
ylabel('|H(w)|');
xgrid(1);

