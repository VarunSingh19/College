// Aim :WRITE A SCILAB PROGRAM TO COMPUTE CIRCULAR CONVOLUTION OF TWO SEQUECNES USING BASIC EQUATION.

clc;
clear;
close;
x = input( "Enter The Input Sequence = " ); // x =[1 1 2 2 ]
m = length( x ) ;
xl = input ( "Enter the lower index of input Sequence = " ); // 0
xh = xl +m -1;
n = xl:1:xh ;
subplot (3 ,1 ,1) ;
a = gca() ;
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ('gnn' ,n , x ) ;
title ("Input Sequence x[n]");
xlabel ("Sample n ");
ylabel ("Amplitude ");

h = input("Enter the Impulse responses Sequence =" ); // h=[1 2 3 4]
l = length(h);
h1 = input("Enter the lower index of  Impulse responses Sequence ="); // 0
hh = h1 +l - 1;
g = h1:1: hh;
subplot (3 ,1 ,2) ;
a = gca () ;
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ( 'gnn' ,g , h ) ;
title ('Impulse Response Sequence h[n]') ;
xlabel ("Samples n");
ylabel ("Amplitude");
// for making length of both signals 
N = max(m,1);
p = m-1;
if(p>=0) then
    h = [h,zeros(1,p)];
else
    x = [x,zeros(1,-p)];
end
for i = 1:N
    y(i) = 0;
    for j =1:N
        k=i-j+1;
        if(k<=0)
            k = N+k;
        end
        y(i)= y(i)+x(j)*h(k);0
    end
end

disp('Circular convolution by equation is y[n]:');
disp(y);
nx = xl+h1;
r = nx:length(y)-1;
subplot (3,1,3) ;
a = gca () ;
a.x_location =("Origin") ;
a.y_location =("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ( 'gnn' ,r , y ) ;
title ( "Output Response Sequence of Circular Convolution y[n] using Basic Equation :") ;
xlabel("Sample n ") ;
ylabel ("Amplitude ") ;


