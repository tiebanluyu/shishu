# README

The existing data type floating-point numbers are not applicable in some places.

## 1. Accuracy limit.

Either 10 or 15. This is fatal in some places. For example, in the calculation of the PI.

The procedure that can only be counted as 15 digit Pi is the same as none.

## 2. The accuracy is lost.

There will be errors in each floating-point operation. Even 0.1 + 0.2 == 0.3 is not correct.

Since Moore's law gives us powerful computing power, why can't you improve the accuracy again?

## 3. Not easy to read

You want to multiply the root two by the root three. I want to get the root six,

But think about it with your mind

Python(other languages are similar) will definitely not give you a root sign of six.

# So lots of developers create various resolvent.So as me. 


## There are ways to create.



```


A = Algnum (a) # fraction , integer or floating point number

B = Algnum ({2: fraction(1), 5: fraction(3)}) 
 
pass in a dictionary. 
Each key is the number under the root sign (int format is required).
and the value is in Fraction format.

C = 12 * sqrt (2) + 2 * sqrt (5) # another method

```

__  real numbers can be added, subtracted, multiplied and divided . But the divisor of real number division shall not exceed 3 items__










