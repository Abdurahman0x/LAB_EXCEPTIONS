def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as e:
    print(e.__class__)
    print("NameError happened: variable 'b' is not defined!")
else:
    print("the operation is successful")