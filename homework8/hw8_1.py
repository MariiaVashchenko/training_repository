# 2.Програма переводить строку в нижній регістр
# 3.Програма видаляє зі строки такі символи пунктуації: .,-:;?!
# 4.Програма видаляє зайві пробіли\табуляції з правого кінця строки
# 5.Програма питає користувача яке слово (або словосполучення) він бажає замінити
# 7.Програма питає на яке слово треба замінити
# 8.Програма виводить відформатовану строку

def word_cat(str1: str, w_replace: str, change_word: str):
    str_new = str1.lower()
    str_new = str_new.replace('.', '')
    str_new = str_new.replace(',', '')
    str_new = str_new.replace('-', '')
    str_new = str_new.replace(':', '')
    str_new = str_new.replace(';', '')
    str_new = str_new.replace('?', '')
    str_new = str_new.replace('!', '')

    return str_new.replace(w_replace.lower(), change_word).rstrip()


if __name__ == '__main__':
    first_str = input('Ведіть строку:')
    w_to_change = input('Введіть слово яке треба замінити: ')
    change = input('Введіть слово на яке будемо міняти:')
    print(f'Відформатована строка: {word_cat(first_str, w_to_change, change)} ')


