def add(a,b):
    return a+b
  
def subtract(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
  
def division (a,b):
    if b!=0:
        return a/b
    else:
       return "error"
        

    
 

 
C=int(input
('''1: add
2: subtract
3: multiply 
4: division
enter your choice: '''))


no1=float(input("no1: "))
no2=float(input("no2: "))

if C==1:
    print(add(no1,no2))

elif C==2:
    print(subtract(no1,no2))

elif C==3:
    print(multiply(no1,no2))

elif C==4:
    print(division(no1,no2))

else:
    print("invalid choice")