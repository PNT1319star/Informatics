def countSmileys(text):
    pattern = 'X<{P'
    matches = text.replace(pattern, '')
    return (len(text) - len(matches)) // len(pattern)

# текста để kiểm tra
text1 = "Привет! X<{P X<{P X<{P"
text2 = "Здравствуйте! Это X<{P>"
text3 = "X<X>X<X<X>X<{P}"
text4 = "Доброе утро X<{P>. Сегодня я себя чувствую очень хорошо X<{P>"
text5 = "Hello world X<{P>"
# Ответы
print(countSmileys(text1))
print(countSmileys(text2))
print(countSmileys(text3))
print(countSmileys(text4))
print(countSmileys(text5))