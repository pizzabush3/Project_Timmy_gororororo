import turtle
turtle.tracer(0,0)
change = 0.5


# treat change as multiplier, higher change higher multiplier, lower change, lower multiplier
# only works if change is greater then 0.5
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
def make_shape_R(numb_sides_R, shape_size_R,degrees_R):
  for i in range(numb_sides_R):
    turtle.forward(shape_size_R*change)
    turtle.right(degrees_R/numb_sides_R)
def make_shape_L(numb_sides_L, shape_size_L,degrees_L):
  for i in range(numb_sides_L):
    turtle.forward(shape_size_L*change)
    turtle.left(degrees_L/numb_sides_L)
def fin(fin_size, fin_length):
  make_shape_L(100,1.3*fin_size,90*fin_length)
  make_shape_L(100,0.1*fin_size,170)
  turtle.right(20)
  make_shape_R(100,0.63*fin_size,80)
turtle.right(315)
make_shape_R(100,4,120)
make_shape_L(100,0.3,40)
turtle.right(120)
make_shape_R(100,3,75)
make_shape_L(100,0.85,32)
turtle.right(50)
make_shape_L(100,0.8,70)
turtle.forward(10)
make_shape_L(100,0.8,70)
make_shape_L(100,0.15,90)
turtle.right(50)
make_shape_L(100,0.8,78)
turtle.forward(10)
turtle.right(20)
turtle.forward(30)
turtle.right(32)
make_shape_L(100,2.5/3,50/3)
turtle.up()
make_shape_L(100,2.5/3,50/3)
turtle.down()
make_shape_L(100,2.5/3,50/3)
turtle.right(70)
fin(1,1)
turtle.up()
turtle.goto(50,40)
turtle.down()
for i in range(1,10):
  turtle.forward(10*i)
  turtle.right(90)
turtle.update()