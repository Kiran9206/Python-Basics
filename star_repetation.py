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




