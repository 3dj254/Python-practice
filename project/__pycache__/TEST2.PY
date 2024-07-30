txt='my name is Dancan Jeff, am a telecommunication student from Pwani University'
print('Dancan Jeff'in txt)

txt="Iam 22 years from Kiambu county"
if '22' in txt:
    print('yes,I am 22 years')

txt="Iam 22 years from Kiambu county"
if 'Mutuya' not in txt:
    print('yes,I am from "Kiambu county"')    

txt='Centrino technology is a company that aids saccos and organisation in developing softwares and in financial managements using a sysytem called  Vanguard'
if 'Vanguard' in txt:
    print('yes,Vanguard is financial software system that Centrino uses to manages finances')

    b="Hello,world"
    print(b[2:5])

    b='Hello,World!'
    print(b[:5])

    b='Hello, World!'
    print(b[2:])

    b='Hello, world!'
    print(b[-5:-2])

    a='Hello, World!'
    print(a.lower())

    a='  Hello, World  '
    print(a.strip())

    a='Hello, World!'
    print(a.replace("H","J"))

    a='Hello, World!'
    print(a.split(","))

    a='Hello'
    b='World'
    c=a+b
    print(c)

    a="Hello"
    b="World"
    c=a+' '+b
    print(c)

    age='22 yrs old'
    txt=f'My name is Dan and am {age}'
    print(txt)

    price=999
    txt=f'I bought my laptop, {price} dollars'
    print(txt)

    price=999
    txt=f'I bought my laptop, {price:.2f} dollars'
    print(txt)

    txt=f'The price is {20*59}dollars'
    print(txt)

    Name='Dancan Jeff Ngaruiya Mwaura'
    location='Mutuya village,kiambu county,Kenya.'
    address='p.o box 438 Kiambu '
    txt=f'I am {Name} from {location} {address}'
    print(txt)


    txt=f'we are the so called \'vikings\' from the north'
    print(txt)



    d={'Name':"Dancan", "Height":'170cm','is_single':'True'}
    txt=f'I am {d["Name"]} with a height of {d["Height"]} and the rumors on going that am single are {d['is_single']} '
    print(txt)
 
txt=f'Mwaura\'s family is very blessed'
print(txt)

if 5 != 10
print('5 and 10 are not equal')