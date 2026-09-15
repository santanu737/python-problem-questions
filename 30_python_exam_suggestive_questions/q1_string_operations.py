"""
Question 1:
Write a Python program to take input a string. Now do the following:
1) Convert all in lowercase.
2) Convert the string in uppercase.
3) Count no. of characters.
4) Count no. of vowels.
"""

# Take input string
text = input("Enter a string: ")

# 1) Convert all in lowercase
lower_text = text.lower()
print("Lowercase:", lower_text)

# 2) Convert the string in uppercase
upper_text = text.upper()
print("Uppercase:", upper_text)

# 3) Count no. of characters
char_count = len(text)
print("Number of characters:", char_count)

# 4) Count no. of vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)
