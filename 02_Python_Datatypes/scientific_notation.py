num = 12.59
print(num)

num1 = 0.1259e2
print(num1) # 12.59

num2 = 1259e-2
print(num2) # 12.59

print(num.__sizeof__()) # 24
print(num1.__sizeof__()) # 24
print(num2.__sizeof__()) # 24