# C1.8. Импорт классов

# Классы также можно передавать в другие файлы с помощью импорта.
# Рассмотрим импорт на примере класса прямоугольника.

# Создадим конструктор, который будет описывать прямоугольник с
# имеющимися харктеристиками: ширина и высота.

# Вычислим площядь фигуры (area):

#                         width
#   	____________________
#   h	|                                       |
#   e	|                                       |
#   i	|            Rectangle            |
#   g	|                                       |
#   h	|                                       |
#   t	|___________________|
#
# 	         area = width * height

# Важно: Работать будем с несколькими файлами,
# размещенными в папке practice_C1. Не забывайье сохранять
# файл с помощью Ctrl + S !

class Rectangle:
	def _init_(self, width, height):
		self.width = width
		self.height =height

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	# Метод, рассчитывающий площадь
	def get_area(self):
		return self.width * self.height

# Выполним импорт из основного файла класса, где описан прямоугольник
# (Rectangle), "возмём" оттуда все свойства, такие как width(ширина) и
# height(высота) и создадим "псевдо" прямоугольник r1.

# Прямоугольник r1 должен получить те же характеристики, что и базовый
# прямоугольник (Rectangle). Проиллюстрируем сказанное схемой.

#                         width
#   	____________________
#   h	|                                       |
#   e	|                                       |
#   i	|            Rectangle            |
#   g	|                                       |
#   h	|                                       |
#   t	|___________________ |
#		   |
#		   v
#		  r1
#   	  __________________
#   	 |                                    |
#   	 |        r1.width = 20         |
#   	 |        r1.height = 11        |
#   	 |__________________|

# Создадим ещё один отдельный файл по название testRectangle.py, для
# того, чтобы реализовать наследование. Причём обезательно в той папке
# где находиться rectangle.py (в нашем случае это папка practice_C1)

from rectangle import Rectangle

r1 = Rectangle(10, 5)

print("r1.width =", r1.width)
print("r1.height =", r1.height)
print("r1.get_width =", r1.get_width())
print("r1.get_height =", r1.get_height())
print("r1.get_area =", r1.get_area())

# Обратите внимание, как осуществляется импорт, то есть прописывается с
# помощью ключевых фраз: from название файла, import название
# каласса. Теперь попробуем запустить testRectangle.py и должны получить
# ожидаемый результат, характеристики со значениями прямоугольника:

# r1.width = 10
# r1.height = 5
# r1.get_width = 10
# r1.get_height = 5
# r1.get_area = 50

# Process finished with exit code 0

# Теперь попробуем самостоятельно вывести второй унаследованный
# прямоугольник, назвав его, например r2.

# Каков механизм работы? Когда вы создаёте объект класса Rectangle,
# конструктор этого класса будет вызван для создания объекта, а атрибутами
# объекта будет присвоено значение из параметра.

# Проиллюстрируем сказанное схемой:

#                                                                                                    r1 = Rectangle(10, 5) 
# class Rectangle:						              ¦    ¦
#						                              ¦    ¦
#		def _init_(self, width, height):                                                   ¦    ¦
#                                                                                                                            ¦    ¦
# 				self.width = width   <=============== ¦    ¦
#                                                                                                                                 ¦  
# 				self.height = height   <================  ¦   

# 1.8.1
# Создайте класс Cat в отдельном файле. Класс должен содержать
# конструктор с параметрами: имя, пол, возраст и методы get(), которые
# будут возвращать все параметры обьекта.
# 
# В другом файле создайте экземпляры класса. В качестве входных данных 
# используйте класс Cat в файл.
# 
# Далее сделайте вывод инфорпмации о котах в консоль.
# 
# Решение для само проверки
# 
# class Cat:
# 	def _init_(self, name, gender, age):
# 		self.name = name
# 		self.gender = gender
# 		self.age = age
# 
# 	def get_name(self):
# 		return self.name
# 
# 	def get_gender(self):
# 		return self.gender
# 
# 	def get_age(self):
# 		return self.age
# 
# cat_1 = Cat("Baron", "boy", 2)
# cat_2 = Cat("Sam", "boy", 2)
# 
# print(cat_1.get_name(), cat_1.gender(), cat_1.age())
# print(cat_2.get_name(), cat_2.gender(), cat_2.age())

# 1.8.2
# Создайте класс Dog с помощью наследования класса Cat. Создайте метод 
# get_pet() таким образом, чтобы он вразвращал только имя и возраст.
# 
# Далее сделайте вывод этой информации в нонсоль.
# 
# class Dog:
#		def _init_(self, name):
# 			self.name = name
#
# class Dog(Cat):
# 		def _init_(self, name, gender, age):
# 				super()._init_(name)
# 				self.gender = gender
# 				self.age = age
#
#		def get_pet(self):
#				ruturn f'{self.name} {self.age}'
#
# dog_1 = Dog("Felix", "boy", 2)
# print(dog_1.get_pet())

