clear;
clc;
close;
// Analog Singnal
A = 1; // Amplitude
Dt = 0.005;
t = -2:Dt:2;
//Continous Time Signal
xa = exp(-A*abs(t));
//Discrete Time Signal
Fs = input("Enter the Sampling Frequency in Hertz :");
// Fs = 1Hz, 2Hz, 3Hz,20Hz,100Hz.
Ts = 1/Fs;
nTs = -2:Ts:2;
x = exp(-A*abs(nTs));
// Analog Signal reconstruction 
Dt = 0.005;
t = -2:Dt:2;
Xa = x*sinc(Fs*(ones(length(nTs),1)*t-nTs*ones(1,length(t))));
//Plotting the original signal and reconstructed signal.
subplot(2,1,1);
a = gca();
a.x_location = "Origin";
a.y_location = "Origin";
plot(t,xa);
xlabel('t in sec');
ylabel('xa(t)');
title('Original Analog Signal ');
subplot(2,1,2);
a = gca();
a.x_location = "origin";
a.y_location = "origin";
plot(t,xa);
xlabel('t in sec');
ylabel('xa(t)');
title("Original Analog Signal");
subplot(2,1,2);
a = gca();
a.x_location = "origin";
a.y_location = "origin";
xlabel('t in sec');
ylabel('xa(t)');
title('Reconstructed Signal using sinc Function, Fs = 100Hz');
plot(t,Xa);








