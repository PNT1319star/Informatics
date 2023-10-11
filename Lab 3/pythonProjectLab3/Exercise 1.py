import re

def countSmileys(text):
    pattern = r'X<{P'
    matches = re.findall(pattern, text)
    return len(matches)

# текста для проверки
text1 = "Привет! X<{P X<{P X<{P"
text2 = "Здравствуйте! Это X<{P>"
text3 = "X<X>X<X<X>X<{P}"
text4 = "Доброе утро X<{P>. Сегодня я себя чувствую очень хорошо X<{P>"
text5 = "X<{P>"
ans=[3,1,1,2,1] #Ожиданные ответы
# функция для проверки
def validate(texts_to_validate, ans):
    for i in range(len(texts_to_validate)):
        if ans[i] != countSmileys(texts_to_validate[i]):
            print("ERROR")
            return
    print("Successful")

validate([text1, text2, text3, text4, text5], ans)
#Ответы
print(countSmileys(text1))
print(countSmileys(text2))
print(countSmileys(text3))
print(countSmileys(text4))
print(countSmileys(text5))
