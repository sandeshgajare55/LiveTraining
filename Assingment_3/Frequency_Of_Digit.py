number=int(input("Enter any Number"))
print("Digit Frequency")
for i in range(0,number):
    cnt=0;
    temp=number;
    while temp>0:
        digit=temp%10
        if digit==i:
            cnt=cnt+1
        temp=temp//10;
    if cnt>0:
        print(i,'Frequency is',cnt)