#ICS3U Final - Shayaan Shaikh - June 19 2025
#image creds: Shayaan Shaikh using https://www.photopea.com/

#import moduels
from tkinter import *
from time import *
from random import *
from math import *

root = Tk()

#set up canvas
screen = Canvas(root, width=800, height=600, background="skyblue")

#set up arrays and var and to asssign the speed, x and y coords for pizzas. Also makes images
def setInitialValues():	
	global xman, yman, xspeed_man, yspeed_man, man_img, pizza_y, pizza_x, pizza_speed, pizza_type, score, mode
	
	#man arrays
	xman = 400
	yman = 300
	xspeed_man = 0
	yspeed_man = 0

	#pizza arrays
	pizza_x = []
	pizza_y = []
	pizza_speed = []
	pizza_type = [] #bad is -1 points and good is +1 points

	score = 1

	#make x pizza location, type and speed in the list
	for i in range(mode):
		# make a random location (x,y) and a random speed
		pizza_x.append(randint(50, 500))
		pizza_y.append(randint(-300, 0))
		pizza_speed.append(randint(3,7))
		#pizza type randomizer (50%)
		if randint(0,2) == 0:
			pizza_type.append("bad")
		else:
			pizza_type.append("good")

	man_img = PhotoImage(file = "man.png")

#handles what will happen if a key is pressed (left/right arrow)
def keyDownHandler( event ):
	global xspeed_man, yspeed_man

	if event.keysym == "Left":
		xspeed_man = -10
	elif event.keysym == "Right":
		xspeed_man = 10
	elif event.keysym == "Up":
		yspeed_man = -10
	elif event.keysym == "Down":
		yspeed_man = 10

#handles what will happen if a key is unpressed/relesed
def keyUpHandler(event):
	global xspeed_man, yspeed_man
	# to stop moving the man after the key is relesed
	xspeed_man = 0
	yspeed_man = 0

#makes the starting screen and the buttons too
def startScreen():
	#buttons:
	screen.create_rectangle(300, 155, 500, 210, fill = "#1f6346", outline = "white")
	screen.create_text(400, 180, text = "Easy Mode", font = "Arial 20 bold", fill = "white")

	screen.create_rectangle(300, 255, 500, 310, fill = "#1f6346", outline = "white")
	screen.create_text(400, 285, text = "Mid Mode", font = "Arial 20 bold", fill = "white")

	screen.create_rectangle(300, 355, 500, 410, fill = "#1f6346", outline = "white")
	screen.create_text(400, 385, text = "Hard Mode", font = "Arial 20 bold", fill = "white")

	#tital
	screen.create_text(400, 50, text = "Pizza Game", font = "Arial 50 bold", fill = "white")

	#instructions
	screen.create_text(400, 100, text = "Use arrow keys to move, Catch normal pizzas (red) for 1 point, and lose 1 point when a burnt one is caught (black). Stay above 0 points to win. Two Rounds", font = "Arial 7", fill = "white")

	#brand
	screen.create_text(400, 450, text = "©2025 - Shayaan Shaikh", font = "Arial 10", fill = "black")

	root.bind("<Button-1>", startScreen_mouse_handler)

#makes the buttons work for the starting screen
def startScreen_mouse_handler(event):
	global mode, xMouse, yMouse

	xMouse = event.x
	yMouse = event.y

	if 300 <= xMouse <= 500 and 155 <= yMouse <= 210:
		screen.delete("all")
		mode = 5
		runGame()
	elif 300 <= xMouse <= 500 and 255 <= yMouse <= 310:
		screen.delete("all")
		mode = 10
		runGame()
	elif 300 <= xMouse <= 500 and 355 <= yMouse <= 410:
		screen.delete("all")
		mode = 15
		runGame()
	else:
		pass

#to draw object that will stay on screen like the man and pizzas. also picks the color of the pizzas here
def drawObjects():
	global xman, yman, man_drawing, pizza_x, pizza_y, pizza_drawing, color, pizza_type, pizza_num

	pizza_num = []

	#man drawing
	man_drawing = screen.create_image(xman, yman, image = man_img)

	#color picker for pizza
	for i in range(len(pizza_x)):
		if pizza_type[i] == "good":
			color = "red"
		elif pizza_type[i] == "bad":
			color = "black"
	#pizza drawing
		pizza_drawing = screen.create_oval(pizza_x[i], pizza_y[i], pizza_x[i]+50, pizza_y[i]+50, fill = color) 
		pizza_num.append(pizza_drawing)

#draws the stats. In our case, the score
def drawStats():
	global livesDisplay, scoreDisplay, score, scoreText

	scoreText = screen.create_text(100, 50, text = f"Score: {score}", fill = "#111111")

# to draw the abackground during the main gameplay
def drawBackground():
	#road
	screen.create_rectangle(0, 600, 800, 350, fill="gray")
	screen.create_rectangle(100, 600, 150, 650, fill="white")
	#sun
	x = randint(200,600)
	y = randint(0, 100)
	x1 = x - 50
	y1 = y - 50
	x2 = x + 50
	y2 = y + 50
	screen.create_oval( x1,y1, x2,y2, fill = "yellow", outline = "white" )

#update the objects that was made during the drawObjects() like the man and pizzas
def updateObjectPositions():
	global yman, xman, xspeed_man, yspeed_man, pizza_speed, pizza_x, pizza_y

	#man updates
	xman = xman + xspeed_man
	yman = yman + yspeed_man
	
	for i in range(len(pizza_y)): # so it will repleat to how many values are in pizza_y (5)
		pizza_y[i] = pizza_y[i] + pizza_speed[i]

	#man ristriction
	if yman < 350:
		yman = 350
	if yman > 400:
		yman = 400
	if xman < 0:
		xman = 0
	if xman > 600:
		xman = 600

	#to reset pizza after falling
	for i in range(len(pizza_y)):
		if pizza_y[i] > 600: # if pizza falls below screenn
			pizza_y[i] = randint(-300, 0)
			pizza_x[i] = randint(50, 300)
			pizza_speed[i] = randint(3,5)

#used to check if there any collisions between the man and the pizzas and to assign points accordingly
def checkCollisions():
	global score, xman, yman, pizza_x, pizza_y, pizza_type, pizza_speed, score, hitbox

	#man hitbox
	man_left = xman - 25
	man_right = xman + 25
	man_up = yman - 25
	man_down = yman + 25

	#to view hitbox of the man, un-comment the next line
	#hitbox = screen.create_rectangle(man_right, man_down, man_left, man_up, fill = "red")

	for i in range(len(pizza_x)): # this will run how mnay val are in pizza_x bc there are 5 pizzas
		#pizza hitbox
		pizza_left = pizza_x[i]
		pizza_right = pizza_x[i] + 50
		pizza_up = pizza_y[i]
		pizza_down = pizza_y[i] + 50

		#if colision is dectectedd
		if man_right > pizza_left and man_left < pizza_right and man_down > pizza_up and man_up < pizza_down:
			if pizza_type[i] == "good":
				score = score + 1
			elif pizza_type[i] == "bad":
				score = score - 3


			#reset pizza to top of screen
			pizza_y[i] = randint(-300, 0)
			pizza_x[i] = randint(50, 350)
			pizza_speed[i] = randint(3,5)

#display the final screen menu for the quit and play again button
def engGame():

	#button backdrop and txt
	endsbox = screen.create_rectangle(300, 70, 500, 150, fill = "#1f6346")
	endstxt = screen.create_text(400, 100, text = "Play Again?", font = "Arial 16 bold", fill = "white")

	screen.create_rectangle(300, 200, 500, 280, fill = "#1f6346")
	screen.create_text(400, 230, text = "Quit", font = "Arial 16 bold", fill = "white")

	root.bind("<Button-1>", engGame_click)

#mouse click handler for the end game screen
def engGame_click(event):
	xMouse = event.x
	yMouse = event.y

	if 300 <= xMouse <= 500 and 70 <= yMouse <= 150:
		screen.delete("all")
		runGame()
	if 300 <= xMouse <= 500 and 200 <= yMouse <= 280:
		root.destroy()
		#got from nut jump
		#why does it take like 5 min to quit
		
#to run the main game
def runGame():
	global score

	setInitialValues()
	drawBackground()

	while score >= 0 :
		drawObjects()
		drawStats()
		updateObjectPositions() 
		checkCollisions()
		
		screen.update()
		sleep(0.03)
		screen.delete( man_drawing, *pizza_num, scoreText )
		# "*" is used in the screen.delete becuse i have all my pizzas info in 1 array, so in order to delete all of them and not only 1, i need to unpack the array.

	#to start the end screen when the score falls under 0
	engGame()
			
#to start the starting screen first
root.after(0, startScreen)

screen.bind("<Button-1>", startScreen_mouse_handler)
screen.bind("<ButtonRelease-1>", engGame_click)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)
screen.pack() #sets up the drawing screen (same as in any Tkinter program)
screen.focus_set() #makes Python pay attention to mouse clicks and button pushes
screen.mainloop()
