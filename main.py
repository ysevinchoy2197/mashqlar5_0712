#1-misol
ovqat = input("Ovqat nomini kiriting: ").lower()

if ovqat == "pizza":
    print("Narxi: 10$")
elif ovqat == "burger":
    print("Narxi: 8$")
elif ovqat == "sushi":
    print("Narxi: 15$")
    if 15 > 10:
        print("Qimmat")
elif ovqat == "pasta":
    print("Narxi: 12$")
else:
    print("Bizda bunday taom yo‘q")

#2-misol
harorat = int(input("Haroratni kiriting: "))
holat = input("Ob-havo holatini kiriting (masalan: yomg‘ir yoki yo‘q): ").lower()

if harorat > 30:
    print("Juda issiq")
elif 20 <= harorat <= 30:
    print("Yoqimli")
elif 0 <= harorat < 20:
    print("Salqin")
else:
    print("Juda sovuq")

if holat == "yomg‘ir":
    print("Soyabon oling")

#3-misol
bal = int(input("Imtihon balini kiriting: "))

if bal < 0 or bal > 100:
    print("Xato bal kiritildi")
elif bal >= 90:
    print("A’lo")
elif 75 <= bal <= 89:
    print("Yaxshi")
elif 60 <= bal <= 74:
    print("Qoniqarli")
else:
    print("Yiqildi")
