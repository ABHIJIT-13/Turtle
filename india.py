import turtle

tina = turtle.Turtle()


def chakra():
	tina.color('green')
	tina.left(90)
	tina.forward(200)
	tina.color('white')
	tina.goto(0,100)
	tina.color('blue')
	tina.width(5)
	tina.circle(100)
	tina.width(2)
	tina.goto(-100,100)
	for i in range(0,24):
		tina.left(15)
		tina.forward(100)
		tina.goto(-100,100)
		


def orange():
	tina.color('white')
	tina.goto(200,200)

	tina.color('orange')
	tina.begin_fill()
	tina.left(90)
	tina.forward(200)
	tina.left(90)
	tina.forward(600)
	tina.left(90)
	tina.forward(200)
	tina.left(90)
	tina.forward(600)
	tina.end_fill()

def green():
	tina.color('white')
	tina.goto(200,-200)

	tina.color('green')
	tina.begin_fill()
	tina.left(90)
	tina.forward(200)
	tina.left(90)
	tina.forward(600)
	tina.left(90)
	tina.forward(200)
	tina.left(90)
	tina.forward(600)
	tina.end_fill()




orange()
green()
chakra()

turtle.exitonclick()		