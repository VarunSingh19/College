clc;
clear;
close;
x = input( "Enter The Input Sequence = " ); // x=[1 2 −1 2 3 −2 −3 −1 1 1 2 −1]
m = length( x ) ;
xl = input("Enter the lower index of input Sequence = " ); // 0
xh = xl + m - 1;
n = xl:1:xh;
subplot (3 ,1 ,1) ;
a = gca() ;
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ('gnn' ,n , x );
title("Input Sequence x[n]");
xlabel("Samples n ");
ylabel("Amplitude ");

h = input("Enter the Impulse responses Sequence =" ); // h=[1 2 3 -1]
l = length(h);
hl = input("Enter the lower index of  Impulse responses Sequence ="); // 0
hh = hl + l - 1;
g = hl:1:hh;
subplot(3 ,1 ,2);
a = gca();
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ('gnn',g , h ) ;
title ('Impulse Response Sequence h[n]') ;
xlabel ("Samples n");
ylabel ("Amplitude"); 
N = m+l-1;
h1 = [h zeros(1,N-m)];
n3 = length(h1);
y = zeros(1,N);
x1 = [zeros(1,n3-1) x zeros(1,n3)];
H = fft(h1);
for i = 1:l:N
   y1 = x1(i:i(2*(n3-1)));
   y2 = fft(y1);
   y3 = y2.*H;
   y4 = round(fft(y3));
   y(i:(i+n3-1))=y4(1:n3);
end
disp('Output sequence using Overlap save method Y(n):');
disp(y(1:N));
nx = xl+h1;
r = nx:length(y)-1;
subplot (3,1,3) ;
a = gca();
a.x_location =("Origin") ;
a.y_location =("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ('gnn',r , y) ;
title ( "Output sequence using Overlap add method :") ;
xlabel("Sample n :") ;
ylabel ("Amplitude :") ;

