clear all;
clc;
close;
s = poly(0,'s');
Omegac = 0.2*%pi; //Cutoff Frequency
H = Omegac/(s+Omegac); //Analog first order Butterworth filter transfer function
T = 1; //Sampling period T =1 Second
z = poly(0,'z');
Hz = horner(H,(2/T)*((z-1)/(z+1))); // Bilinear Transformation.
HW = frmag(Hz(2),Hz(3),512); //Frequency response for 512 points.
w = 0:%pi/511:%pi;
a = gca();
a.thickness = 1;
plot(W/%pi,HW,'r');
a.foreground = 1;
a.font_style = 9;
xgrid(1);
xtitle("Magnitude Response of Single pole LPF filter Cutoff Frequency = 0.2*pi","Normalized Digital Frequency --->","Magnitude");
