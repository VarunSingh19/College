clear all;
clc;
close;
M = 30;
D = 2;//Decimation factor =2.
Wc = %pi/2; //Cutoff Frequency.
Wp = Wc/(2*%pi); //Passband Edge Frequency.
Ws = 0.31; // Stopband edgeb Frequency.
hn = eqfir(M,[0 Wp;Ws .5],[1 0],[2 1]);
disp("The LPF Filter Coefficients are :",hn);
// Obtaining Polyphase Filter Coenfficients from hn.
p = zeros(D,M/D);
for k = 1:D
    for n = 1:(length(hn)/D)
        p(k,n) = hn(D*(n-1)+k);
    end
end
disp("The Polyphase decimator for D = 2 are :",p);
