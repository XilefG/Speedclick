x = 1
x2 = 1.55
y = "String"
z = True
a = [1,4, x]
b = tuple(a)
c = set(b)
d = dict()
d['hi'] = 1
d[''] = 0
# d = {'hi': 1, '': 0}

def thingy(a, b):
    print(a+b)

somethingelse = 3
if somethingelse == 3:
    print(2)
elif somethingelse == 2:
    print(3)
else:
    pass

for i in [1,2,3,4,5,6,9]:
    n = i**2
    print(n)    
    while n < 20:
        print(n**3)
        n += 1
        

