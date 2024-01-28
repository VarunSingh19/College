// Generating common discrete-time signals

n = 0:20; // Time indices

// Unit impulse signal
delta = [zeros(1,5), 1, zeros(1,15)];

// Unit step signal
u = [zeros(1,5), ones(1,16)];

// Exponential signal
a = 0.9; // Exponential decay factor
x_exp = a .^ n;

// Sinusoidal signal
f = 0.1; // Frequency of the sinusoid
x_sin = sin(2*%pi*f*n);

// Displaying signals
subplot(2,2,1)
plot(n, delta)
title('Unit Impulse Signal')

subplot(2,2,2)
plot(n, u)
title('Unit Step Signal')

subplot(2,2,3)
plot(n, x_exp)
title('Exponential Signal')

subplot(2,2,4)
plot(n, x_sin)
title('Sinusoidal Signal')

