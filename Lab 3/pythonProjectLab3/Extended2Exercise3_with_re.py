import re

def parser(input):
    input = re.sub(r'<(\w+)>', r'\g<1>: ', input)
    input = re.sub(r'</\w+>', r'', input)
    return input

with open('./input.xml', 'r', encoding='utf-8') as f:
    s = ''.join(f.readlines())

res = parser(s)

with open('output3.yaml', 'w', encoding='utf-8') as f:
    f.write(res)