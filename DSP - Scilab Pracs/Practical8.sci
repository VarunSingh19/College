// Ca p tio n : Program to D e sig n FIR Low Pa s s F i l t e r
clear;
clc ;
close ;
M = input ( "enter the odd filter length = " ) ;

// F i l t e r l e n g t h
Wc = input ( "Enter the Digital cut off frequency =" ) ;

// D i g i t a l C u t off f r e q u e n c y
Tuo = (M -1) /2 // C e n t e r Value
for n = 1: M
     if ( n == Tuo +1)
        hd ( n) = Wc / %pi ;
     else
        hd ( n) = sin( Wc *(( n -1) - Tuo ) ) /((( n -1) - Tuo ) * %pi )
             ;
      end
  end
// Rectangular Window
for n = 1: M
    W ( n ) = 1;
end

//Windowing Filter Coefficiets
h = hd .* W ;
disp (h , "Filter Coefficiet are : " );
[ hzm , fr ]= frmag (h ,256);
hzm_dB = 20* log10 ( hzm ) ./ max ( hzm );
subplot (2 ,1 ,1);
plot (2* fr , hzm );
xlabel( " Normalized Digital Frequency W" );
ylabel ( " Magnitude " ) ;
title( " Frequency Response 0f FIR LPF using Rectangular window " );
xgrid (1);
subplot (2 ,1 ,2);
plot (2* fr , hzm_dB );
xlabel( " Normalized Digital Frequency W" );
ylabel( " Magnitude in dB " ) ;
title( " Frequency Response 0f FIR LPF using Rectangular window " );
xgrid (1)
