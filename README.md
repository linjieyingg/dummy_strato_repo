# Assuming 'has_number' is available in a module like 'project_utils'
from project_utils import has_number 

# Example 1: String containing numbers
text_with_number = "my_password123"
print(f"'{text_with_number}' has a number: {has_number(text_with_number)}")
# Expected output: 'my_password123' has a number: True

# Example 2: String without numbers
text_without_number = "my_password"
print(f"'{text_without_number}' has a number: {has_number(text_without_number)}")
# Expected output: 'my_password' has a number: False

# Example 3: Empty string
empty_text = ""
print(f"'{empty_text}' has a number: {has_number(empty_text)}")
# Expected output: '' has a number: False

# Example 4: String with only numbers
numeric_text = "12345"
print(f"'{numeric_text}' has a number: {has_number(numeric_text)}")
# Expected output: '12345' has a number: True