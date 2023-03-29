
def komm_pay(last_count: int, current_count: int, cost: float, ):
    return (current_count - last_count) * cost


def income_many(amount: float, percent: float, flag: bool):
    if flag == True:
        return amount - (amount * percent) / 100
    else:
        return (amount * percent) / 100


def travel_cost(consumption: float, cost: float, km: float):
    return consumption / 100 * km * cost


if __name__ == '__main__':
    # рассчитат тариф
    last = int(input(f'Введите предыдущие показатели: '))
    current = int(input(f'Введите текущие показатели: '))
    cost = float(input(f'Введите тариф, грн: '))
    print(f'сумма {round(komm_pay(last, current, cost), 2)} грн')

    # задача 2 расчитать доход
    amount = float(input(f'Введите сумму дохода, грн: '))
    percent = float(input(f'Введите %: '))
    print(
        f'Сумма дохода: {income_many(amount, percent, True)} грн; ' + f'сумма налога: {income_many(amount, percent, False)} грн')

    # задача 3 расход на топливо

    consumption = float(input(f'Введите расход бензина на 100 км , литры: '))
    cost = float(input(f'Введите стоимость литра, грн: '))
    km = float(input(f'Введите сколько км хотите проехать: '))
    print(f'Стоимость поездки: {round(travel_cost(consumption, cost, km), 2)} грн')
