import math


def bmi(a, b):
    bmis = b/math.pow(a/100, 2)
    if bmis < 18:
        print("過輕")
    elif bmis < 24:
        print("正常")
    elif bmis < 27:
        print("過重")
    else:
        print("肥胖")


cm = float(input("cm:"))
kg = float(input("kg:"))
bmi(cm, kg)
