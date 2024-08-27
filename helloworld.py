intValues = [1, 2, 3]

x, z, r = intValues
y = "Hello world!"
if 5 > 2:
    print("Five is greater than 2")

print(type(x))
print(y)
print(z)
print(r)

s = "resderer"

def myFunc():
    global a
    a = "test"
    print(s)

myFunc()
print(a)