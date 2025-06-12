from pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 7 * 2")
assert result == 17

result2 = calc.evaluate("7 * 2 + 3 * 5")
assert result2 == 29

print("Test passed!")