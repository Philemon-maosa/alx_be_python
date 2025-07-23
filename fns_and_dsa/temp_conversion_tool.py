FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5

def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
	return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32