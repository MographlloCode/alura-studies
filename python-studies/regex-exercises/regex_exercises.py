''' This exercises were offered by w3resources '''

import re

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). 

def exercise_one():
  user_entry = input('Type something: ')
  def validator(user_entry):
    validator = re.compile(r'[^a-zA-Z0-9]')
    string = validator.search(user_entry)
    return not bool(string)
  
  print(validator(user_entry))

# 2. Write a Python program that matches a string that has an a followed by zero or more b's. 

def exercise_two():
  user_entry = input('Type something: ')
  def validator(text):
    validator = '^a(b*)$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')
  
  print(validator(user_entry))
  

# 3. Write a Python program that matches a string that has an a followed by one or more b's. 

def exercise_three():
  user_entry = input('Type something: ')
  def validator(text):
    validator = '^a(b+)$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')
  
  print(validator(user_entry))

# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'. 

def exercise_four():
  user_entry = input('Type something: ')
  def validator(text):
    validator = 'a(b?)$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')
  
  print(validator(user_entry))

# 5. Write a Python program that matches a string that has an a followed by three 'b'. 

def exercise_five():
  user_entry = input('Type something: ')
  def validator(text):
    validator = 'ab{3}$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')
    
  print(validator(user_entry))

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'. 

def exercise_six():
  user_entry = input('Type somthing: ')
  def validator(text):
    validator = 'ab{2,3}$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')
  
  print(validator(user_entry))

# 7. Write a Python program to find sequences of lowercase letters joined with a underscore. 

def exercise_seven():
  user_entry = input('Type something: ')
  def validator(text):
    validator = '^[a-z]+_[a-z]+$' 
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))

# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters. 

def exercise_eight():
  user_entry = input('Type something: ')
  def validator(text):
    validator = '^[A-Z]{1}[a-z]+$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))
  
# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. 

def exercise_nine():
  user_entry = input('Type something: ')
  def validator(text):
    validator = 'a.*?b$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))

# 10. Write a Python program that matches a word at the beginning of a string. 

def exercise_ten():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '^\w+'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))    

# 11. Write a Python program that matches a word at the end of string, with optional punctuation. 

def exercise_eleven():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '\w+\S*$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))   

# 12. Write a Python program that matches a word containing 'z'. 

def exercise_twelve():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '.z+.'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))   


# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word. 

def exercise_thirteen():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '\Bz\B'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))  

# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores. 

def exercise_fourteen():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '^[a-zA-Z0-9_]*$'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))  

# 15. Write a Python program where a string will start with a specific number. 

def exercise_fifteen():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = '^[0-9]+'
    if re.search(validator, text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))  


# 16. Write a Python program to remove leading zeros from an IP address. 

def exercise_sixteen():
  ip = '192.168.045.003'
  string = re.sub('\.[0]*', '.', ip) # The sub() function replaces the matches with the text of your choice: in this exemple ??? 192.168.45.3
  print(string)

# 17. Write a Python program to check for a number at the end of a string. 

def exercise_seventeen():
  user_entry = input('Type Something: ')
  def validator(text):
    validator = re.compile(r'.*[0-9]$')
    if validator.match(text):
      return 'Found a match!'
    else:
      return ('Not matched!')

  print(validator(user_entry))  

# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string. 
# "Exercises number 1, 12, 13, and 345 are important"

# def exercise_eighteen():
#   results = re.finditer(r'([0-9]{1-3})', 'Exercises number 1, 12, 13, and 345 are important') # 
#   print('Number of length 1 to 3')
#   for n in results:
#     print(n.group(0)) #

# 19. Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'



# 20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'



# 21. Write a Python program to find the substrings within a string. 
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'
# Note: There are two instances of exercises in the input string.



# 22. Write a Python program to find the occurrence and position of the substrings within a string. 



# 23. Write a Python program to replace whitespaces with an underscore and vice versa. 



# 24. Write a Python program to extract year, month and date from an url. 



# 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format. 



# 26. Write a Python program to match if two words from a list of words starting with letter 'P'. 



# 27. Write a Python program to separate and print the numbers of a given string. 



# 28. Write a Python program to find all words starting with 'a' or 'e' in a given string. 



# 29. Write a Python program to separate and print the numbers and their position of a given string. 



# 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string. 



# 31. Write a Python program to replace all occurrences of space, comma, or dot with a colon. 



# 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon. 



# 33. Write a Python program to find all five characters long word in a string. 



# 34. Write a Python program to find all three, four, five characters long words in a string. 



# 35. Write a Python program to find all words which are at least 4 characters long in a string. 



# 36. Write a python program to convert camel case string to snake case string. 



# 37. Write a python program to convert snake case string to camel case string. 



# 38. Write a Python program to extract values between quotation marks of a string. 



# 39. Write a Python program to remove multiple spaces in a string. 



# 40. Write a Python program to remove all whitespaces from a string. 



# 41. Write a Python program to remove everything except alphanumeric characters from a string. 



# 42. Write a Python program to find urls in a string. 



# 43. Write a Python program to split a string at uppercase letters. 



# 44. Write a Python program to do a case-insensitive string replacement. 



# 45. Write a Python program to remove the ANSI escape sequences from a string. 



# 46. Write a Python program to find all adverbs and their positions in a given sentence. 

# Sample text : "Clearly, he has no excuse for such behavior."



# 47. Write a Python program to split a string with multiple delimiters. 

# Note : A delimiter is a sequence of one or more characters used to specify the boundary between separate, independent regions in plain text or other data streams. An example of a delimiter is the comma character, which acts as a field delimiter in a sequence of comma-separated values.



# 48. Write a Python program to check a decimal with a precision of 2. 



# 49. Write a Python program to remove words from a string of length between 1 and a given number. 



# 50. Write a Python program to remove the parenthesis area in a string. 
# Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Expected Output:
# example
# w3resource
# github
# stackoverflow


# 51. Write a Python program to insert spaces between words starting with capital letters. 


# 52. Write a Python program that reads a given expression and evaluates it. 
# Terms and conditions:
# The expression consists of numerical values, operators and parentheses, and the ends with '='.
# The operators includes +, -, *, / where, represents, addition, subtraction, multiplication and division.
# When two operators have the same precedence, they are applied to left to right.
# You may assume that there is no division by zero.
# All calculation is performed as integers, and after the decimal point should be truncated Length of the expression will not exceed 100.
# -1 ? 10 9 = intermediate results of computation = 10 9


# 53. Write a Python program to remove lowercase substrings from a given string. 


# 54. Write a Python program to concatenate the consecutive numbers in a given string. 
# Original string:
# Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.
# After concatenating the consecutive numbers in the said string:
# Enter at 120 Kearny Street. The security desk can direct you to floor 16. Please have your identification ready.


# 55. Write a Python program to convert a given string to snake case. 
# Sample Output:
# java-script
# gd-script
# btw...-what-*-do*-you-call-that-naming-style?-snake-case?


# 56. Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.
# Sample Output:
# Orange
# [1, 2, 3, 4, 5]
# Java
# Python
#  '''