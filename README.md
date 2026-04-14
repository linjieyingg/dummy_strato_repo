from my_project.utils import convert_temperature

# Convert 25 degrees Celsius to Fahrenheit
celsius_value = 25
fahrenheit_result = convert_temperature(celsius_value, unit_from='C', unit_to='F')
print(f"{celsius_value}°C is {fahrenheit_result}°F")
# Expected output: 25°C is 77.0°F

# Convert 68 degrees Fahrenheit to Celsius
fahrenheit_value = 68
celsius_result = convert_temperature(fahrenheit_value, unit_from='F', unit_to='C')
print(f"{fahrenheit_value}°F is {celsius_result}°C")
# Expected output: 68°F is 20.0°C

# Invalid unit example (will raise an error)
try:
    convert_temperature(100, unit_from='K', unit_to='C')
except ValueError as e:
    print(f"Error: {e}")
# Expected output: Error: Invalid 'unit_from'. Must be 'C' or 'F'.