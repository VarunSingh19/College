clear all;
clc;
close;
N = 8; //8-point FFT
x = [1,0,2,0,3,1,0,2]; //given discrete sequence 
X = fft(x,-1); // 8- points FFT of given discrete sequence
Pxx = (1/N)*(abs(X).^2); //Peridogram Estimate
disp(X,"DFT of x(n) is X(k)= ");
disp(Pxx,"Peridogram of x(n) is Pxx(k/N)=");
figure(1);
a = gca();
a.data_bounds = [0,0;8,11];
plot2d3("gnn" ,[1:N],Pxx);
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
title("Peridogram Estimate");
xlabel("Discrete Frequency Variable k ---->");
ylabel("Periodogram Pxx (k /N) ------>");
