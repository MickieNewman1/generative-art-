# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13th 03:57:04 2021

@author: mickie newman
"""
from turtle import * #fetches turtle commands
from random import * #fetches random number commands
import numpy as np

win = Screen()
win.bgcolor("#003249") #dark blue background

#hex colors
lightGray ='#CCDBDC'
purpleBlue = '#7692FF'
seaBlue = '#9AD1D4'
blueSky = '#7ED4E6'
bluerBlue = '#3BA99C' 

crystal = Turtle(visible=False)# so we dont see the turtle walking around ruens the imersion

crystal.speed("fastest")

crystal.width(3)

crystal.up()

colors = [lightGray , purpleBlue, seaBlue, blueSky, bluerBlue]#list of colors for the program to choose from

for i in range(randint(10, 50)): #randomizes how many times the loop is run
    crystal.color(choice(colors)) #choosing a random color
    crystal.goto(randint(-100,100), randint(-100,100)) #choosing a random starting point
    crystal.down()



    for i in range(randint(1, 50) ): #randomizes how long a single line goes for
        crystal.forward(50) #all segments are 50 long
        crystal.right(randint(-10, 10)*109) #randomizes which angle the turtle turns to, but in multiples of 109 degrees.
        #This is because due to the types of bonds in Tetrahedral structures have angles of 109 Degrees
done()