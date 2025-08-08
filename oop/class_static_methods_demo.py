class Calculator:
    # Correct class attribute definition
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage:
sum_result = Calculator.add(10, 5)
print(f"The sum is: {sum_result}")

product_result = Calculator.multiply(10, 5)
print(f"The product is: {product_result}")
