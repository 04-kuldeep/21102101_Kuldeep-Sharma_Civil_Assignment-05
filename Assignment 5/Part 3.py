a=float(input("Enter the length of side a : "))
b=float(input("Enter the length of side b : "))
c=float(input("Enter the length of side c : "))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(area)
else :
    print("Error")