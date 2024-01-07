''' Write a program that prints the sum of the digits of a given threedigit number.
Input
The input will be a single line containing a three-digit number.
Output
The output should be a single line containing the sum of the three
digits of the given number.
Explanation
For example, if the given number is 326, the sum of its digits, 3  2
6 is 11.
Sample Input 1
326
Sample Output 1
11
Sample Input 2
222
Sample Output 2 '''



digi = int(input("Enter the digits"))

sum = 0
for i in range(len(str(digi))+1):
    sum += i

print(f"sum of {digi} : {sum}")