# Эта программа приветствует пользователя и запращивает
# ввод информации.

print('Hello World!')
print('What is your name?') # запрос имени
MyName = input()
print('It is good to meet you, ' + MyName)
print('The length of your mane is:')
print(len(MyName))
print('What is your age?') # запрос возраста
MyAge = input()
print('You will be ' + str(int(MyAge) +1) + ' in a year.')