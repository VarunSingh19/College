// Aim :Time and Frequency Response of LTI system


// Caption: Program to generate and plot the impulse response and frequency
// response of a Linear Constant Coefficient First Order Differential Equation
clear;
clc;
close;

// [1]. Impulse response h(t) = exp(-a*t) * u(t), A>0
a = 1; // Constant coefficient a=1
Dt = 0.005;
t = 0: Dt: 10;
ht = exp(-a * t);
figure(1)
a = gca();
a.y_location = 'origin';
plot(t, ht);
xlabel('time t --->');
ylabel('h(t)');
title('Impulse Response of 1st Order Linear Constant Coeff. Diff. Equation');

// [2]. Finding Frequency response using Continuous Time Fourier Transform
Wmax = 2 *%pi* 1; // Analog Frequency = 1Hz
K = 4;
k = 0:(K / 1000): K;
W = k * Wmax / K;
HW = ht * exp(-sqrt(-1) * t' * W) * Dt;
HW_Mag = abs(HW);
W = [-mtlb_fliplr(W), W(2:1001)]; // Omega from -Wmax to Wmax
HW_Mag = [mtlb_fliplr(HW_Mag), HW_Mag(2:1001)];
[HW_Phase, db] = phasemag(HW);
HW_Phase = [-mtlb_fliplr(HW_Phase), HW_Phase(2:1001)];

figure(2)
// Plotting Magnitude Response
subplot(2, 1, 1);
a = gca();
a.y_location = 'origin';
plot(W, HW_Mag);
xlabel('Frequency in Radians/Seconds ---> W');
ylabel('abs(H(jW))');
title('Magnitude Response');

// Plotting Phase Response
subplot(2, 1, 2);
a = gca();
a.y_location = 'origin';
a.x_location = 'origin';
plot(W, HW_Phase *%pi / 180);
xlabel('Frequency in Radians/Seconds ---> W');
ylabel('<H(jW)');
title('Phase Response in Radians');
