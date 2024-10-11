input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])
for x in range(-100,101):
    h = a * (x ** 3) + b * (x ** 2) + c * x + d == 0
    if h >= 0:
        t = h
    elif h <= 0:
        t = h
    print(t)
