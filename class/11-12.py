a = int(input("number:"))
count = 0
for b in (2, pow(a, 0.5)):
    if a % b == 0:
        count += 1
        break
if(count == 0):
    print("Yes")
else:
    print("No")
