x = 3 + 5j
print(type(x))

# y = 3 + 5i -> throw an error

a = 1.22 + 3.55J
print(a)

b = complex(12, 9)
print(b) # 12 + 9j

c = complex(12)
print(c) # 12 + 0j


print(a.real) # 1.22
print(a.imag) # 3.55