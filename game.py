import random
from meet import *

cells = []
for i in range(99):
	cella = {"x":get_random_x(), "y":get_random_y(), "radius":20, 		"dy":random.random(), "dx":random.random()}
	za = create_cell(cella)
	cells.append(za)
while True:
	move_cells(cells)
	for cell in cells:
	if (cell.xcor() >= get_screen_width() or cell.xcor() <= 		get_screen_width()*(-1):
		cella."dx" == cella."dx"*(-1)
	if (cell.ycor() >= get_screen_height() or cell.ycor() <= 			get_screen_height()*(-1):
		cella."dy" == cella."dy"*(-1)
