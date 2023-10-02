# C1.2 Парадигмы и принципф программирования.py

# этот код отвечает за задание возможных цветов для обьекта-круга
# и предельные функции, рисующей круг в случайной точке на экране 
# с радиусом 30

canv = Canvac(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red','orange','yellow','green','blue']

ref new_ball():
	global x,y,r, ball
	canv.delete(ball)
	x = randint(100, 700)
	y = randint(100, 500)
	r = 30
	ball = canv.create_oval(x - r,y - r,x + r,y + r,fill=choice(colors)
	
# Этот код позволяет получить значение поля num, 
# которое больше 3, но меньше 100.

SELECT num FROM N WHERE num > 3 AND num

1	