'''Write a program that reads two words W1 and W2 .
W1 contains two parts. The first part contains W2 and the second part contains the remaining letters in W1 .
Print W1 with the first part as stars ( * ).
Input
The first line of input contains a string representing W1 .
The second line of input contains a string representing W2 .
Output
The output should be a single line containing a string W1 with the first part as stars.
Explanation
For example, if the given words are W1  Subway and W2  Sub .
S u b w a y
0 1 2 3 4 5
The first of Subway ( W1 ) is Sub ( W2 ).
Print stars ( * ) instead of Sub in Subway.
The output should be ***way.
Sample Input 1
Subway
Sub
Sample Output 1
***way
Sample Input 2
Hyperactive
Hyper
Sample Output 2
*****active'''


str1 = input("enter the mainstring: ")
str2 = input("Enter the string which you wanna change with star : ")

if str2 in str1:
    str1 = str1.replace(str2, (len(str2)*"*"))
    print(str1)
else:
    print("no")

# --------------------------------------------------
    


# -------------------------------------------------------------------------------------
'''Write a program that reads a word and prints the first two and the
last two letters of the word and prints the stars ( * ) instead of the
remaining letters.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing a string that has the
first two and the last two letters of the word and stars ( * ) instead
of the remaining letters.
Explanation
For example, if the given word is message,
The number of letters in the word message is 7.
The first two and the last two letters are me, ge.
The number of letters excluding the first two and last two letters in a word is
3.
3 stars should be printed between the first two and the last two letters.
The output should be me***ge.
The output should be me***ge.
Sample Input 1
message
Sample Output 1
me***ge
Sample Input 2
12345
Sample Output 2
12*45

'''


a =  input("enter something! : ")
length = len(a)
f_3 = a[:2]
l_3 = a[-2:]
r_c = length - 4
print(f_3+("*"*r_c)+l_3)





f = "apple"
g = "ple"

print(f[:3] == g[:3])
print(f[-3:]==g[-3:])