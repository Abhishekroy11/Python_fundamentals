'''Without using a Third Variable ,Swap a number.'''
a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

'''With using a Third Variable ,Swap a number.'''
a = int(input("Enter first number a: "))
b = int(input("Enter second number b: "))
c = a
a = b
b = c

print("After swapping:")
print("a =", a)
print("b =", b)