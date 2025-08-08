class Calculator:
  calculation_type ' "Arithmetic Operations"

@staticmethod
     def add(a,b):
         return a + b


 @classmethod
     def multiply(cls, a, b):
	 print(f" Calculation Type: {cls.calculation_Type}")
         return a * b

print(Calculator.add(10,5))
print(Calculator.multiply(4,3))
	 