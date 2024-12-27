# https://www.codewars.com/kata/65cdd06eac0d2ad8ee6c6067/train/python

nth_term_of_the_fibonacci_sequence=lambda n:pow(x:=2<<n,n+1,x*x+~x)%x

# too large length
nth_term_of_the_fibonacci_sequence=lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)
