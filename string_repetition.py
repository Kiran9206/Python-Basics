'''Given a word and a number N, write a program to print the given
word, N number of times in a single line.
Input
The first line of input contains a word.
The second line of input contains the integer N which denotes the
number of times the word has to be repeated.
Output
The output should contain the given string repeated N times in a
single line.
Note: There should not be any spaces between the repetitions.
Explanation
For example, if the given word is "Maths", and the N is 2,the word has
to be repeated 2 times, so the output should be
"MathsMaths"
Sample Input 1
Maths
2
Sample Output 1
MathsMaths
'''


a = input("Enter the sring : \n")
num = int(input("how many times you want me to repete the string : \n"))
a = a + " "
print(f"output : {num*a}")