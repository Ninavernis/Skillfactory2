ticket = int(input("Ведите необходимое количество билетов: "))
payment = 0
for i in range(ticket):
    a = int(input("Введите возраст участника: "))
    if a < 18:
        payment += 0
    elif 18<= a < 25:
        payment += 990
    else:
        payment +=1390
if ticket > 3:
    print("Сумма к оплате:", payment * 0.9)
else:
    print("Сумма к оплате:", float(payment))
