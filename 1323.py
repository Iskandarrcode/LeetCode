num = 9669
num = str(num)
for i in range(0, len(num)):
    if num[i] == "6":
        print(int(num[:i] + "9" + num[i + 1:]))

print(int(num))