
from turtle import *
import pygame
pygame.init()

print("Hello welcome to my game")
print("Press the arrow keys to go up or down or right or left")
print("Press 1234 to change color")
print("Press either d for pen down or u for pen up")


    # creating a loop to check events that
    # are occuring
i = 0
sen = input("Enter a number for the sensitivity and speed! (Reccomended 5 - 10) ")
print("OK!")
w = input("Enter line width(Rec : 1-20): ")
print("OK!")

col = input("what do you want the background to be(color)")
wn = Screen()
wn.bgcolor(col)
print("OK!")
w = float(w)
width(w)

sen = float(sen)
while True:
  i += sen
  def up():
      setheading(90)
      forward(i)
    
  def down():
      setheading(270)
      forward(i)
    
  def left():
      setheading(180)
      forward(i)
    
  def right():
      setheading(0)
      forward(i)
  def pen():
    penup()
  def pend():
    pendown()
  def colorR():
    color("red")
  def colorG():
    color("green")
  def colorB():
    color("blue")
  def colorBl():
    color("black")
  listen()
  
  onkey(colorR, '1')
  onkey(colorG, '2')
  onkey(colorB, '3')
  onkey(colorBl, '4')
  
  onkey(pend, 'd')
  onkey(pen, 'u')
  
  onkey(up, 'Up')
  
  onkey(down, 'Down')
  onkey(left, 'Left')
  onkey(right, 'Right')
    
  mainloop()
