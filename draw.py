import turtle as t

t.speed(10)
t.pensize(3)

def drawCircle(n,colorpen,colorfill):
    t.pencolor(colorpen)
    t.fillcolor(colorfill)
    t.begin_fill()
    t.circle(n)
    t.end_fill()

def movePen(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()  

def drawHeart(n,colorpen,colorfill):
    t.pencolor(colorpen)
    t.fillcolor(colorfill)
    t.begin_fill()
    t.left(135)
    t.circle(n,180)
    t.circle(4*n,25)
    # t.forward(2*n)
    t.left(45)
    t.circle(4*n,25)
    t.circle(n,180)
    t.end_fill()

    

    
movePen(0,0)
drawCircle(110,'#d7b317','#fff39d')
movePen(-40,130)
drawCircle(20,'#5d2750','#7e3807')
movePen(40,130)
drawCircle(20,'#5d2750','#7e3807')
movePen(0,95)
drawHeart(50,'#b03410','#fe633d')
movePen(-80,30)
drawCircle(20,'#d7b317','#fff39d')
movePen(60,30)
drawCircle(20,'#d7b317','#fff39d')
movePen(-35,155)
drawCircle(5,'#ffffff','#ffffff')
movePen(30,155)
drawCircle(5,'#ffffff','#ffffff')
movePen(-45,145)
drawCircle(3,'#ffffff','#ffffff')
movePen(45,145)
drawCircle(3,'#ffffff','#ffffff')
movePen(0,40)
t.write("武汉加油",False,'center',font=('arial',35,'normal'))



t.exitonclick()