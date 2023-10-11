import re
def replace_time_with_tbd(text):
    pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?\b'  # Регулярное выражение для времени
    replaced_text = re.sub(pattern, '(TBD)', text)
    return replaced_text
def output(text,result):
    print("Исходный текст:")
    print(text)
    print("Текст с заменой времени на (TBD):")
    print(result)
# Пример текста с расписанием
text0 = "Занятие 1: 10:00 - 12:00"
text1 = "Занятие 2: 18:39:59 - 20:10:01"
text2 = "Уважаемые студенты! В эту субботу в 15:00 планируется доп.занятие на 2 часа.\nТо есть в 17:00:01 оно уже точно кончится."
text3 = "Перерыв с 10:00:20 до 10:20:30."
text4 = "Первый коллоквиум состоится в 15:20 в 18 октября."
# Замена времени на "(TBD)"
replaced_text0 = replace_time_with_tbd(text0)
replaced_text1 = replace_time_with_tbd(text1)
replaced_text2 = replace_time_with_tbd(text2)
replaced_text3 = replace_time_with_tbd(text3)
replaced_text4 = replace_time_with_tbd(text4)
# Вывод результата
output(text0,replaced_text0)
output(text1,replaced_text1)
output(text2,replaced_text2)
output(text3,replaced_text3)
output(text4,replaced_text4)
#Дополнетельное задание 2


