
# Элегантного решения через циклы изобразить не получается:), лучше сделать через функции, но эту лекцию не смотрела

# Наверняка, можно обеденить в один список и использовать метки, но другие лекции я еще не смотрела.
# Да, можно использовать одну переменную переобявляя список, но изменения удобнее вносить тут.
# cохраняем базу знаний чат-бота
hello_discuss = ['привіт', 'хай', 'доброго дня']
doing_discuss = ['справи', 'робиш', 'займаєшься']
doing_cinema = ['фільм', 'кінотеатр', 'серіал']
i = 0

print(f'Ця програма імітує розмову з чат-ботом. Якщо захочете завершити бесіду напишіт "бувай"')
question = input('Ви:')

# пока пользователь не вышел из программы, продолжать беседу

while question.lower().strip() != 'бувай':
    i = 0
    flag = 0
    # пройтись по словарю чат-бота приветствие
    while i < len(hello_discuss):
        if hello_discuss[i] not in question.lower():
            i += 1
        else:
            break
    if i == len(hello_discuss):
        print(f'Чат-бот: Я терпляче буду чекати, поки ти мені не скажеш: привіт, хай, чи доброго дня. Якщо втомишся '
              f'напиши "бувай"')
        question = input('Ви:')

    elif i != len(hello_discuss):
        print(f'Чат-бот: Доброго вечора, я бот з України!')
        question = input('Ви:')

        i = 0
        # пройтись по словарю чат-бота "что делаешь"
        while i < len(doing_discuss):
            if doing_discuss[i] not in question.lower():
                i += 1
            else:
                break
        if i == len(doing_discuss):
            print(f'Чат-бот: Не зрозуміло, але  продовжимо розмову')
            question = input('Ви:')

        elif i != len(doing_discuss):
            print(f'Чат-бот: Я вчуся програмувати на Pyton')
            question = input('Ви:')
         # пройтись по словарю хобби

            i = 0
            while i < len(doing_cinema):
                if doing_cinema[i] not in question.lower():
                    i += 1
                else:
                    break
            if i == len(doing_cinema):
                print(f'Чат-бот: Цікаво, розкажи ще щось')
                question = input('Ви:')
                print(f'Чат-бот: Поки не розумію мови,дай мені пару тижднів.Бувай!')
                exit(0)

            elif i != len(doing_cinema):
                print(f'Чат-бот: Чудово! А мені подобається читати книжки у жанрі фентезі')
                question = input('Ви:')
                print(f'Чат-бот: Давай продовжимо розмову через пора годин. Прийшла нова лекція на навчанні - хочу '
                      f'подивитись. Хорошого дня, бувай!')
                exit(0)
        print(f'Чат-бот: Дуже добре, мені пора бувай')
        exit(0)
exit(0)
