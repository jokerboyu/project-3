(1):
grade=int(input("enter your grade:"))

if grade>=50:
    print("pass")
else:
    print("fail")
 
(2):
x=int(input("Enter your grade:"))

if x>=90:
    print("A")
elif x>=80:
    print("B") 
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")
   
(3):
a=int(input("enter:"))
b=int(input("enter:"))
c=int(input("enter:"))
s=a+b+c
av=s/3
print("sum of three numbers=",s)
print("Average=",av)
p=a**b
print("the value of a power b=",p)
print("the value of C=",c)


if a==-a:
      print("error, a value is negative")
else:
    r=a**c 
    print("c the root of a =",r)

(4):
x=int(input("Enter:"))
y=int(input("Enter:"))
z=int(input("Enter:"))

if x>z>y:
    print("maximium no.=",x,"minimum no.=",y)
elif x>y>z:
    print("maximum no.=",x,"minimum no.=z",z)
elif y>z>x:
    print("maximum no.=",y,"minimum no.=",x)
elif y>x>z:
    print("maximum no.=",y,"minimum no.=",z)
elif z>y>x:
    print("maximum no.=",z,"minimum no.=",x)
elif z>x>y:
    print("maximum no.=",z,"minimum no.=",y)
else:
    print ("numbers are not found!!")