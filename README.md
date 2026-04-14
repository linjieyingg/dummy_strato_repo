# Assuming is_palindrome is part of a 'utils' module in 'my_project'
from my_project.utils import is_palindrome

# Basic palindromes
print(f"'madam' is a palindrome: {is_palindrome('madam')}")
# Expected output: 'madam' is a palindrome: True

print(f"'Racecar' is a palindrome: {is_palindrome('Racecar')}")
# Expected output: 'Racecar' is a palindrome: True

# Non-palindromes
print(f"'hello' is a palindrome: {is_palindrome('hello')}")
# Expected output: 'hello' is a palindrome: False

# Palindromes with spaces, punctuation, and mixed case
print(f"'A man, a plan, a canal: Panama' is a palindrome: {is_palindrome('A man, a plan, a canal: Panama')}")
# Expected output: 'A man, a plan, a canal: Panama' is a palindrome: True

print(f"'No lemon, no melon' is a palindrome: {is_palindrome('No lemon, no melon')}")
# Expected output: 'No lemon, no melon' is a palindrome: True