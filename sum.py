
num = int(input(" "));
if num == 0:
    exit();
elif num < 1:
    print("next");
else:
    sum = 0;
    while num > 0:
    	sum += num;
    	num -= 1;
    print("Sum = ", sum);
