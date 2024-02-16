program = '''Write a program that reads two numbers A and B , and prints
the remainder when A is divided by B .
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer that is the
remainder when A is divided by B .
Explanation
For example, if the given numbers are A  10 and B  3 ,
The remainder is 1 when 10 is divided by 3.
The output should be 1.
Sample Input 1
10
3
Sample Output 1
1
Sample Input 2
24
5
Sample Output 2
4
'''

print(program)
a = int(input("Enter the A value : "))
b = int(input("Enter the B value : "))

print(a%b)
# -------------------------------------------------------------------------------------

program = '''Write a program that reads a number N and checks if the number
N is divisible by 7.
Print Divisible by Seven if N is divisible by 7. Otherwise, print
Not Divisible by Seven.
    Note
A Number N is divisible by 7, if the remainder is 0 when N
is divided by 7.
Example:
35 is divisible by 7. (Remainder is 0 when 35 is divided by 7)
27 is not divisible by 7. (Remainder is 6 (not 0) when 27 is divided
by 7)

Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a string. Divisible by
Seven should be printed if the number is divisible by 7. Otherwise,
Not Divisible by Seven should be printed.
Explanation
For example, if the given number N  35 ,
The remainder is 0 when 35 is divided by 7.
The output should be Divisible by Seven.
Sample Input 1
35
Sample Output 1
Divisible by Seven
Sample Input 2
8
Sample Output 2
Not Divisible by Seven
'''

print(program)
n = int(input("Enter a number : "))
remainder = n%7
Divisible = remainder == 0

if Divisible:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")

# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B and prints the
Quotient and Remainder when A is divided by B .
    Note
For Example, if 5 is divided by 2 (5/2),
Divisor <-- 2  5  2 --> Quotient
4
---------
1 --> Remainder
Quotient is 2 Quotient should be an integer).
Remainder is 1
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The first line of output should be an integer that is the Quotient.
The second line of output should be an integer that is the Remainder.
Explanation
For example, if the given numbers are A  5 and B  2 ,
The Quotient is 2 when 5 is divided by 2.
The Remainder is 1 when 5 is divided by 2.
The output should be,
Sample Input 1
5
2
Sample Output 1
2
1
Sample Input 2
30
10
Sample Output 2
3
0
'''
print(program)
divident = int(input("Enter Divident value : "))
divisor = int(input("Enter Divisor value : "))
Quotient = divident//divisor
Remainder = divident%divisor
print(Quotient)
print(Remainder)
# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if N is
divisible by 2.
Print Even if N is divisible by 2. Otherwise, print Odd.
    Note
A Number N is divisible by 2, if the remainder is 0 when N
is divided by 2.
Example:
4 is divisible by 2. (Remainder is 0 when 4 is divided by 2)
3 is not divisible by 2. (Remainder is 1 (not 0) when 3 is divided by
2)

Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a string. Even should
be printed if N is divisible by 2. Otherwise, Odd should be
printed

Explanation
For example, if the given number is N  4 ,
The remainder is 0 when 4 is divided by 2.
The output should be Even.
For example, if the given number is N  3 ,
The remainder is 1 (not 0) when 3 is divided by 2.
The output should be Odd.
Sample Input 1
4
Sample Output 1
Even
Sample Input 2
3
Sample Output 2
Odd

'''
print(program)
a = int(input("Enter a number : "))
remainder = a%2
even = remainder == 0
if even:
    print("Even")
else:
    print("odd")

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and finds the,
Remainder when N is divided by 4.
Remainder when N is divided by 5.
Print the greatest remainder among the two remainders when N is
divided by 4 and 5.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer that is the
greatest remainder among the two remainders when N is divided
by 4 and 5.
Explanation
For example, if the given number is N  12 ,
The remainder is 0 when N is divided by 4.
The remainder is 2 when N is divided by 5.
The greatest remainder among the two remainders 0 and 2 is 2.
The output should be 2.
Sample Input 1
12
Sample Output 1
2
Sample Input 2
147
Sample Output 2
3
'''
print(program)
n = int(input("Enter a value : "))
remainder_of_4 = n%4
remainder_of_5 = n%5
greatest = remainder_of_4 > remainder_of_5

if greatest:
    print(remainder_of_4)
else:
    print(remainder_of_5 ) 

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if the
remainder is 0 or 1 when N is divided by 11.
Print Special Eleven if the remainder is 0 or 1 when N is divided
by 11. Otherwise, print Normal Number.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a string. Special
Eleven should be printed if the remainder is 0 or 1 when N is
divided by 11. Otherwise, Normal Number should be printed.
Explanation
For example, if the given number is N  22 ,
The output should be Special Eleven as the remainder is 0 when
N is divided by 11.
For example, if the given number is N  23 ,
The output should be Special Eleven as the remainder is 1 when
N is divided by 11.
Sample Input 1
22
Sample Output 1
Special Eleven
Sample Input 2
23
Sample Output 2
Special Eleven
Sample Input 3
15
Sample Output 3
Normal Number
'''
print(program)
n = int(input("Enter a value : "))
remainder = n%11
Special_11 = (remainder ==0) or (remainder ==1)
if Special_11:
    print("Special Eleven")
else:
    print("Normal Number") 

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a two-digit number N and checks if
N is divisible by both the digits of N .
Print the double of N if N is divisible by both the digits of N .
Otherwise, print N .
    Note
The double of N is calculated as N * 2 .
Example: N  15
The double of 15 is 30 ( 15 * 2  30 ).
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer. The double
of N should be printed if N is divisible by both the digits of
N . Otherwise, N should be printed.
Explanation
For example, if the given number is N  15 ,
For example, if the given number is N  15 ,
The digits of N are 1 and 5.
✔ N is divisible by 1. (15 is divisible by 1)
✔ N is divisible by 5. (15 is divisible by 5)
As N is divisible by both the digits of N , print the double of
N .
The output should be 30 as the double of N is 30 ( 15  2  30 )
For example, if the given number is N  26 ,
The digits of N are 2 and 6.
✔ N is divisible by 2. (26 is divisible by 2)
✖ N is divisible by 6. (26 is not divisible by 6)
As N is not divisible by both the digits of N , print N .
The output should be 26.
Sample Input 1
15
Sample Output 1
30
Sample Input 2
26
Sample Output 2
26

'''

print(program)
num = input("enter a two digit number : ")

first_num = int(num[0])
second_num = int(num[1])

first_num_is_divisible_by_num = (int(num)%first_num) == 0
second_num_is_divisible_by_num = (int(num)%second_num) == 0

if first_num_is_divisible_by_num and second_num_is_divisible_by_num:
    print(int(num)*2)
else:
    print(int(num))


# -------------------------------------------------------------------------------------
program = '''Write a program that reads a two-digit number N and checks if
any of the given conditions is satisfied.
The number N is divisible by 9.
One of the digits of the number N is equal to 9
Print Lucky Number if any of the given conditions is satisfied.
Otherwise, print Unlucky Number.
    Note
The number N is divisible by 9, if the remainder is 0 when
N is divided by 9.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a string. Lucky
Number should be printed if any of the given conditions is satisfied.
Otherwise, Unlucky Number should be printed.
Explanation
For example, if the given number is N  18 ,
✔ The number N is divisible by 9. (18 is divisible by 9)
✖ One of the digits of the number N is equal to 9. (1, 8 are not
equal to 9)
The output should be Lucky Number as one of the given conditions
is satisfied.
Sample Input 1
18
Sample Output 1
Lucky Number
Sample Input 2
13
Sample Output 2
Unlucky Number
'''

print(program)
num = input("enter a two digit number : ")

first_digit = (int(num[0])) == 9
second_digit =(int(num[1])) == 9
num_divisible_by_9 = (int(num)%9) == 0

if first_digit or second_digit or num_divisible_by_9:
    print("Lucky Number")
else: print("Unlucky Number")


# -------------------------------------------------------------------------------------
program = '''Write a program that reads a string S and checks if all the given
conditions are satisfied.
The first three characters of S is NXT.
The remaining characters of S contain a Number. Number is divisible by
2 or 7.
Print Special String if all the given conditions are satisfied.
Otherwise, print Not a Special String.
    Quick Tip
Make sure the number is converted to an integer before doing
any operations like Division ( / ), Remainder ( % ), etc.
Example: S  NXT1234
The number in NXT1234 is 1234.
1234 should be converted to an integer before doing any operations
Input
The input will be a single line containing a string representing S .
Output
The output should be a single line containing a string. Special
String should be printed if all the given conditions are satisfied.
Otherwise, Not a Special String should be printed.
Explanation
For example, if the given string is A  NXT1234 ,
✔ The first three characters of S is NXT. The first three
characters of NXT1234 is equal to NXT)
✔ The remaining characters of S is divisible by 2 or 7. The
remaining characters of NXT1234 is 1234. 1234 is divisible by 2)
The output should be Special String as all the given conditions are
satisfied.
Sample Input 1
NXT1234
Sample Output 1
Special String
Sample Input 2
PRA49
Sample Output 2
Not a Special String
'''
print(program)
alpha_num = input("enter a alphanumeric(1st 3 should be alphabetics) value: ")

first_three_alpha_is_nxt = (alpha_num[:3]).upper() == 'NXT'
remain_nums_divisible_by_2 = (int(alpha_num[3:])%2) == 0
remain_nums_divisible_by_7 = (int(alpha_num[3:])%2) == 0
if first_three_alpha_is_nxt and (remain_nums_divisible_by_2 or remain_nums_divisible_by_7):
    print("Special String")
else: print("Not a Special String")


# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B , and checks
if all the given conditions are satisfied.
A and B are divisible by 3.
A or B is divisible by 12.
Print Pair if all the given conditions are satisfied. Otherwise, print
Not a Pair.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Pair should be
printed if all the given conditions are satisfied. Otherwise, Not a Pair
should be printed.
Explanation
For example, if the given numbers are A  15 and B  240 ,
✔ A and B are divisible by 3. (15 and 240 are divisible by 3)
✔ A or B is divisible by 12. (240 is divisible by 12)
The output should be Pair as all the given conditions are satisfied.
Sample Input 1
15
240
Sample Output 1
Pair
Sample Input 2
360
7
Sample Output 2
Not a Pair
'''

print(program)
num_a = int(input('Enter a number :'))
num_b = int(input('Enter another number : '))

num_a_divisible_by_3 = (num_a % 3) == 0
num_b_divisible_by_3 = (num_b % 3) == 0
num_a_divisible_by_12 = (num_a % 12) == 0
num_b_divisible_by_12 = (num_b % 12) == 0

if (num_a_divisible_by_3 and num_b_divisible_by_3) and (num_a_divisible_by_12 or num_b_divisible_by_12):
    print("Pair")
else: print("Not a Pair")
  

# -------------------------------------------------------------------------------------
program = '''Write a program to print if the given number is divisible by any of the
lucky numbers 6, 3, 2 in decreasing order of priority(6 is luckier than
3 and 3 is luckier than 2.
Print "Number is divisible by" followed by the luckiest number among
the above 3 which can divide the number.
Print "Number is not divisible by 2, 3 or 6" if the number is not
divisible by any of them.
Input
The input will be a single line containing a positive number.
Output
If the given number is divisible by 6, print "Number is divisible by 6".
If the given number is divisible by 3, print "Number is divisible by 3".
If the given number is divisible by 2, print "Number is divisible by 2".
In all other cases print "Number is not divisible by 2, 3 or 6".
Explanation
In the example 126 is divisible by 2, 3 and 6
But 6 takes precedence because 6 is luckiest amongst the three. So
the output should be "Number is divisible by 6"
Sample Input 1
126
Sample Output 1
Number is divisible by 6
Sample Input 2
27
Sample Output 2
Number is divisible by 3
Sample Input 3
55
Sample Output 3
Number is not divisible by 2, 3 or 6
'''
print(program)
num = int(input("Enter a number : "))

num_is_divisible_by_6 = (num%6) == 0
num_is_divisible_by_3 = (num%3) == 0
num_is_divisible_by_2 = (num%2) == 0
lucky_num = True
if lucky_num and num_is_divisible_by_6:
    print("Number is divisible by 6")
    lucky_num = False
if lucky_num and num_is_divisible_by_3:
    print("Number is divisible by 3")
    lucky_num = False
if lucky_num and num_is_divisible_by_2:
    print("Number is divisible by 2")
    lucky_num = False
if lucky_num:
    print("Number is not divisible by 2, 3 or 6")

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a two-digit number N and checks if
any of the given conditions is satisfied.
The sum of digits of N is equal to 7.
One of the digits of N is equal to 7.
N is divisible by 7.
Print Special Number if any of the given conditions is satisfied.
Otherwise, print Normal Number.
Input
The input will be a single line containing a two-digit integer
representing N .
Output
The output should be a single line containing a string. Special
Number should be printed if any of the given conditions is satisfied.
Otherwise, Normal Number should be printed.
Explanation
For example, if the given two-digit number is N  67
✖ The sum of digits of N is equal to 7. ( 6  7  13 , 13 is not
equal to 7)
✔ One of the digits of N is equal to 7. (6, 7 are digits of 67. 7 is
equal to 7)
✖ N is divisible by 7. (67 is not divisible by 7)
The output should be Special Number as one of the given
conditions is satisfied.
Sample Input 1
67
Sample Output 1
Special Number
Sample Input 2
36
Sample Output 2
Normal Number

'''
print(program)
N = input(("Enter a tow-digit number : "))
first_num,second_num = int(N[0]), int(N[1])
sum_of_n = first_num + second_num
sum_of_n_is_equal_to_7 = sum_of_n == 7
first_num_equal_to_7 = int(first_num) == 7
second_num_equal_to_7 = int(second_num) == 7
N_devisible_by_7 = (int(N) %7) == 0
if sum_of_n_is_equal_to_7 or first_num_equal_to_7 or second_num_equal_to_7 or N_devisible_by_7:
    print("Special Number")
else: print("Normal Number")


# -------------------------------------------------------------------------------------
program = '''Write a program that reads a distance D in km and calculates the
score.
If D is less than or equal to 10, the score is D .
If D is greater than 10, the score is the sum of 10 and (D  10) * 3 .
Input
The input will be a single line containing an integer representing D .
Output
The output should be a single line containing an integer that is the
score.
Explanation
For example, if the given distance is D  3 ,
3 is less than or equal to 10
The score is 3 ( D )
The output should be 3.
For example, if the given distance is D  25 ,
25 is greater than 10.
The score is the sum of 10 and (D  10) * 3 .
    10 + (D - 10) * 3
    10 + (25 - 10) * 3
    10 + (15) * 3
    10 + 45
    55
The output should be 55
Sample Input 1
3
Sample Output 1
3
Sample Input 2
25
Sample Output 2
55

'''
print(program)
d = int(input("Enter a number : "))
d_less_and_equal_10 = d<=10
d_greater_10 = d>10
if d_greater_10:
    print(10 + (d - 10) * 3)
else: print(d)


# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and prints the Cube of
N (N
3
).
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer that is the
Cube of N (N
3).
Explanation
For example, if the given number is N  4 ,
The Cube of N is 64 (4
3  64).
The output should be 64.
Sample Input 1
4
Sample Output 1
64
Sample Input 2
10
Sample Output 2
1000
'''
print(program)

N = int(input("Enter a number : "))
print(N**3)
# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and an exponent E and
prints the result of N power E (N
E
).
Input
The first line of input contains an integer representing the number
N .
The second line of input contains an integer representing the
exponent E .
Output
The output should be a single line containing an integer that is the
result of N power E (N
E).
Explanation
For example, if the given number is N  3 and the exponent is E
2 ,
The result of N power E is 9. (3
2  9)
The output should be 9.
For example, if the given number is N  5 and the exponent is E
3 ,
The result of N power E is 125. (5
3  125)
The output should be 125.
Sample Input 1
3
2
Sample Output 1
9
Sample Input 2
5
3
Sample Output 2
125
'''
print(program)
N = int(input("Enter a number : "))
E = int(input("enter the exponent : "))
print(N**E)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and prints the Square
Root of N .
    Note
To calculate the Square Root of N , use the N power 0.5
(N
0.5
).

Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a float that is the
Square Root of N .
Explanation
For example, if the given number is N  4 ,
The Square Root of N is 2.0 (4
0.5  2.0).
The output should be 2.0.
Sample Input 1
4
Sample Output 1
2.0
Sample Input 2
100
Sample Output 2
10.0
'''
print(program)
N = int(input("Enter a number to find square root of it : "))
print(N**0.5)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B , and checks
if A
2  B
2
(sum of the square of A and the square of B ) is
greater than or equal to 60.
Print Greater than or Equal to 60 if the sum of the square of A
and the square of B is greater than or equal to 60. Otherwise,
print Less than 60.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Greater than
or Equal to 60 should be printed if A
2  B
2
is greater than or
equal to 60. Otherwise, Less than 60 should be printed.
Explanation
For example, if the given numbers are A  10 and B  2 ,
The square of A is 100 (10
2
).
The square of B is 4 (2
2).
The sum of the square of A and the square of B is 104 ( 100 + 4 =
104 ).
104 (sum of the square of A and the square of B ) is greater than or
equal to 60.
The output should be Greater than or Equal to 60.
Sample Input 1
10
2
Sample Output 1
Greater than or Equal to 60
Sample Input 2
1
3
Sample Output 2
Less than 60

'''

print(program)
n1 = int(input("enter n1 value : "))
n2 = int(input("Enter n2 value : "))

sum_quare = (n1**2) + (n2**2)

sum_quare_is_grater_than_60 = sum_quare >=60
if sum_quare_is_grater_than_60:
    print("Greater than or Equal to 60")
else: print("Less than 60")

# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B and finds the,
Result of A power B (A
B
)
Result of B power A (B
A)
Print the greatest among the results of A power B (A
B
) and
B power A (B
A).
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer. The result of
A
B should be printed if A
B is greater than B
A. Otherwise, the result
of B
A should be printed.
Explanation
For example, if the given two numbers are A  2 and B  3 ,
Result of A power B (A
B
) is 8. (2
3  8)
Result of B power A (B
A) is 9. (3
2  9)
Greatest among the two results is 9. (9 is greater than 8)
The output should be 9.
Sample Input 1
2
3
Sample Output 1
9
Sample Input 2
3
1
Sample Output 2
3

'''
print(program)
n1 = int(input("enter n1 value : "))
n2 = int(input("Enter n2 value : "))
n1_power_n2, n2_power_n1 = n1**n2, n2**n1
n1_power_greater_n2 = n1_power_n2 > n2_power_n1
if n1_power_greater_n2:
    print(n1_power_n2)
else: print(n2_power_n1)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if the last digit
of N is equal to the last digit of the square of N .
Print Equal if the last digit of N is equal to the last digit of the
square of N . Otherwise, print Not Equal.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a string. Equal should
be printed if the last digit of N is equal to the last digit of the
square of N . Otherwise, Not Equal should be printed.
Explanation
For example, if the given number is N  15 ,
The square of N is 225 (15
2  225).
The last digit of N (15) is 5.
The last digit of square of N (225) is 5.
5 (last digit of 15) is equal to 5 (last digit of 225).
The output should be Equal as the last digit of N is equal to the
last digit of the square of N .
Sample Input 1
15
Sample Output 1
Equal
Sample Input 2
2
Sample Output 2
Not Equal


'''
print(program)
n = int(input("Enter a number : "))
Last_digit_of_n = int(n%10)
square_of_n = n**2
Last_digit_of_n_of_square = square_of_n %10

if Last_digit_of_n == Last_digit_of_n_of_square:
    print("Equal")
else : print("Not Equal")

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a three-digit number N and checks if
N is an Armstrong Number.
    Note
Armstrong Number
A number is said to be an Armstrong Number if the sum of
powers of all the digits of the number is the number itself.
Example:
371 is an Armstrong Number as the sum of the powers of all
digits of N is equal to 371. (3
37
31
3  371)
Input
The input will be a single line containing a three-digit integer
representing N .
Output
The output should be a single line containing a boolean. True should
be printed if N is an Armstrong Number. Otherwise, False
should be printed.
Explanation
For example, if the given number is N  371 ,
The digits in 371 are 3, 7 and 1.
Number of digits in 371 is 3.
Sum of digits to the power of 3 is 371. (3
37
31
3  371)
371 (Sum of the powers of all digits of N ) is equal to 371 ( N ). So,
N is an Armstrong Number.
The output should be True.
Sample Input 1
371
Sample Output 1
True
Sample Input 2
351
Sample Output 2
False
'''
print(program)
n = input("enter a three digit number : ")
number_of_dgit = len(n)
sum_of_power = (int(n[0])**number_of_dgit) + (int(n[1])**number_of_dgit) + (int(n[2])**number_of_dgit)
amstrong = sum_of_power == int(n)
if amstrong:
    print("True")
else: print("False")
# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if the triple of
N is divisible by 6.
Print the triple of N if the triple of N is divisible by 6.
Otherwise, print N .
    Note
The Triple of N is calculated as 3 * N .
Example: Triple of 6 is 18. ( 3 * 6  18 )

Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer. Triple of
N should be printed if the triple of N is divisible by 6.
Otherwise, N should be printed.
Explanation
For example, if the given number is N  6 ,
The triple of N is 18. ( 3 * 6  18 )
18 is divisible by 6.
The output should be 18 ( 3 * 6  18 ).
For example, if the given number is N  9 ,
The triple of N is 27. ( 3 * 9  27 )
27 is not divisible by 6.
The output should be 9 ( N ).
Sample Input 1
6
Sample Output 1
18
Sample Input 2
9
Sample Output 2
9

'''
n = int(input("Enter a number : "))

Triple_of_n = n*3
Triple_of_n_divisible_by_6 = (Triple_of_n % 6) == 0
if Triple_of_n_divisible_by_6:
    print(Triple_of_n)
else: print(n)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if N is
divisible by 3.
Print the triple of N if N is divisible by 3. Otherwise, print the
double of N .
    Note
Double of N is calculated as N * 2
Triple of N is calculated as N * 3

Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer. The triple of
N should be printed if N is divisible by 3. Otherwise, the double
of N should be printed.
Explanation
For example, if the given number is N  6 ,
6 is divisible by 3. So, N should be tripled ( N * 3 ).
The triple of 6 is 18. ( 6 * 3  18 )
The output should be 18.
For example, if the given number is N  4 ,
4 is not divisible by 3. So, N should be doubled ( N * 2 ).
The double of 4 is 8. ( 4 * 2  8 )
The output should be 8.
Sample Input 1
3
Sample Output 1
9
Sample Input 2
4
Sample Output 2
8

'''
print(program)
n = int(input("Enter a number : "))

Triple_of_n = n*3
n_divisible_by_3 = (n % 3) == 0
if n_divisible_by_3:
    print(Triple_of_n)
else: print(n*2)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B and finds the,
Remainder when A is divided by B ( A % B ).
Remainder when B is divided by A ( B % A ).
Print the smallest among the remainders A % B and B % A .
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer that is the
smallest among the remainders A % B and B % A .
Explanation
For example, if the given numbers are A  3 and B  7 ,
The remainder A % B is 3. ( 3 % 7  3 )
The remainder B % A is 1. ( 7 % 3  1 )
Smallest among 1 and 3 is 1.
The output should be 1.
Sample Input 1
3
7
Sample Output 1
1
Sample Input 2
12
6
Sample Output 2
0

'''
print(program)
a = int(input(('Enter value of A : ')))
b = int(input(('Enter value of b : ')))

Remainder_of_a_by_b, Remainder_of_b_by_a = a%b, b%a
if Remainder_of_a_by_b <= Remainder_of_b_by_a:
    print(Remainder_of_a_by_b)
else: print(Remainder_of_b_by_a)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if N is not
divisible by all the given numbers 2, 3, 5 and 7.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a boolean. True should
be printed if N is not divisible by the given numbers 2, 3, 5 and
7. Otherwise, False should be printed.
Explanation
For example, if the given number N  5633 ,
✔ 5633 is not divisible by 2.
✔ 5633 is not divisible by 3.
✔ 5633 is not divisible by 5.
✔ 5633 is not divisible by 7.
The output should be True as 5633 is not divisible by 2, 3, 5 and
7.
Sample Input 1
5633
Sample Output 1
True
Sample Input 2
1000
Sample Output 2
False
'''
print(program)
N = int(input("enter a number : "))
n_not_divisible_by_2, n_not_divisible_by_3, n_not_divisible_by_5, n_not_divisible_by_7 = ((N%2)!=0),((N%3)!=0),((N%5)!=0),((N%27)!=0)
if n_not_divisible_by_2 and n_not_divisible_by_3 and n_not_divisible_by_5 and n_not_divisible_by_7:
    print(True)
else: print(False)


# -------------------------------------------------------------------------------------
program = '''Write a program that reads a number N and checks if one of the
given conditions is satisfied.
N is divisible by 5 and N is divisible by 7.
N is less than 7.
Print N if one of the given conditions is satisfied. Otherwise, print
the remainder when N is divided by 5 and the remainder when
N is divided by 7 on each line.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer N if one of
the given conditions is satisfied.
Otherwise,
The first line of output should be an integer that is the remainder
when N is divided by 5.
The second line of output should be an integer that is the remainder
when N is divided by 7.

Explanation
For example, if the given number is N  3 ,
✖ N is divisible by 5 and N is divisible by 7
✔ N is less than 7
The output should be 3 as one of the given conditions is satisfied.
For example, if the given number is N  9 ,
✖ N is divisible by 5 and N is divisible by 7.
✖ N is less than 7.
✖ N is less than 7. (9 is not less than 7)
As both the given conditions are not satisfied, the output should be
the remainders when 9 is divided by 5 and 7.
The remainder when 9 divided by 5 is 4.
The remainder when 9 divided by 7 is 2.
The output should be,
4
2

Sample Input 1
9
Sample Output 1
4
2
Sample Input 2
3
Sample Output 2
3

'''
print(program)
N = int(input("enter a number : "))
n_divisible_by_5 , n_divisible_by_7, n_less_than_7 = ((N%5) == 0), ((N%7) == 0), N<7
if (n_divisible_by_5 and n_divisible_by_7) or n_less_than_7:
    print(N)
else:
    print(N%5)
    print(N%7)

# -------------------------------------------------------------------------------------
program = '''Write a program that reads two sides A and B of a right-angled
triangle and prints the Hypotenuse H of the right-angled
triangle.
    Quick Tip
According to Pythagoras's theorem, the Hypotenuse of a rightangled triangle is A
2  B
2
)
0.5
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer that is the
Hypotenuse of the right-angled triangle.
Explanation
For example, if the given sides are A  3 , and B  4 ,

Hypotenuse = A
2  B
2
)
0.5
The square of A is 9 (3
2
).
The square of B is 16 (4
2).
The sum of squares of A and B is 25 ( 9  16  25 ).
The hypotenuse is equal to 5. (25
0.5
)
The output should be 5.
Sample Input 1
3
4
Sample Output 1
5
Sample Input 2
12
5
Sample Output 2
13

'''

print(program)
a = int(input(('Enter value of A : ')))
b = int(input(('Enter value of b : ')))

value_a = a**2
value_b = b**2
Hypotenuse  =  (value_a + value_b)**0.5
print(Hypotenuse)


# -------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B and checks if
the square root of A is equal to B .
    Note
To calculate the Square Root of a number N , use the N
power 0.5 (N
0.5
)
Print Square root of A is equal to B if the square root of A is
equal to B . Otherwise, print Square root of A is not equal to B.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Square root
of A is equal to B should be printed if the square root of A is
equal to B . Otherwise, Square root of A is not equal to B
should be printed.

Explanation
For example, if the given numbers are A  64 and B  8 ,
The square root of A is 8 (64
0.5  8).
8 (square root of 64) is equal to 8 ( B ).
The output should be Square root of A is equal to B as the
square root of A is equal to B .
Sample Input 1
64
8
Sample Output 1
Square root of A is equal to B
Sample Input 2
55
5
Sample Output 2
Square root of A is not equal to B


'''
print(program)
a = int(input(('Enter value of A : ')))
b = int(input(('Enter value of b : ')))

squareroot_a = a**0.5
squareroot_b = b**0.5
if squareroot_a == b:
    print("Square root of A is equal to B")
else: print("Square root of A is not equal to B")

# -------------------------------------------------------------------------------------

program = '''Write a program that reads a four-digit number N and checks if
N is an Armstrong Number.

    Note
Armstrong Number
A number is said to be an Armstrong Number if the sum of
powers of all the digits of the number is the number itself.
Example:
1634 is an Armstrong Number as the sum of powers of all
digits of N is equal to 1634. (1
4 6
4 3
4 4
4  1634)

Print Armstrong Number if N is an Armstrong number.
Otherwise, print Not an Armstrong Number.
Input
The input will be a single line containing a four-digit integer
representing N .

Output
The output should be a single line containing a string. Armstrong

Number should be printed if N is an Armstrong number.
Otherwise, Not an Armstrong Number should be printed.
Explanation
For example, if the given four-digit number is N  1634 ,
The digits in 1634 are 1, 6, 3, and 4.
Number of digits in 1634 is 4.
The sum of powers of all the digits of N is 1634. (1
4 6
4 3
4 4
4
 1634)
1634 (Sum of powers of all digits of N ) is equal to 1634. So, N is
an Armstrong number.
The output should be Armstrong Number.
Sample Input 1
1634
Sample Output 1
Armstrong Number
Sample Input 2
1568
Sample Output 2     
Not an Armstrong Number

'''
print(program)
N = input("enter 4 digit number : ")

length = len(N)
first_no, second_no, third_no, fourth_no = int(N[0]), int(N[1]), int(N[2]), int(N[3])
sum_of_digits = (first_no**length) + (second_no**length) + (third_no**length) + (fourth_no**length)
Armstrong_Number = sum_of_digits == int(N)
if Armstrong_Number:
    print("Armstrong number")
else: print("Not an Armstrong Number")


# -------------------------------------------------------------------------------------

program = '''Given N number of days as input, write a program to convert N
number of days to years ( Y ), weeks ( W ) and days ( D ).
Note: Take 1 year  365 days
Input
The input contains single integer N .
Output
The first line of output contains an integer Y representing the
number of years.
The second line of output contains an integer W representing the
number of weeks.
The third line of output contains an integer D representing the
number of days.
Explanation
Given N  1329 . The value can be written as
1329  3 years  33 weeks  3 days
So the output should be
3
33
3
Sample Input 1
1329
Sample Output 1
3
33
3
Sample Input 2
0
Sample Output 2
0
0
0
'''
print(program)
Days = int(input("enter the n days : "))
year = Days//365
print(year)
Days_left = (Days - (year*365))
weeks = Days_left//7
print(weeks)
Days_left = (Days_left - weeks*7)
print(Days_left)
# -------------------------------------------------------------------------------------
