program = '''Write a program that reads a number and converts it to a positive
number.
If the given number is negative, convert it to a positive number and
print it. Otherwise, print the given number.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a positive integer.
Explanation
For example, if the given number is 5,
5 is a negative number.
5 should be converted to a positive number which is 5.
The output should be 5.
For example, if the given number is 39,
39 is a positive number.
The output should be 39.

Sample Input 1
-5
Sample Output 1
5
Sample Input 2
39
Sample Output 2
39

'''

print(program)

a = -5

if (a < 0):
    print(a * -1)
else:
    print(a)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the student's marks as input and prints
PASS or FAIL.If the student has scored more than 50, print PASS.
In all other cases print FAIL.
Input
The input will be a single line containing a number.
Output
The output should be a single line containing PASS or FAIL.
Explanation
In the given example, the student's marks are 85, which is more than
50, so the result should be PASS.
Similarly, if the marks are 45, the result should be FAIL.
Sample Input 1
85
Sample Output 1
PASS
Sample Input 2
45
Sample Output 2
FAIL
'''
print(program)
a = int(input("enter the marks"))
if (a >= 50 ):
    print("PASS")
else:
    print("Fail")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B and prints the
greatest among the two numbers.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer that is the
greatest among the two numbers.
Explanation
For example, if the given numbers are A  4 and B  3 , the
output should be 4 as 4 is greater than 3.
Sample Input 1
4
3
Sample Output 1
4
Sample Input 2
15
7
Sample Output 2
15
'''
print(program)
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
if (a > b):
    print(a)
else:
    print(b)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the age of a person and checks if the age
of the person is greater than or equal to 18 for eligibility to vote.
Print Eligible if the age of the person is greater than or equal to
18, otherwise print Not Eligible.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a string. Eligible should
be printed if the age of the person is greater than or equal to 18,
otherwise Not Eligible should be printed.
Explanation
For example,
If the given age of a person is 15, the output should be Not Eligible
as 15 is not greater than or equal to 18.
If the given age of a person is 21, the output should be Eligible as
21 is greater than 18.
Sample Input 1
15
Sample Output 1
Not Eligible
Sample Input 2
21
Sample Output 2
Eligible

'''

print(program)
age =  int(input("Enter you age : "))
if (age >=18):
    print("Eligible")
else:
    print("Not Eligible")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program to print the relation between two numbers, X and
Y .
Input
The first line is integer X .
The second line is integer Y .
Output
Print X  Y if X is less than Y otherwise, print X  Y .
Explanation
Given X  2 , Y  5
As 2  5 X  Y
So the output is X  Y
Sample Input 1
2
5
Sample Output 1
X < Y
Sample Input 2
5
2
Sample Output 2
X >= Y
'''

print(program)
x = int(input("Enter the x value : "))
y = int(input("Enter the y value : "))
if (x >= y):
    print("X >= Y")
else:
    print("X < Y")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program to check if the given two numbers are equal.
Input
The first line of input contains a number.
The second line of input contains a number.
Output
If the given numbers are equal, print "Equal". In all other cases, print
"Not Equal".
Explanation
For example, if the first number is 5 and the second number is 5.
Since both the given numbers are equal. So the output should be
"Equal".
Whereas, if the first number is 10 and the second number is 5, both
the numbers are not equal. So the output should be "Not Equal".
Sample Input 1
5
5
Sample Output 1
Equal
Sample Input 2
10
5
Sample Output 2
Not Equal
'''


print(program)
a =  int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
if (a == b):
    print("Equal")
else:
    print("Not Equal")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Given the length and breadth of a box, check if it is a Rectangle or
Square.
Input
The first line of input will contain the length of the box.
The second line of input will contain the breadth of the box.
Output
If the given length and breadth are equal, print "Square". In all other
cases, print "Rectangle".
Explanation
For example, if the given length is 6, and the given breadth is 6, the
length and breadth are equal. So the output should be "Square".
Similarly, if the given length is 5, and the breadth is 10, the length
and breadth are not equal. So the output should be "Rectangle".
Sample Input 1
6
6
Sample Output 1
Square
Sample Input 2
5
10
Sample Output 2
Rectangle
'''


print(program)
length  =  int(input("Enter the length of a box : "))
breadth =  int(input("Enter the brreadth of a box : "))
if (length == breadth):
    print("Square")
else:
    print("Rectangle")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a temperature and checks if the given
temperature is between 15 and 40.
Print Can go for a walk if the given temperature is between 15 and
40, otherwise print Cannot go for a walk.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a string. Can go for a
walk should be printed if the temperature is between 15 and 40,
otherwise Cannot go for a walk should be printed.
Explanation
For example, if the given temperature is 26,
26 is greater than 15.
26 is less than 40.
So, 26 is between 15 and 40.
The output should be Can go for a walk as 26 is between 15 and
40.
Sample Input 1
26
Sample Output 1
Can go for a walk
Sample Input 2
5
Sample Output 2
Cannot go for a walk

'''



print(program)
tem = int(input("Enter the temperature : "))
if(tem >= 15 and tem <=40):
    print("Can go for a walk")
else:
    print("cannot go for a walk")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads the size S and page count C of a
book and checks if S is equal to large or C is greater than or
equal to 300.
Print Buy a Book if S is equal to large or C is greater than or
equal to 300. Otherwise, print Do Not Buy a Book.
Input
The first line of input contains a string representing S .
The second line of input contains an integer representing C .
Output
The output should be a single line containing a string. Buy a Book
should be printed if S is equal to large or C is greater than or
equal to 300. Otherwise, Do Not Buy a Book should be printed.
Explanation
For example, if the given size is S  "large" and the page count is
C  80 ,
✔ S is equal to large. (large is equal to large)
✗ C is greater than or equal to 300. (80 is not greater than or
equal to 300)
The output should be Buy a Book as the size of the book S is
equal to large.
Sample Input 1
large
80
Sample Output 1
Buy a Book
Sample Input 2
small
200
Sample Output 2
Do Not Buy a Book
'''


print(program)
s = input("Enter the size 'small / large : ")
c = int(input("Enter the count of pages of a book : "))
if s == 'large' or c >=300:
    print("Buy a Book")
else:
    print("Do not Buy a Book")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B and checks if
both A and B are less than or equal to 1000 or B is greater
than 500.
Print Pair if both A and B are less than or equal to 1000 or
B is greater than 500. Otherwise, print Not a Pair.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Pair should be
printed if both A and B are less than or equal to 1000 or B
is greater than 500. Otherwise, Not a Pair should be printed.
Explanation
For example, if the given numbers are A  300 and B  200 ,
✔ Both A and B are less than or equal to 1000. (300 and 200 are
less than or equal to 1000)
✗ B is greater than 500. (200 is not greater than 500)
The output should be Pair as both 300 and 200 are less than or
equal to 1000.
Sample Input 1
300
200
Sample Output 1
Pair
Sample Input 2
1464
20
Sample Output 2
Not a Pair
'''

print(program)
a = int(input("Enter the value of A :"))
b = int(input("Enter the value of B :"))
if (a <= 1000 and b<=1000) or (b>500):
    print("Pair")
else:
    print("Not a Pair")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the scores A and B of two players
and checks if one of the scores is greater than 300 and the sum of
the scores is less than 500.
Print Can team up if one of the scores is greater than 300 and the
sum of the scores is less than 500, otherwise print Cannot team
up.
Input
The first line of input contains an integer representing the score A .
The second line of input contains an integer representing the score
B .
Output
The output should be a single line containing a string. Can team up
should be printed if one of the scores is greater than 300 and the
sum of the scores is less than 500, otherwise Cannot team up
should be printed.
Explanation
For example, if the given scores are A  350 and B  134 ,
✔ One of the scores is greater than 300 (350 is greater than 300).
✔ The sum of scores is less than 500 ( 350  134  484 , 484 is
less than 500).
The output should be Can team up as one of the scores is greater
than 300 and the sum of the scores is less than 500.
Sample Input 1
350
134
Sample Output 1
Can team up
Sample Input 2
450
82
Sample Output 2
Cannot team up

'''

print(program)
score_a = int(input("Enter the score of player A : "))
score_b = int(input("Enter the score of player B : "))
if(score_a > 300 or score_b > 300) and ((score_a + score_b) < 500):
    print(
        "Can team up"
    )
else:
    print("Cannot team up")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads a number and checks if the given number
is equal to 0 or positive.
Print Zero if the given number is equal to 0.
Print Positive if the given number is a positive number.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a string. Zero should
be printed if the given number is equal to 0. Positive should be
printed if the given number is greater than 0.
Explanation
For example, if the given number is 56, the output should be
Positive as 56 is greater than 0.

Sample Input 1
56
Sample Output 1
Positive
Sample Input 2
0
Sample Output 2
Zero

'''

print(program)
num = int(input("Enter a number : "))
if (num == 0):
    print("Zero")
if(num > 0):
    print("Positive")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a number and checks if the given number
is zero, positive or negative.
Print Zero if the given number is equal to 0.
Print Positive if the given number is greater than 0.
Print Negative if the given number is less than 0.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a string. Zero should
be printed if the given number is equal to 0. Positive should be
printed if the given number is greater than 0. Negative should be
printed if the given number is less than 0.
Explanation
For example,
If the given number is 12, the output should be Negative as 12 is less
than 0.
If the given number is 15, the output should be Positive as 15 is greater
than 0.

Sample Input 1
-12
Sample Output 1
Negative
Sample Input 2
15
Sample Output 2
Positive
Sample Input 3
0
Sample Output 3
Zero

'''
print(program)
num = int(input("Enter a number : "))
if (num == 0):
    print("Zero")
if(num > 0):
    print("Positive")
if(num <0):
    print("Negetive")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a number N and checks if N is
greater than 10.
Print the result of N  5 if N is greater than 10. Otherwise, print
the result of N  1 .
Input
The input will be a single line containing an integer representing N .
Output
The output should be a single line containing an integer. The result of
N  5 should be printed if N is greater than 10. Otherwise, the
result of N  1 should be printed.
Explanation
For example, if the given number is N  3 ,
3 is not greater than 10.
The result of N  1 is 4 ( 3  1  4 ).
The output should be 4 as N is not greater than 10.
For example, if the given number is N  63 ,
63 is greater than 10.
Sample Input 1
3
Sample Output 1
4
Sample Input 2
63
Sample Output 2
68

'''
print(program)
n = int(input("Enter a number : "))
if (n>10):
    print(n+5)
else:
    print(n+1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the three angles A , B , and C of a
Triangle and checks if the sum of the three angles of the Triangle is
equal to 180.
Print the Triangle as given below if the sum of the three angles of the
Triangle is equal to 180. Otherwise, print Not a Valid Triangle.
Input
The first line of input contains an integer representing angle A .
The second line of input contains an integer representing angle B .
The third line of input contains an integer representing angle C .
Output
The output should be three lines containing a Triangle as shown in
the sample output if the sum of A , B and C is equal to 180.
Otherwise, the output should be a single line containing the string
Not a Valid Triangle.
Explanation
For example, if the given three angles of the Triangle are A  60 ,
B  45 , and C  75 ,
The sum of the three angles of the Triangle is equal to 180. ( 60
+ 45 + 75  180 )
The output should be the Triangle as given below,
To print the Triangle, print a star on the first line, two stars on the
second line and three stars on the third line.
For example, if the given three angles of the Triangle are A  80 ,
B  90 and C  100 ,
The sum of the three angles of the Triangle is not equal to 180.
( 80 + 90 + 100  270 )
The output should be Not a Valid Triangle.
Sample Input 1

60
45
75
Sample Output 1
*
**
***
Sample Input 2
80
90
100
Sample Output 2
Not a Valid Triangle

'''
print(program)
a = int(input("enter the a side of A triangle : "))
b = int(input("enter the a side of B triangle : "))
c = int(input("enter the a side of C triangle : "))
if ((a+b+c) == 180):
    print(1*"*")
    print(2*"*")
    print(3*"*")
else:
    print("Not a Valid Triangle")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads three numbers A , B , and C , and
checks if each number is greater than 100.
Print All are greater than 100 if each number is greater than 100.
Otherwise, print Not all are greater than 100.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
The third line of input contains an integer representing C .
Output
The output should be a single line containing a string. All are
greater than 100 should be printed if each number is greater than
100. Otherwise, Not all are greater than 100 should be printed.
Explanation
For example, if the given numbers are A  110 , B  256 , and C
6350 ,
✔ A is greater than 100. (110 is greater than 100)
✔ B is greater than 100. (256 is greater than 100)
✔ C is greater than 100. (6350 is greater than 100)
The output should be All are greater than 100 as each number is
greater than 100.
Sample Input 1
110
256
6350
Sample Output 1
All are greater than 100
Sample Input 2
120
50
1
Sample Output 2
Not all are greater than 100

'''
print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
c = int(input("enter the C value : "))
if(a > 100 and b>100 and c>100):
    print("All are greater than 100")
else:
    print("Not all are greater than 100")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a Room Number and checks if the
Number in the given Room Number is less than 30.
The Room Numbers are in the format of R1 , R35 , etc.
Print Ground Floor if the Number is less than 30. Otherwise, print
Not Ground Floor.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing a string. Ground Floor
 should be printed if the Number in Room Number is less than 30.
Otherwise, Not Ground Floor should be printed.
Explanation
For example, if the given Room Number is R27,
R 2 7
0 1 2
The first character of the Room Number is R.
The remaining characters of the Room Number is 27. So, the Number in
Room Number is 27.
27 is less than 30.
The output should be Ground Floor as the room number is less
than 30.
Sample Input 1
R27
Sample Output 1
Ground Floor
Sample Input 2
R401
Sample Output 2
Not Ground Floor


'''
print(program)
num = input("enter the room number which is starting from the letter R : ")
a = int(num[1:])

if (a < 30):
    print("Ground Floor")
else:
    print("Not Ground Floor")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads three numbers A , B , and C , and
checks if the difference between any two numbers ( A  B , B  C
and C  A ) is always less than 25.
Print Difference is less than 25 if the difference between any two
numbers ( A  B , B  C and C  A ) is always less than 25.
Otherwise, print Difference is not less than 25.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
The third line of input contains an integer representing C .
Output
The output should be a single line containing a string. Difference is
less than 25 should be printed if the difference between any two
numbers is always less than 25. Otherwise, Difference is not
less than 25 should be printed.
Explanation
For example, if the given numbers are A  65 , B  60 , and C
52 ,
The difference between A , B ( A  B ) and the difference
between B , C ( B  C ) and the difference between C , A
( C  A ) should be less than 25.
✔ The difference A  B is less than 25. ( 65  60  5 , 5 is less
than 25)
✔ The difference B  C is less than 25. ( 60  52  8 , 8 is less
than 25)
✔ The difference C  A is less than 25. ( 52  65  13 , 13 is less
than 25)
The output should be Difference is less than 25 as the difference
between any two numbers ( A  B , B  C and C  A ) is always
less than 25.
Sample Input 1
65
60
52
Sample Output 1
Difference is less than 25
Sample Input 2
100
70
35
Sample Output 2
Difference is not less than 25
'''

print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
c = int(input("enter the C value : "))
if((a-b)<25 and (b-c)<25 and (c-a)<25):
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads three sides A , B , and C of a
triangle and checks if the sum of any two sides of the triangle is
always greater than the third side.
Print It's a Triangle if the sum of any two sides of the triangle is
always greater than the third side. Otherwise, print It's not a
Triangle.
Input
The first line of input contains an integer representing side A .
The second line of input contains an integer representing side B .
The third line of input contains an integer representing side C .
Output
The output should be a single line containing a string. It's a Triangle
should be printed if the sum of any two sides of the triangle is
always greater than the third side. Otherwise, It's not a Triangle
should be printed.
Explanation
For example, if the given sides of the triangle are A  4 , B  5
and C  3 ,
The sum of sides A , B should be greater than C and the sum
of sides B , C should be greater than A and the sum of sides
C , A should be greater than B .
✔ A  B is greater than C . ( 4  5  9 , 9 is greater than 3)
✔ B  C is greater than A . ( 5  3  8 , 8 is greater than 4)
✔ C  A is greater than B . ( 3  4  7 , 7 is greater than 5)
The output should be It's a Triangle as the sum of any two sides of
the triangle is always greater than the third side.
Sample Input 1
4
5
3
Sample Output 1
It's a Triangle
Sample Input 2
6
3
2
Sample Output 2
It's not a Triangle


'''

print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
c = int(input("enter the C value : "))
if((a+b)>c and (b+c)>a and (c+a)>b):
    print("It's a Triangle")
else:
    print("It's not a Triangle")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a string S and checks if the length of
S is between 2 and 7 or the first character of S is not equal to
"a".
Print Valid String if the length of S is between 2 and 7 or the
first character of S is not equal to "a". Otherwise, print Not a
Valid String.
Input
The input will be a single line containing a string representing S .
Output
The output should be a single line containing a string. Valid String
should be printed if the length of S is between 2 and 7 or the first
character of S is not equal to "a". Otherwise, Not a Valid
String should be printed.
Explanation
For example, if the given string S  "apple" ,
✔ The length of S is between 2 and 7. The length of apple is 5.
5 is between 2 and 7)
✖ The first character of S is not equal to "a". The first character
of apple is equal to a)
The output should be Valid String as the length of S is between
2 and 7.
Sample Input 1
apple
Sample Output 1
Valid String
Sample Input 2
atlantic
Sample Output 2
Not a Valid String
Sample Input 3
out
Sample Output 3
Valid String

'''

print(program)
s = input("enter a value : ")
if((len(s)>=2 and len(s)<=7) or (s[0] != 'a')):
    print("Valid String")
else:
    print("Not a Valid String")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B and checks if
any of the given numbers is between 40 and 140.
Print Between 40 and 140 Yes if any of the given numbers is
between 40 and 140. Otherwise, print Between 40 and 140 No.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Between 40
and 140 Yes should be printed if any of the given numbers is
between 40 and 140. Otherwise, Between 40 and 140 No
should be printed.
Explanation
For example, if the given numbers are A  12 and B  100 ,
✖ A is between 40 and 140. (12 is not between 40 and 140)
✔ B is between 40 and 140. (100 is between 40 and 140)
The output should be Between 40 and 140 Yes as B is
between 40 and 140.
Sample Input 1
12
100
Sample Output 1
Between 40 and 140: Yes
Sample Input 2
33
4
Sample Output 2
Between 40 and 140: No
'''

print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
if((a >=40 and a<=140) or (b >=40 and b<=140)):
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B , and checks
if one of the below conditions is satisfied.
One of A and B is less than 20.
The sum of A and B is between 30 and 50.
Print the sum of A and B if one of the given conditions is
satisfied. Otherwise, print A and B on each line.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
If one of the given conditions is satisfied,
The output should be a single line containing an integer that is the
sum of A and B .
Otherwise,
The first line of output should be an integer containing A .
The second line of output should be an integer containing B .
Explanation
For example, if the given numbers are A  45 and B  7 ,
✔ One of A and B is less than 20. (7 is less than 20)
✖ The sum of A and B is between 30 and 50. ( 45  7  52 ,
52 is not between 30 and 50)
The output should be 52 (sum of A and B ) as one of the given
conditions is satisfied.
For example, if the given numbers are A  30 and B  100 ,
✖ One of A and B is less than 20. (30 and 100 are not less
than 20)
✖ The sum of A and B is between 30 and 50. ( 30  100
130 , 130 is not between 30 and 50)
The output should be,
30
100

Sample Input 1
45
7
Sample Output 1
52
Sample Input 2
30
100
Sample Output 2
30
100


'''

print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
if(((a+b) >=30 and (a+b)<=50) or (a<20 or b<20)):
    print(a+b)
else:
    print(a, "\n",b)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B and checks if
one of the below conditions is satisfied.
One of A and B is equal to 6.
The sum of A and B is equal to 6.
The difference between A and B is equal to 6.
Print Lucky if one of the given conditions is satisfied. Otherwise,
print Not Lucky.

Note.

Both A  B and B  A is used to calculate the difference
between A and B .


Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing a string. Lucky should
be printed if one of the given conditions is satisfied. Otherwise, Not
Lucky should be printed.
Explanation
For example, if the given numbers are A  4 and B  10 ,
✖ One of A and B is equal to 6.
✖ The sum of A and B is equal to 6.
✔ The difference between A and B is equal to 6.
The output should be Lucky as one of the given conditions is
satisfied.
Sample Input 1
4
10
Sample Output 1
Lucky
Sample Input 2
3
2
Sample Output 2
Not Lucky
Sample Input 3
15
9
Sample Output 3
Lucky
'''


print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
if((a==6 or b==6) or (a+b) == 6 or (a-b) == 6 or (b-a) == 6):
    print("Lucky")
else:
    print("Not Lucky")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Write a program that reads three numbers A , B and C and
prints the greatest among the three numbers.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
The third line of input contains an integer representing C .
Output
The output should be a single line containing an integer that is the
greatest among the three numbers.
Explanation
For example, if the given numbers are A  2 , B  5 and C  7 ,
The greatest among A and B is B . (5 is greater than 2)
The greatest among B and C is C . (7 is greater than 5)
The output should be 7 as it is the greatest among the three
numbers.
Sample Input 1
2
5
7
Sample Output 1
7
Sample Input 2
3
5
2
Sample Output 2
5

'''

print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
c = int(input("enter the C value : "))
if((a>b) and (a>c)):
    print(a)
if((b>a) and (b>c)):
    print(b)
if((c>a) and (c>b)):
    print(c)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''A company decided to give a bonus of 5% to an employee if his/her
years of service is more than five years.
Write a program that reads an employee's salary and c
and decides whether the employee gets the bonus or not.
Input
The first line of input will contain the salary of an employee.
The second line of input will contain years of service.
Output
If the employee gets a bonus, print the net bonus amount.
If the employee doesn't get the bonus, print "No Bonus",.
Explanation
For example, if the employee's salary is 25000 and years of
experience is 3. As the years of experience is less than 5, the output
should be "No Bonus".
Similarly, if the employee's salary is 50000 and years of experience is
6. As the years of experience is more than 5, the employee is eligible
for the bonus. By computing the 5% of his salary, the net bonus
amount should be 2500.0
Sample Input 1
25000
3
Sample Output 1
No Bonus
Sample Input 2
50000
6
Sample Output 2
2500.0

'''
print(program)
salary = int(input("enter your salary : "))
service = int(input("Enter years of service : "))
if(service >=5):
    print((salary*5)/100)
else:
    print("No Bonus")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


program = '''Given three angles of a triangle, write a program to check whether
the triangle is valid or not. A triangle is valid if the sum of its three
angles is equal to 180 degrees.
Input
The first line of input will contain the first angle of the triangle.
The second line of input will contain the second angle of the triangle.
The third line of input will contain the third angle of the triangle.
Output
If the sum of the three angles is equal to 180, print "It's a Triangle". In
all other cases, print "It's not a Triangle".
Explanation
For example, if the first angle is 80, the second angle is 90, and the
third angle is 100. Therefore the sum of the three angles(80  90
100 is 270, which is not equal to 180. So the output should be "It's
not a Triangle".
Similarly, if the first angle is 60, the second angle is 60, and the third
angle is 60. Therefore the sum of the three angles(60  60  60 is
180, which is equal to 180. So the output should be "It's a Triangle".
Sample Input 1
80
90
100
Sample Output 1
It's not a Triangle
Sample Input 2
60
60
60
Sample Output 2
It's a Triangle

'''

print(program)
a = int(input("enter the a side of A triangle : "))
b = int(input("enter the a side of B triangle : "))
c = int(input("enter the a side of C triangle : "))
if ((a+b+c) == 180):
    print("It's a Triangle")
else:
    print("It's not a Triangle")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the rank of a student R and checks if
R is less than 10.
Print HONOR STUDENT if R is less than 10. Otherwise, print
NORMAL STUDENT.
Input
The input will be a single line containing an integer representing R .
Output
The output should be a single line containing a string. HONOR
STUDENT should be printed if R is less than 10. Otherwise,
NORMAL STUDENT should be printed.
Explanation
For example, if the given rank is R  1 , the output should be
HONOR STUDENT as 1 is less than 10.
For example, if the given rank is R  15 , the output should be
NORMAL STUDENT as 15 is not less than 10.
Sample Input 1
1
Sample Output 1
HONOR STUDENT
Sample Input 2
15
Sample Output 2
NORMAL STUDENT
'''

print(program)
r = int(input("Enter the rank of a student : "))
if(r<10):
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two numbers A and B and checks if
the sum of A and B is less than 10.
Print the sum of A and B if the sum of A and B is less
than 10. Otherwise, print the product of A and B .
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
Output
The output should be a single line containing an integer. The sum of
A and B should be printed if the sum of A and B is less
than 10. Otherwise, the product of A and B should be printed.
Explanation
For example, if the given numbers are A  1 and B  2 ,
✔ The sum of A and B is less than 10. (Sum of A and B is
3 ( 1  2  3 ). 3 is less than 10)
The output should be 3 ( 1  2  3 ) as the sum of A and B is
less than 10.
For example, if the given numbers are A  42 and B  10 ,
✖ The sum of A and B is less than 10. (Sum of A and B is
52 ( 42  10  52 ). 52 is not less than 10)
The output should be 420 ( 42  10  420 ) as the sum of A and
B is not less than 10.
Sample Input 1
1
2
Sample Output 1
3
Sample Input 2
42
10
Sample Output 2
420


'''
print(program)
a = int(input("enter the A value : "))
b = int(input("enter the B value : "))
if((a+b)<10):
    print(a+b)
else:
    print(a*b)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads two coupon codes A and B and
checks if the first three characters of one of the coupon codes is
equal to "DIS".
Print Discount if the first three characters of one of the coupon
codes is equal to "DIS". Otherwise, print No Discount.
Input
The first line of input contains a string representing A .
The second line of input contains a string representing B .
Output
The output should be a single line containing a string. Discount
should be printed if the first three characters of one of the coupon
codes is equal to "DIS". Otherwise, No Discount should be printed.
Explanation
For example, if the given coupon codes are A  "DISA9#5" and B
"6BYX" ,
✔ The first three characters of A is equal to "DIS". The first three
characters of "DISA9#5" is "DIS". "DIS" is equal to "DIS")
✖ The first three characters of B is equal to "DIS". The first three
characters of "6BYX" is "6BY". "6BY" is not equal to "DIS")
The output should be Discount as the first three characters of A
is equal to "DIS".
Sample Input 1
DISA9#5
6BY@X
Sample Output 1
Discount
Sample Input 2
17F
DVC&SN
Sample Output 2
No Discount
'''

print(program)
a = input("enter the A value : ")
b = input("enter the B value : ")

if(a[:3] == 'DIS' or b[:3] == 'DIS'):
    print("Discount")
else:
    print("No Discount")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads the marks M in Maths and marks P
in Physics and checks if both M and P are greater than 35 or
sum of M and P is greater than or equal to 100.
Print Qualified if both M and P are greater than 35 or sum of
M and P is greater than or equal to 100. Otherwise, print Not
Qualified.
Input
The first line of input contains an integer representing M .
The second line of input contains an integer representing P .
Output
The output should be a single line containing a string. Qualified
should be printed if both M and P are greater than 35 or sum
of M and P is greater than or equal to 100. Otherwise, Not
Qualified should be printed.
Explanation
For example, if the given marks are M  50 and P  40 ,
✔ Both M and P are greater than 35. (50 and 40 are greater
than 35)
✖ Sum of M and P is greater than or equal to 100. ( 50 + 40 =
90 , 90 is not greater than or equal to 100)
The output should be Qualified as both M and P are greater
than 35.
Sample Input 1
50
40
Sample Output 1
Qualified
Sample Input 2
30
49
Sample Output 2
Not Qualified 
 

'''
print(program)
m = int(input("Enter the m marks : "))
p = int(input("Enter the p marks : "))
if(((m>35)and(p>35)) or ((m+p) >= 100)):
    print("Qualified")
else:
    print("Not Qualified")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads a three-digit number N and checks if
both the given conditions are satisfied.
Any of the digits of N is not equal to 5
N is between 300 and 700
Print Valid Number if both the given conditions are satisfied.
Otherwise, print Not a Valid Number.
Input
The input will be a single line containing a three-digit integer
representing N .
Output
The output should be a single line containing a string. Valid Number
should be printed if both the given conditions are satisfied.
Otherwise, Not a Valid Number should be printed.
Explanation
For example, if the given three-digit number is N  653 ,
✔ Any of the digits of N is not equal to 5. (Digits of N are 6, 5
and 3. 6, 3 are not equal to 5)
✔ N is between 300 and 700. (653 is between 300 and 700)
The output should be Valid Number as both the given conditions
are satisfied.
Sample Input 1
653
Sample Output 1
Valid Number
Sample Input 2
947
Sample Output 2
Not a Valid Number
'''

print(program)
digi = input("Enter three digit number : ")
if((digi[0] or digi[0] or digi[0]) != '5' and (int(digi) >=300 and int(digi) <= 700) ):
    print("Valid Number")
else:
    print("Not a Valid Number")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

program = '''Write a program that reads three numbers A , B , and C and
checks if any of the given numbers is between 9 and 21.
Input
The first line of input contains an integer representing A .
The second line of input contains an integer representing B .
The third line of input contains an integer representing C .
Output
The output should be a single line containing a boolean. True should
be printed if any of the given numbers is between 9 and 21.
Otherwise, False should be printed.
Explanation
For example, if the given numbers are A  2 , B  4 , and C
16 ,
✖ A is between 9 and 21. (2 is not between 9 and 21)
✖ B is between 9 and 21. (4 is not between 9 and 21)
✔ C is between 9 and 21. (16 is between 9 and 21)
The output should be True as one of the given numbers is between
9 and 21.
Sample Input 1
2
4
16
Sample Output 1
True
Sample Input 2
2
4
6
Sample Output 2
False

'''

print(program)
a = int(input("enter the value of A : "))
b = int(input("enter the value of B : "))
c = int(input("enter the value of C : "))
if(((a>=9) and (a<=21)) or ((b>=9) and (b<=21)) or ((c>=9) and (c<=21))):
    print(True)
else:
    print(False)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




