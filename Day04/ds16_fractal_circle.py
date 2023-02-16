import turtle
t = turtle.Turtle()
t.shape("circle")

c = t.clone()
c.color("blue")
c.circle(30)

for i in range(4,40) :
    c.circle(i*10)
    c.circle(-i*10)

turtle.mainloop()