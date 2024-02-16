a = 5
b = -5

print((a >= 0 and b>=0), (a>5 or b>5))

print(False and False)

program = ''' Write a program that reads a three-digit number and checks if all the
digits of the number are the same.
Input
The input will be a single line containing a three-digit integer.
Output
The output should be a single line containing a boolean. True should
be printed if all the digits of the number are the same, otherwise
False should be printed.
Explanation
For example, if the given number is 222,
The first digit (2) is equal to the second digit (2).
The second digit (2) is equal to the third digit (2).
The output should be True as all the digits of the number 222 are
the same.

Sample Input 1
222
Sample Output 1
True
Sample Input 2
989
Sample Output 2
False '''

print(program)    
digi = input("Enter the three digits number : ")

print((digi[0] == digi[1]) and (digi[0] == digi[2]))

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
program = '''Write a program that reads two numbers A and B and checks if
the sum of A and B is negative or the product of A and B
is negative.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a boolean. True should
be printed if the sum of A and B is negative or the product of
A and B is negative, otherwise False should be printed.
Explanation
For example, if the given numbers are A  5 and B  3 ,
✖ The sum of A and B is negative. ( 5  3  2 , 2 is a
positive number)
✔ The product of A and B is negative. ( 5 * 3  15 , 15 is a
negative number)
The output should be True as the product is negative.

Sample Input 1
5
-3
Sample Output 1
True
Sample Input 2
100
4
Sample Output 2
False

'''

print(program)   
a = int(input("Enter a digit : "))  
b = int(input("Enter a digit again : "))
add  = a=b
product = a*b
print((add < 0 ) or (product < 0))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads three sides A , B , and C of a
triangle and checks if the sum of any two sides of the triangle is
always greater than the third side.
Input
The first line of input contains an integer representing side A .
The second line of input contains an integer representing side B .
The third line of input contains an integer representing side C .
Output
The output should be a single line containing a boolean. True should
be printed if the sum of any two sides of the triangle is always
greater than the third side, otherwise False should be printed.
Explanation
For example, if the given sides of the triangle are A  3 , B  4
and C  5 ,
The sum of sides A , B should be greater than C and the sum
of sides B , C should be greater than A and the sum of sides
C , A should be greater than B .
✔ A  B is greater than C . ( 3  4  7 , 7 is greater than 5)
✔ B  C is greater than A . ( 4  5  9 , 9 is greater than 3)
✔ C  A is greater than B . ( 5  3  8 , 8 is greater than 4)

The output should be True as the sum of any two sides of the
triangle is always greater than the third side.
Sample Input 1
3
4
5
Sample Output 1
True
Sample Input 2
2
1
10
Sample Output 2
False


'''

print(program)   

a = int(input("Enter a number"))
b=  int(input("Enter a number"))
c = int(input("Enter a number"))

sum_a = a+b
sum_b = a+c
sum_c = b+c

print((sum_a > c) and (sum_b > b) and (sum_c >a))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a number N and checks if the number
N is between 50 and 100 or if the first digit of N is equal to 7.
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing a boolean. True should
be printed if the number N is between 50 and 100 or if the first
digit of N is equal to 7, otherwise False should be printed.
Explanation
For example, if the given number is N  54 ,
✔ The number N is between 50 and 100. (54 is between 50 and
100)
✖ The first digit of N is equal to 7. (The first digit of 54 is 5. 5 is
not equal to 7)
The output should be True as N is between 50 and 100.

Sample Input 1
54
Sample Output 1
True
Sample Input 2
101
Sample Output 2
False


'''
print(program)   
n = int(input("Enter a number : "))
b = str(n)

print(((n>50) and (n<100)) or (str(b[0]) == '7'))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads two numbers A and B and checks if
both the below conditions are satisfied.
One of A and B is less than 20.
One of A and B is greater than 30.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a boolean. True should
be printed if one of A and B is less than 20 and one of A
and B is greater than 30, otherwise False should be printed.
Explanation
For example, if the given numbers are A  15 and B  35 ,
✔ One of A and B is less than 20. (15 is less than 20)
✔ One of A and B is greater than 30. (35 is greater than 30)
The output should be True as both the given conditions are
satisfied.

Sample Input 1
15
32
Sample Output 1
True
Sample Input 2
9
21
Sample Output 2
False

'''

print(program)   
a = int(input("Enter a number :"))
b =int(input("Enter a number :"))

print(((a <20) or (b<20)) and ((a > 30) or (b>30)))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads the marks M in Maths, marks P in
Physics and marks C in Chemistry and checks if both the below
conditions are satisfied.
M  35 and P  35 and C  35 .
M  P  90 or P  C  90 or M  C  90 .
Input
The first line of input contains an integer representing marks M in
Maths.
The second line of input contains an integer representing marks P
in Physics.
The third line of input contains an integer representing marks C in
Chemistry.
Output
The output should be a single line containing a boolean. True should
be printed if both the given conditions are satisfied, otherwise False
should be printed.
Explanation
For example, if the given marks are M  50 , P  35 and C
40 ,
✔ M  35 and P  35 and C  35
✔ M  P  90 or P  C  90 or M  C  90

The output should be True as both the given conditions are
satisfied.
Sample Input 1
50
35
40
Sample Output 1
True
Sample Input 2
35
35
100
Sample Output 2
True

'''

print(program)   

m = int(input("Enter a m marks : "))
p = int(input("Enter a p marks : "))
c = int(input("Enter a c marks : "))


print(((m>=35) and (p>=35) and (c >=35)) or (((m+p) >= 90)) or ((p+c)>=90) or ((m+c)>=90))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads the marks M in Maths, marks P in
Physics and marks C in Chemistry and checks if any of the below
conditions is satisfied.
M  60 and P  50 and C  45 and M  P  C  180 .
M  P  120 or C  P  110 .
Input
The first line of input contains an integer representing marks M in
Maths.
The second line of input contains an integer representing marks P
in Physics.
The third line of input contains an integer representing marks C in
Chemistry.
Output
The output should be a single line containing a boolean. True should
be printed if any of the given conditions is satisfied, otherwise False
should be printed.
Explanation
For example, if the given marks are M  72 , P  65 and C  51 ,
✔ M  60 and P  50 and C  45 and M  P  C  180
✔ M  P  120 or C  P  110

The output should be True as any of the given conditions is
satisfied.
Sample Input 1
72
65
51
Sample Output 1
True
Sample Input 2
70
0
70
Sample Output 2
False
'''
print(program)   
m = int(input("Enter a m marks : "))
p = int(input("Enter a p marks : "))
c = int(input("Enter a c marks : "))
print(((m>=60) and (p>=50) and (c>=45) and ((m+p+c) >=180))  or (((m+p) >=120) or ((c+p) >=110)))
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 

program = '''Write a program that reads the marks in Maths M , Physics P ,
and Chemistry C , and checks if all the below conditions are
satisfied.
M  P  100 or P  C  100 or M  C  100
M  P  C  180
Input
The first line of input contains an integer representing M .
The second line of input contains an integer representing P .
The third line of input contains an integer representing C .
Output
The output should be a single line containing a boolean. True should
be printed if all the given conditions are satisfied, otherwise False
should be printed.
Explanation
For example, if the given marks are M  82 , P  55 , and C
45 ,
✔ M  P  100 or P  C  100 or M  C  100 . ( 82  55
137 , 137 is greater than or equal to 100)
✔ M  P  C  180 . ( 82  55  45  182 , 182 is greater than 180)
The output should be True as all the given conditions are satisfied.

Sample Input 1
82
55
45
Sample Output 1
True
Sample Input 2
71
30
70
Sample Output 2
False
    
'''

print(program)   

m = int(input("Enter a m marks : ")) # Initializing a variable
p = int(input("Enter a p marks : ")) # Initializing a variable
c = int(input("Enter a c marks : ")) # Initializing a variable
print((((m+p)>=100) or ((p+c)>=100) or ((m+c)>=100)) and ((m+p+c) >=180)) 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
