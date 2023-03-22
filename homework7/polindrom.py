
#Задача1:
# пользователь вводит строку
word_input = input('Введіть строку:')
list_for_slice = list()
# избавляемся от знаков пунктуации
for n in word_input:
    if n not in (',', '.', ':', ' ', ';', '"', '{', '}', '\n', '\t', '(', ')', '?', '!', '/'):
        list_for_slice.append(n.lower())
# собираем строку и проверям полиндром:

if ''.join(list_for_slice)[::-1] == ''.join(list_for_slice)[::1]:
    print(f'Это полиндром!')
else:
    print(f'Это НЕ полиндром!')

# Задача 2:

text = list()
word_input = input('Введіть текст з дужками:')

#делаем из строки побуквенный список
for i in word_input:
    text.append(i)
i = 0
j = 0

# проходимся по списку извлекаем символы в скобках
while i in range(len(text)):
    if text[i] == '(':
        j = i
        while text[j] != ')':
            text.pop(j)
        if text[j] == ')':
            text.pop(j)
    i = i + 1
# собираем текст
print(''.join(text))
