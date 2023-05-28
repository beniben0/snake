import turtle
import time
import random

score=0
record=0
retarder=0.1

fenêtre=turtle.Screen()
fenêtre.title("Snake Game")
fenêtre.bgcolor("black")
fenêtre.setup(width=600, height=600)
fenêtre.tracer(0)

tête=turtle.Pen()
tête.shape("square")
tête.color("green")
tête.speed(0)
tête.penup()
tête.goto(0,0)
tête.direction="Stop"

fruit=turtle.Pen()
fruit.shape("triangle")
fruit.color("white")
fruit.penup()
fruit.goto(0,100)

# Pour le score et le record
encodage=turtle.Pen()
encodage.speed(0)
encodage.color("white")
encodage.penup()
encodage.hideturtle()
encodage.goto(0,250)
encodage.write("Score : 0  Record : 0", align="center", font=("candara", 24, "bold"))

def monter():
    if tête.direction!="bas":
        tête.direction="haut"

def descendre():
    if tête.direction!="haut":
        tête.direction="bas"

def tourner_a_droite():
    if tête.direction!="gauche":
        tête.direction="droite"        

def tourner_a_gauche():
    if tête.direction!="droite":
        tête.direction="gauche" 

def bouger():
    if tête.direction=="haut":
        y=tête.ycor()
        tête.sety(y+20)
    elif tête.direction=="bas":
        y=tête.ycor()
        tête.sety(y-20)
    elif tête.direction=="droite":
        x=tête.xcor()
        tête.setx(x+20)
    elif tête.direction=="gauche":
        x=tête.xcor()
        tête.setx(x-20)

fenêtre.listen()
fenêtre.onkeypress(monter,"Up")
fenêtre.onkeypress(descendre,"Down")
fenêtre.onkeypress(tourner_a_droite,"Right")
fenêtre.onkeypress(tourner_a_gauche,"Left")


game_is_on = True
corps = []

# Main Gameplay
while game_is_on:
	fenêtre.update()
	if tête.distance(fruit) < 20: # nouvelle position du fruit
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		fruit.goto(x, y)

		new_segment = turtle.Pen() # nouveau segment (queue)
		new_segment.shape("square")
		new_segment.color("orange") # tail colour
		new_segment.penup()
		corps.append(new_segment)
		score += 10
		if score > record:
			record = score
		encodage.clear()
		encodage.write("Score : {} Record : {} ".format(
			score, record), align="center", font=("candara", 24, "bold"))

	# Dessiner la queue
	for index in range(len(corps)-1, 0, -1): 
		x = corps[index-1].xcor()
		y = corps[index-1].ycor()
		corps[index].goto(x, y)
	if len(corps) > 0:
		x = tête.xcor()
		y = tête.ycor()
		corps[0].goto(x, y)
		
	bouger()		
	time.sleep(retarder)

	# Vérifier les collisions avec les bords
	if tête.xcor() > 290 or tête.xcor() < -290 or tête.ycor() > 290 or tête.ycor() < -290:
		tête.goto(0, 0)
		tête.direction = "Stop"
		for segment in corps:
			segment.goto(1000, 1000)
		corps.clear()
		score = 0
		encodage.clear()
		encodage.write("Score : {} Record : {} ".format(
			score, record), align="center", font=("candara", 24, "bold"))
	
	# Vérifier les collisions avec la queue
	for segment in corps:
		if segment.distance(tête) < 20:
			tête.goto(0, 0)
			tête.direction = "Stop"
			for segment in corps:
				segment.goto(1000, 1000)
			corps.clear()
			score = 0
			encodage.clear()
			encodage.write("Score : {} Record : {} ".format(
				score, record), align="center", font=("candara", 24, "bold"))
	


