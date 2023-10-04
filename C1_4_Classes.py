# C1.4. Классы

user_peter = { 
		"name" : "Peter",
		"email" : "peterrobertson@mail.com",
		"created_at" : "2019-05-05",
		"is_email_verified" : True,
		"purchases" : ["Egg", "Spam", "Hat", "Knife": "Shield", "Book of Knight secrets"],
}

user_julia = { 
		"name" : "Julia Donaldson",
		"email" : "juliadonaldson@mail.com",
		"created_at" : "2019-06-13",
		"is_email_verified" : True,
		"purchases" : ["Egg", "Spam", "Magis Brush"],
}

product_eggs = { 
		"name" : "Egg",
		"category" : "food",
		"is_availadle" : False,
		"quantity_in_stock" : 0,
		"vendor" : "Dark Knight LTD",
		"manager" : "William The Conqueror",
}

def is_product_availadle(product):
		return True if product ["quantity_in_stock"] > 0 else False
		
		

# Абстракция "пользователь". Давайте создадим такой класс.
# Для создания класс используем ключевое слово class:

class User:
		pass # этот класс ничего не делает
		
# Ключевое слово class работает так же, как ключевое слово def для
# создания функциий, только в данном случае дальше идёт 
# обьевление класса

# В отличие от переменных, для наименования которых в Python принято
# использовать snake_case, для классов используют CamelCase - регистр, 
# в котором слова склеены между собой, и каждое начинается с заглавной буквы.

# Пока что мы создали класс, в котором не чего не происходит. 
# Мы использовали ключевое слово pass, которое используется как 
# плецсхолдер для пустых классов и функций, чтобы избежать синтаксической ошибки.

# Как мы отбсуждали выше, классы используються как фабрика для создания 
# объектов. Давайте создадим  экземпляры нашего класса User, 
# соответствующие двум пользователям, Питеру и Юлии, и укажем их имена.

class User:
		pass
		
peter = User()
peter.name = "Peter Robertson"

julia = User()
julia.name = "Julia Donaldson"

print(peter.name)
print(julia.name)

# Вывод :
# Peter Robertson
# Julia Donaldson

# Здесь .name -- это атрибут экземпляра нашего класса.
# Атрибуты позволяют хранить произвольные данные в привязке к 
# конкретному экземпляру (сам по себе класс тоже может хранить 
# какие-то данные, но об этом позже).

# В этом смылсе классы и экземпляры  классов работают так же , как 
# модули: они создают пространство имён, в котором доступны 
# различные сущности. Как мы видим, после создания экземпляра 
# мы смогли каждому задать произвольный атрибут и положить 
# в него уникальное значение. При этом пространства имён наших 
# экземпляров остаются независимыми:

peter.email = "peterrobertson@mail.com"
print(peter.email)
print('\n')
print(julia.email)

peterrobertson@mail.com
Traceback (most recent call last):
		File "User/path/script.py", line 20, in <module>
		
				print(julia.email)
AttributeError: 'User' object has no attribute 'email'

# Создание проигвольного атрибута у одного экземпляра не привело ни к 
# каким изменениям у второго, что логично.

# Можно сравнить классы с формой и инструкцией для выпекания пирогов, 
#  а экземпляры - с конкретными испечёнными пирогами. Если вы откусили 
# кусок от одного, это никак не повлияет на следующие.

# Дальше мы увидем, как правильно решить нашу изначальную проблему 
# с повторяющимися по структуре словарями.

# 1.4.1 
# Что из этого являеться "настоятельной рекомендуемыми" названием для 
# класса в Python?
#
# cartState
# CartState +
# cart_state

# 1.4.2
# Как создать экземпляр каласса User с названием chris ?
# 
# User(chris)
# chris = User
# User.hris
# chris = User() +

# 1.4.3
# Как создать атрибут phone_number у объекта peter ?
# 
# peter.phone_number = "79116451238" +++
# peter["phone_number"] = "79116451238"
# peter.phone_number == "79116451238"

# Мы можем задавать атрибуты, которые будут доступны из любого объекта,
# причём без дополнительных действий. Для этого их надо объявить прямо
# внутри класса:

class User:
		number_of_fingers = 5
		number_of_eyes = 2
		
lancelot = User()
print(lancelot.number_of_fingers)
# Выыод:
# 5

4

