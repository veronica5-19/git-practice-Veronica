from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Veronica")
print("Today's Date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 2))
print("Division Error:", divide(10, 0))