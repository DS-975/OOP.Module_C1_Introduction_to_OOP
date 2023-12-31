#C1.10 Практикум

#1.10.1 

#Создайте класс одной из геометрических фигур (например,
#прямоугольника), где в конструкторе задабтся атрибуты: начальные
#координаты х, у, width и height (или другие в зависимости от выбранной
#фигуры).

#Создайте метод, который возыращает атрибуты прямоугольника как строку
#(постарайтесь применить магический метод __str__. Для объекта 
#прямоугольника со значениеми атрибута х = 5, у = 10, width = 50,  height = 100
#метод должен вернуть строку Rectangle :  5, 10, 50, 100.

class Rectangle:
	def __init__(self, x, y, width,  height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
	def __str__(self):
		return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}.'
		
rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)

#1.10.2

#В классе, написанном в предыдущем задании, создайте метод, который
#будет рассчитывать площадь фигуры. Выведите значение площади на 
#экран.

class Rectangle:
	def __init__(self, x, y, width,  height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
	def __str__(self):
		return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}.'
		
rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)
print(rect_1.get_area())

#1.10.3

#В проекте "Дом питомца" добавим новую услугу - электронный кошелёк.
#Необходимо создать класс "Клиент", который будет содержать данные о 
#клинтах и их финансовых операциях. О клиенте известна слудующая
#информация: имя, фамилия, город, баланс.

#Далее сделайте вывод о клиентах в консоль в формате:

#"Иван Петров. Москва. Баланс: 50 руб." 

class Customers:
	def __init__(self, first_name, second_name, city, balance):
		self.first_name = first_name
		self.second_name = second_name
		self.city = city
		self.balance = balance
		
	def __str__(self):
		return f'''"{self.first_name} {self.second_name}".{self.city}. Баланс: {self.balance} руб.'''

costomer_1 = Customers('Иван' ,  'Петров' , 'Москва' ,50)
print(customer_1)

#1.10.4

#Команда прокта "Дом питомца" планирует большой корпоратив для своих
#клиентов. Вам необходимо написать программу, которая позволит
#составить список гостей. В класс "Клиент" добавить метод, который будет
#возвращать информацию только по имени, фамилии и городе клиента.

#Затем создайте список, в который будут добавлины все клиенты, и 
#выведете его в консоль. 

class Customers:
	def __init__(self, first_name, second_name, city, balance):
		self.first_name = first_name
		self.second_name = second_name
		self.balance = balance
		self.city = city
		
		
	def __str__(self):
		return f'''"{self.first_name} {self.second_name}".{self.city}. Баланс: {self.balance} руб.'''

	def get_guest(self):
		return f'{self.first_name} {self.second_name}, г.{self.city}'
		
costomer_1 = Customers('Иван' ,  'Петров' , 'Москва' ,50)
costomer_2 = Customers('Владимир' ,  'Зайцев' , 'Кострома' ,50)
costomer_3 = Customers('Оселя' ,  'Янина' , 'Новосибирск' ,50)

guest_list = [costomer_1, costomer_2, costomer_3]

	for guest in guest_list:
		print(guest.get_guest())


		
