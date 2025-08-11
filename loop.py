
count = 0

while count < 5:
    print("Loop iteration:", count)
    count += 1

##Break & Continue
count = 0
while count < 10:
    if (count == 7):
        print("Breaking the loop at count =", count)
        break
    else:
        print("Current count:", count)
    count += 1


i = 0
while i < 10:
    if (i == 7):
        print("continue =", i)
        i += 1
        continue
    else:
        print("Current count:", i)
    i += 1
