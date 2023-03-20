# подскажите, что имелось в виду под вариантами реализации?
# обработчик ввода цифр или подсчет суммы?

list_cnt = []
sum_cnt = input('Введите число или sum:')
flag = 0

while sum_cnt.lower().strip() != 'sum':
    while isinstance(sum_cnt, str):
        try:
            sum_cnt = float(sum_cnt)
            list_cnt.append(sum_cnt)
        except Exception:
            print(f'Не число.Введите число или sum!')
            break

    sum_cnt = input('Введите число или sum:')
# посчитать сумму с помощью while
i = 0
s_all = 0
j = len(list_cnt)

while i < j:
    s_all = list_cnt[i] + s_all
    i += 1
print(f'Посчитано с помощью while {s_all}')

# посчитать сумму с помощью for
s_all = 0

for i in range(j):
    s_all = s_all + list_cnt[i]
print(f'Посчитано с помощью for {s_all}')
