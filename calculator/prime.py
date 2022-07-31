n1=int(input("enter the num1"))
n2=int(input("enter the num2"))
for num in range(n1,n2+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)

