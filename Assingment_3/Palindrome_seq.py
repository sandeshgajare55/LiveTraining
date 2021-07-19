max = 500
for num in range(1, max + 1):
    tempno = num
    reverse = 0
    while (tempno > 0):
        Rem = tempno % 10
        reverse = (reverse * 10) + Rem
        tempno = tempno // 10
if (num == reverse):
        print(reverse, end='  ')