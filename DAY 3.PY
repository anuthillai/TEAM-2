arithmetic operators
  addition(+)
    result = 5 + 3  # result is 8
  subtraction(-)
    result = 10 - 4 # result is 6
  multiplication(*)
    result = 6 * 2  # result is 12
  division, returns a float(/)
    result = 7 / 2  # result is 3.5
  modulo, returns the remainder of the division(%)
    result = 7 % 2  # result is 1 (7 divided by 2 is 3 with a remainder of 1)
  exponentiation(**)
    result = 2 ** 3 # result is 8 (2 raised to the power of 3, or 2 * 2 * 2)
  floor division, returns the integer part of the division(//)
    result = 7 // 2 # result is 3

assingment operators   
  =,	x = 5,	x = 5	
 +=,	x += 3,	x = x + 3	
 -=,	x -= 3,	x = x - 3	
 *=,	x *= 3,	x = x * 3	
 /=,	x /= 3,	x = x / 3	
 %=,	x %= 3,	x = x % 3	
 //=,	x //= 3,	x = x // 3	
 **=,	x **= 3,	x = x ** 3	
 &=,	x &= 3,	x = x & 3	
 |=,	x |= 3,	x = x | 3	
 ^=,	x ^= 3,	x = x ^ 3	
 >>=,	x >>= 3,	x = x >> 3	
 <<=	x, <<= 3,	x = x << 3

comparison(rational) operators
  ==(Equal)	
   x == y	
  !=(Not equal)	
   x != y	
  >(Greater than)	
   x > y	
  <(Less than)	
   x < y	
  >=(Greater than or equal to)	
   x >= y	
  <=(Less than or equal to)	
   x <= y

logical operators
 and, Returns True if both statements are true,	
   x < 5 and  x < 10	
 or, Returns True if one of the statements is true,	
   x < 5 or x < 4	
 not, Reverse the result, returns False if the result is true,	
   not(x < 5 and x < 10)

identity operators
 is, Returns True if both variables are the same object,
     x is y	
 is not, Returns True if both variables are not the same object,
    x is not y

membership operators
 in, Returns True if a sequence with the specified value is present in the object,
        x in y	
 not in, Returns True if a sequence with the specified value is not present in the object,
        x not in y

bitwise operators
 &&(AND),	Sets each bit to 1 if both bits are 1,
      x && y	
 |(OR),	Sets each bit to 1 if one of two bits is 1,
      x | y	
 ^(XOR), Sets each bit to 1 if only one of two bits is 1,
      x ^ y	
 ~(NOT), Inverts all the bits
      ~x	
 <<(Zero fill left shift), Shift left by pushing zeros in from the right and let the leftmost bits fall off,
      x << 2	
 >>(Signed right shift), Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off,
      x >> 2
