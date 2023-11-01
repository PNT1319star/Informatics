def parser(input): # Обработка входных данных в формате XML
    while ('</' in input):
        tr = False
        start = 0  #Переменная, которая отслеживает положение пары закрывающих тегов
        end = 0
        for i in range(len(input)):#Определить положение пар закрывающих тегов
            if tr and input[i] == '>':
                end = i
                tr = False
            if tr:
                continue
            if (i < len(input) - 1):
                if (input[i] + input[i + 1]) == '</':
                    tr = True
                    start = i

        input = input[0:start] + input[end + 1:len(input)]
    input = input.replace('<', '').replace('>', ": ").strip()
    return input
def emptyLine(input):
    # Изменить: удалить строки без символов
    input_lines = input.split('\n')
    input_lines = [line for line in input_lines if line.strip()]
    input = '\n'.join(input_lines)
    return input


with open('./input.xml', 'r', encoding='utf-8') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output.yaml', 'w', encoding='utf-8') as f:
    f.write(res)
with open('./output.yaml', 'r', encoding='utf-8') as f:
    y = ''.join(f.readlines())

line = emptyLine(y)


with open('output.yaml', 'w', encoding='utf-8') as f:
    f.write(line)