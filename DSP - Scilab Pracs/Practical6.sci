x = input ( "Enter The Input Sequence = " ) // x =[1 2 3 1 ]
m = length ( x ) ;
xl = input ( "Enter the lower index of input Sequence = " ); // 0
xh = xl +m -1;
n = xl :1: xh ;
subplot (2 ,2 ,1) ;
a = gca () ;
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 (' gnn ' ,n , x ) ;
title ( "Input Sequence x[n]"  ) ;
xlabel ( "Sample n ") ;
ylabel ( "Amplitude "  ) ;

h = input ( "Enter the Impulse responses Sequence =" ) ; 
// h=[1 2 1 1 ]
l = length ( h ) ;
hl = input (  "Enter the lower index of  Impulse responses Sequence ="  ) ; // 0
hh = hl +l -1;
g = hl :1: hh ;
subplot (2 ,2 ,2) ;
a = gca () ;
a.x_location = ' o r i g i n' ;
a.y_location = ' o r i g i n ' ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ( ' gnn ' ,g , h ) ;
title ( ' I m p u l s e R e s p o n s e S e q u e n c e h [ n ] ' ) ;
xlabel ( ' S a m p l e s n ' ) ;
ylabel ( ' A m p l i t u d e ' ) ;
// A u t o c o r r e l a t i o n
y = xcorr (x , x ) ;
disp ( ' Auto C o r r e l a t i o n Of g i v e n S e q u e n c e y ( n )= ' ) ;
disp ( y ) ;
nx = xl + xl ;
nh = xh + xh ;
r = nx : nh ;
subplot (2 ,2 ,3) ;
a = gca () ;
a.x_location = ("Origin") ;
a.y_location = ("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ( ' gnn ' ,r , y ) ;
title ( "Output of auto Correlation of sequence :") ;
xlabel ("Sample n ") ;
ylabel ("Amplitude ") ;
// C r o s s c o r r e l a t i o n
z = xcorr (x , h ) ;
disp ("Cross Correlation of Sequence y(n) =" ) ;
disp ( z ) ;
subplot (2 ,2 ,4) ;
a = gca () ;
a.x_location =("Origin") ;
a.y_location =("Origin") ;
a.foreground = 5;
a.font_color = 5;
a.font_style = 5;
plot2d3 ( ' gnn ' ,r , z ) ;
title ( "Output of cross Correlation of sequence :") ;
xlabel("Sample n ") ;
ylabel ("Amplitude ") ;

//INPUT :
// Enter t h e I n p u t S e q u e n c e =[1 2 3 1 ]
// E n t e r t h e l o w e r i n d e x o f I n p u t S e q u e n c e =0
// E n t e r t h e I m p u l s e r e s p o n s e S e q u e n c e =[1 2 1 1 ]
// E n t e r t h e lower index of impulse response Sequence = 0
