def parser(input): # Обработка входных данных в формате XML
    while ('</' in input):
        tr = False
        start = 0 #Переменная, которая отслеживает положение пары закрывающих тегов
        end = 0
        for i in range(len(input)): #Определить положение пар закрывающих тегов
            if tr and input[i] == '>':
                end = i
                tr = False
            if tr:
                continue
            if (i < len(input) - 1):
                if (input[i] + input[i + 1]) == '</':
                    tr = True
                    start = i

        input = input[0:start] + input[end + 1:len(input)]#Удалять пару закрывающих тегов и содержимое внутри них из ввода
    input = input.replace('<', '').replace('>', ": ")
    return input

with open('./input.xml', 'r', encoding='utf-8') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output.yaml', 'w', encoding='utf-8') as f:
    f.write(res)