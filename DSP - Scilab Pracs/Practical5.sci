// Finding autocorrelation and cross-correlation of sequences

x = [1 2 3 4]; // Sequence 1
y = [2 1 0 -1]; // Sequence 2
N = length(x);
M = length(y);

auto_corr_x = xcorr(x, x, 'biased'); // Autocorrelation of x
auto_corr_y = xcorr(y, y, 'biased'); // Autocorrelation of y

disp('Autocorrelation of x:')
disp(auto_corr_x)
disp('Autocorrelation of y:')
disp(auto_corr_y)

cross_corr_xy = xcorr(x, y, 'biased'); // Cross-correlation between x and y

disp('Cross-correlation between x and y:')
disp(cross_corr_xy)


