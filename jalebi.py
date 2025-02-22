a = int(input("enter a number:"))
sum = 0
while a!=0:
    rem = rem%10
    sum += rem*rem*rem 
    a=a/10
print(sum)    
if sum==a:
    print("armstrong number")
else:
    print("not an armstrong number")
