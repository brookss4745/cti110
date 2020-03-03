# This program will run with turtle and make designs
# 2/27/2020
# CTI-110-P2WH2 - Turtle Graphic 
# Sierra N. Brooks



import turtle

turtle = turtle.Turtle()

turtle.speed(10)

for i in range(180):
 turtle.forward(100)
 turtle.right(30)
 turtle.forward(20)
 turtle.left(60)
 turtle.forward(50)
 turtle.right(30)

 turtle.penup()
 turtle.setposition(0, 0)
 turtle.pendown()


 turtle.right(2)


turtle.done() 




#Pseudocode
#Declare Variable
#Import turtle

#Get Input
#Display a prompt to the user to get turtle
#Input turtle

#Calculate the numbers needed to  move forward and backwards


