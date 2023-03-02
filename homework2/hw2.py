# задача1 оплата коммуналных услуг

# вопрос: для значений с 0.25 - работает, для значений 0,25 получаю ошибку could not convert string to float: '0,28'
# какие существуют методы для таких случаев, чтобы значение с разделителем "," интерпритатор распознавал как число?

last_count = int(input(f'Введите предыдущие показатели: '))
current_count = int(input(f'Введите текущие показатели: '))
cost = float(input(f'Введите тариф, грн: '))

all_amount = (current_count - last_count) * cost
print(f'сумма {round(all_amount, 2)} грн')


# задача 2 расчитать доход
amount = float(input(f'Введите сумму дохода, грн: '))
percent = float(input(f'Введите %: '))

profit = amount - (amount * percent) / 100
print(f'Сумма дохода: {round(profit, 2)} грн; ' + f'сумма налога: {(amount * percent) / 100} грн')


# задача 3 расход на топливо

consumption = float(input(f'Введите расход бензина на 100 км , литры: '))
cost = float(input(f'Введите стоимость литра, грн: '))
km = float(input(f'Введите сколько км хотите проехать: '))

cost_transfer = consumption / 100 * km * cost

print(f'Стоимость поездки: {round(cost_transfer, 2)} грн')
