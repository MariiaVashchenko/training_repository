# s = 'In Python, numeric types are float and int'

# x = 'абырваг'
# print(x[::-1])

text = list()
word_input = input('Введіть текст з дужками:')
j=0
#делаем из строки побуквенный список
for i in word_input:
     if word_input=='('
       i.

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
