// Aim : WRITE A SCILAB PROGRAM FOR DESIGNING OF FIR FILTER FOR LOW PASS, HIGH PASS, BANDPASS AND BAND REJECT RESPONSES


clc;
clear;
close;
//xdel(winsid());

fc1 = input('Enter the analog cutoff Frequency in Hz= '); // 250
fc2 = input('Enter an analog higher cutoff frequency in Hz= '); // 600
fs = input('Enter the analog sampling Frequency in Hz= '); // 2000
M = input('Enter order of filter = '); // 4

w1 = (2 *%pi) * (fc1 / fs);
w2 = (2 *%pi) * (fc2 / fs);

// FIR LOW PASS FILTER
disp('DESIGNING OF FIR LOW PASS FILTER :');
disp(w1, 'Digital Cutoff Frequency in radians cycles/samples');
wc1 = w1 /%pi;
disp(wc1, 'Normalized digital cutoff frequency in cycles/samples');
[wft, wfm, fr] = wfir('lp', M + 1, [wc1 / 2, 0], 're', [0, 0]);
disp(wft, 'Impulse Response of LPF FIR filter: h(n)=');

// Plotting magnitude response of LPF filter
subplot(2, 4, 1);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * fr, wfm);
title('Magnitude Response of FIR LPF');
xlabel('Normalized Digital Frequency w');
ylabel('Magnitude |H(w)|');
xgrid(1);

subplot(2, 4, 2);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(fr * fs, wfm);
title('Magnitude Response of FIR LPF');
xlabel('Analog frequency in Hz f');
ylabel('Magnitude |H(w)|');
xgrid(1);

// FIR HIGH PASS FILTER
disp('DESIGNING OF FIR HIGH PASS FILTER :');
disp(w1, 'Digital Cutoff Frequency in radians cycles/samples');
wc1 = w1 /%pi;
disp(wc1, 'Normalized digital cutoff frequency in cycles/samples');
[wft, wfm, fr] = wfir('hp', M + 1, [wc1 / 2, 0], 're', [0, 0]);
disp(wft, 'Impulse Response of HPF FIR filter: h(n)=');

// Plotting magnitude response of HPF filter
subplot(2, 4, 3);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * fr, wfm);
title('Magnitude Response of FIR HPF');
xlabel('Normalized Digital Frequency w');
ylabel('Magnitude |H(w)|');
xgrid(1);

subplot(2, 4, 4);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(fr * fs, wfm);
title('Magnitude Response of FIR HPF');
xlabel('Analog frequency in Hz f');
ylabel('Magnitude |H(w)|');
xgrid(1);

// FIR BAND PASS FILTER
disp('DESIGNING OF FIR BAND PASS FILTER :');
disp(w1, 'Digital lower cutoff frequency in radians cycles/samples');
disp(w2, 'Digital higher cutoff frequency in radians cycles/samples');
wc1 = w1 /%pi;
wc2 = w2 /%pi;
disp(wc1, 'Normalized digital lower cutoff frequency in cycles/samples');
disp(wc2, 'Normalized digital higher cutoff frequency in cycles/samples');
[wft, wfm, fr] = wfir('bp', M + 1, [wc1 / 2, wc2 / 2], 're', [0, 0]);
disp(wft, 'Impulse response of Bandpass Filter FIR filter: h(n)=');

// Plotting the magnitude response of BPF filter
subplot(2, 4, 5);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * fr, wfm);
xlabel('Normalized Digital Frequency w');
ylabel('Magnitude |H(W)|');
title('Magnitude Response of FIR BPF');
xgrid(1);

subplot(2, 4, 6);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(fr * fs, wfm);
xlabel('Analog Frequency in Hz f');
ylabel('Magnitude |H(w)|');
title('Magnitude Response of FIR BPF');
xgrid(1);

// FIR BAND REJECT FILTER
disp('DESIGNING OF FIR BAND REJECT FILTER :');
disp(w1, 'Digital lower cutoff frequency in radians cycles/samples');
disp(w2, 'Digital higher cutoff frequency in radians cycles/samples');
wc1 = w1 /%pi;
wc2 = w2 /%pi;
disp(wc1, 'Normalized digital lower cutoff frequency in cycles/samples');
disp(wc2, 'Normalized digital higher cutoff frequency in cycles/samples');
[wft, wfm, fr] = wfir('sb', M + 1, [wc1 / 2, wc2 / 2], 're', [0, 0]);
disp(wft, 'Impulse response of Band reject filter FIR filter: h(n)=');

// Plotting the magnitude response of BRF filter
subplot(2, 4, 7);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(2 * fr, wfm);
xlabel('Normalized Digital Frequency w');
ylabel('Magnitude |H(W)|');
title('Magnitude Response of FIR BRF');
xgrid(1);

subplot(2, 4, 8);
a = gca();
a.thickness = 2;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot(fr * fs, wfm);
xlabel('Analog Frequency in Hz f');
ylabel('Magnitude |H(w)|');
title('Magnitude Response of FIR BRF');
xgrid(1);
