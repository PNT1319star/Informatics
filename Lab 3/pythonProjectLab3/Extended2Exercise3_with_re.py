import re

def parser(input):
    input = re.sub(r'<(\w+)>', r'\g<1>: ', input)
    input = re.sub(r'</\w+>', r'', input)
    return input
def emptyLine(input):
    input_lines = input.split('\n')
    input_lines = [line for line in input_lines if line.strip()]
    input = '\n'.join(input_lines)
    return input

with open('./input.xml', 'r', encoding='utf-8') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output_with_re.yaml', 'w', encoding='utf-8') as f:
    f.write(res)
with open('./output_with_re.yaml', 'r', encoding='utf-8') as f:
    y = ''.join(f.readlines())

line = emptyLine(y)
with open('output_with_re.yaml', 'w', encoding='utf-8') as f:
    f.write(line)

