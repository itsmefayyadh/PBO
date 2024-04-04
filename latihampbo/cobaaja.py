x = 100
y = 200

def myfunc():
    global y
    y = 300
    x = y

myfunc()

print(x)
print(y)