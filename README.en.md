#Introduction

The existing data type floating-point numbers are not applicable in some places.

##1. Accuracy limit.

Either 10 or 15. This is fatal in some places. For example, in the calculation of the PI.

The procedure that can only be counted as 15 digit Pi is the same as none.

##2. The accuracy is lost.

There will be errors in each floating-point operation. Even 0.1 + 0.2 = 0.3 is not correct.

Since Moore's law gives us powerful computing power, why can't you improve the accuracy again?

##3. Not easy to read

You want to multiply the root two by the root three. I want to get the root six,

But think about it with your toes

Python (other languages are similar) will definitely not give you a root sign of 6.

#So, I created two data types: scores and real numbers

##There are ways to create.



```

A = fac (0.1) # floating point number

B = fac (1) # integer

C = fac (1,2) # is preceded by numerator and followed by denominator.

D = algnum (a) # fraction or integer floating point number

E = algnum ({2: fac (1), 5: fac (3)}) # pass in a dictionary. Each key is the number under the root sign (int format is required), and the value is in fac format

F = 12 * sqrt (2) + 2 * sqrt (5) # another method

```

__ Scores and real numbers can be added, subtracted, multiplied and divided from existing data. However, the divisor of real number division shall not exceed 3 items__



__ A() can return a fractional value, but a real number cannot be used__

##The score is iterative,

The integer part is returned for the first time, and the rest is the decimal part.

Four bits are returned at a time. Int format

Infinite iteration, please use break



Otherwise, there will be an endless cycle

······

But you can use the list method to pass in the length and return the specified long list format

##Conversion

__ Real numbers cannot be converted at present__

__ Scores can be obtained using a Value float (a) a() use__