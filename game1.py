import random
import math
from meet import *
cells=[]

user_cell={"x":get_random_x(), "y":get_random_y(), "radius":15, "dy":random.random(), "dx":random.random()}
za=create_cell(user_cell)
cells.append(za)

for x in range(50) :
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":(random.random()*30)+10, "dy":random.random(), "dx":random.random	(),"color":"blue"}
	z=create_cell(cell1)
	cells.append(z)
	
def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if (x>width):
			cell.set_dx(-cell.get_dx())
		if (y>height):
			cell.set_dy(-cell.get_dy())
		if (x<-width):
			cell.set_dx(-cell.get_dx())
		if (y<-height):
			cell.set_dy(-cell.get_dy())


while True:
	move_cells(cells)
	borders(cells)


	
