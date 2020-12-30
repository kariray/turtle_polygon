import turtle

turtle.setup(width=1000, height=300) #터틀 창의 크기를 가로 1000, 세로 300으로 지정
t=turtle.Turtle() #터틀 불러오기

t.penup() #커서의 이동경로가 표시 안되게
t.goto(-400,0) #해당좌표로 커서 이동
t.color("red") #색깔 지정
t.pendown() #커서의 이동경로가 표시 되게
t.circle(50) #반지름 50짜리 원 그리기
t.penup()
t.goto(-400,-50)
t.write("원",font=(15))
t.pendown()

t.penup()
t.goto(-300,0)
t.color("orange")
t.pendown()
t.circle(50,steps=3)
t.penup()
t.goto(-300,-50)
t.write("삼각형",font=(15))
t.pendown()

t.penup()
t.goto(-200,0)
t.color("green")
t.pendown()
t.circle(50,steps=4)
t.penup()
t.goto(-200,-50)
t.write("사각형",font=(15))
t.pendown()

t.penup()
t.goto(-100,0)
t.color("green")
t.pendown()
t.circle(50,steps=5)
t.penup()
t.goto(-100,-50)
t.write("오각형",font=(15))
t.pendown()

t.penup()
t.goto(0,0)
t.color("blue")
t.pendown()
t.circle(50,steps=6)
t.penup()
t.goto(0,-50)
t.write("육각형",font=(15))
t.pendown()

t.penup()
t.goto(100,0)
t.color("purple")
t.pendown()
t.circle(50,steps=7)
t.penup()
t.goto(100,-50)
t.write("칠각형",font=(15))
t.pendown()

t.penup()
t.goto(200,0)
t.color("red")
t.pendown()
t.circle(50,steps=8)
t.penup()
t.goto(200,-50)
t.write("팔각형",font=(15))
t.pendown()

t.penup()
t.goto(300,0)
t.color("orange")
t.pendown()
t.circle(50,steps=9)
t.penup()
t.goto(300,-50)
t.write("구각형",font=(15))
t.pendown()

t.penup()
t.goto(400,0)
t.color("green")
t.pendown()
t.circle(50,steps=10)
t.penup()
t.goto(400,-50)
t.write("십각형",font=(15))
t.pendown()

