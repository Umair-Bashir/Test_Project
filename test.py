python -m py_compile test.py

# imperial to metric units
x = float(input('enter your number: '))
y= input('enter the units: ')
z = input('enter desired units: ')
y = y.lower()
z = z.lower()
def imp_to_metr(x):
    if y=='ft' and z=='in':
        res = x / 12
        print(str(res)+'in')
    elif y =='in' and z =='ft':
        res = x*12
        print(str(res)+'ft')
    elif y == 'kg' and z == 'lbs':
        res = x*2.205
        print(str(res)+'lb')
    elif y == 'lb' and z == 'kg':
        res = x / 2.205
        print(str(res)+ 'kg')

     
    else:
        print('You have entered inconsistent units to convert')
    return y
imp_to_metr(x)


#conversion of temperature
x = int(input('Enter the temperature: '))
t = input('Enter the temp units: ')
q = input('Enter the desired units: ')
t= t.upper()
q= q.upper()
def temp(x):
    if t == 'C':
        if q == 'K':
            y = x + 273.15
            print(str(round(y)) + 'C')
        elif q =='F':
            y = (x * 9/5) + 32
            print(str(round(y)) +'C' )
    elif t == 'K':
        if q =='C':
            y = x - 273.15
            print(str(round(y)) + 'C')
        elif q =='F':
            y = (x-273.15)*9/5+32
            print(str(round(y) )+'F')
    elif t == 'F':
        if q == 'K':
            y = (x-32) * 5/9 + 273.15
            print(str(round(y))+ 'K')
        elif q == 'C':
            y = (x-32) * 5/9
            print(str(round(y))+ 'C')
    else:
        print('You have entered the wrong set of units')
    return x
temp(x)

# Prefixes

w = float(input('Enter your number: '))
units = input('Enter the prefix: ')
units = units.lower()
def prefixes(w):
    if units == 'k' or units =='thousands'or units =='thousand':
        z = w / 1000
        print(str(round(z,2))+'Million')
    elif  units == 'm' or units == 'million'or units =='millions':
        z = w *1000
        print(str(round(z,2))+'k')
    return z
prefixes(w)
