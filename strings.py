# strings

'''1) Write a program to get a string value and print the same as output:
Sample Input:
Hello World
Sample Output:
Hello World'''

Ans:
input_string = input("Enter a string: ")
print(input_string)

'''2) Write a program to print th length of the given string.
Sample Input:
Hello
Sample Output:
Hello: 5'''

Ans:
input_string = input("Enter a string: ")
length_of_string = len(input_string)
print(f"{input_string}: {length_of_string}")

'''3) There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.)
Problem Description:
The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered.
4. Print the total count of both the variables.
5. Exit.
Input & Output Format:
Input consists of one string.
Output consists of two integers.
First output consists of count of the uppercase.
Second output consists of count of the lowercase.
Sample Input:
Cyfuno
Sample Output:
Uppercase: 1
Lowercase: 5'''

Ans:
input_string = input("Enter a string: ")
uppercase_count = 0
lowercase_count = 0
for char in input_string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
print(f"Uppercase: {uppercase_count}")
print(f"Lowercase: {lowercase_count}")

'''4) Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
Sample Input:
Cyfuno
Sample Output:
Words: 1
Letters: 6'''

Ans:
input_string = input("Enter a string: ")
words_count = len(input_string.split())
characters_count = len(input_string.replace(" ", ""))
print(f"Words: {words_count}")
print(f"Letters: {characters_count}")

'''5)Write a Python Program to calculate the number of digits and letters in a string.

Problem Description:
The program takes a string and calculates the number of digits and letters in a string.

Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a digit is encountered and increment the second count variable each time a character is encountered.
4. Print the total count of both the variables.
5. Exit.

Input & Output Format:
Input consists of a string
Output consists of two integers.
First output refers to the total count of the characters.
Second output refers to the total count of the digits.

Sample Input:
Cyfuno2020

Sample Output:
Characters: 6
Digits: 4'''

Ans:
input_string = input("Enter a string: ")
letters_count = 0
digits_count = 0
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        letters_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digits_count += 1
print(f"Characters: {letters_count}")
print(f"Digits: {digits_count}")

'''6) Write a Python Program to form a new string made of the first 2 characters and last 2 characters from a given string.
Problem Description:
The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize a count variable to 0.
3. Use a for loop to traverse through the characters in the string and increment the count variable each time.
4. Form the new string using string slicing.
5. Print the newly formed string.
6. Exit.
Sample Input:
Hello World
Sample Output:
Held'''

Ans:
input_string = input("Enter a string: ")
new_string = ""
if len(input_string) >= 4:
    # Form the new string using string slicing
    new_string = input_string[:2] + input_string[-2:]
else:
    # If the string is too short, return the original string
    new_string = input_string
print(new_string)

'''7)Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo'''

Ans:
input_string = input("Enter a string: ")
index_to_remove = int(input("Enter the index to remove: "))
if 0 <= index_to_remove < len(input_string):
    new_string = input_string[:index_to_remove] + input_string[index_to_remove + 1:]
else:
    new_string = input_string  # If the index is invalid, return the original string
print(new_string)







