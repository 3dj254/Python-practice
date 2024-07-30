students=('pupil','cbc','mono','sophomer','junior','senior')
x,y,z,a,b,c=students
print(x)
print(y)
print(z) 
print(a)
print(b)
print(c)

x="python is fantastic"
print(x)

x='python'
y='is'
z='fantastic'
print(x + y + z)



name='John'
age=27
height='1.54inches'
is_student=True
print(name)
print(age)
print(height)
print(is_student)


x='ni mtaamu'
def myfunc():
    print('Dame yangu '+x)
myfunc()
    
y='ni IT guy'
def wanjau():
    print('JOHNNIE '+y)
wanjau()

x='fun'

def myfunc():
    global x
    x='fun'

myfunc()
print('python is '+ x)   

x=' am wise'
def me():
    print('I'+x)
me()    

carname="Volvo"
print(carname)

x=5
y=10
z=(x+y)
print(z)


x=y=z="oranges"
print(z)

#datatypes
x={"Bananas","Ovacadoes","Cherry"}
print(type(x))

X=5j
print(type(X))

X={'name':'jeff',"age":28}
print(type(X))

x =3+5j
y =5j
z = -5j
print(type(x))
print(type(y))
print(type(z))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

a="hello,world!"
print(a[1])

for x in 'banana':
    print(x)

a="Hello,World!"
print(len(a))    

txt="the best  things in life are free"
print('free'in  txt)

txt="The best things in life are free"
if "free" in txt:
    print('yes,"free" is present')

txt="The best things in life are free"
print('expensive' not in txt)

txt="The best things in life are free"
if 'expensive' not in txt:
    print("yes,'expensive' not present")