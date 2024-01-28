// Computing linearity property of a given signal

// Define two signals
n = 0:10; // Time indices
x1 = rand(1, 11); // First random signal
x2 = rand(1, 11); // Second random signal

a = 2; // Scaling factor

// Applying linearity property: a * x1[n] + a * x2[n] = a * (x1[n] + x2[n])

// Compute left side: a * x1[n] + a * x2[n]
left_side = a * x1 + a * x2;

// Compute right side: a * (x1[n] + x2[n])
right_side = a * (x1 + x2);
// Check if both sides are equal (within a small tolerance)
if norm(left_side - right_side, 1) < 1e-10 then
    disp('The signal exhibits linearity property.')
else
    disp('The signal does not exhibit linearity property.')
end

