import turtle
import random
import time

# Pencereyi oluştur
wn = turtle.Screen()
wn.title("Catch 10 bananas Leonardo")
wn.bgcolor("light blue")
wn.setup(width=700, height=700)

# Oyuncu turtle'ını oluştur
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(0)
player.penup()
player.goto(0, 0)

cake_gif_path = "cake_gif.gif"
monkey_gif_path = "monkey_gif.gif"
wn.addshape("banana-dance.gif")
wn.addshape(cake_gif_path)
wn.addshape(monkey_gif_path)

# Yemekleri oluştur
food = turtle.Turtle()
food.shape("banana-dance.gif")
food.color("yellow")
food.speed(0)
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Skor
score = 0

# Skor metni için turtle
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("purple")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Hareket hızı
movement_speed = 10

# Ekran sınırları
left_boundary = -290
right_boundary = 290
top_boundary = 290
bottom_boundary = -290

# Hareket yönleri
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Oyuncu hareketi fonksiyonları
def move_left():
    global moving_left
    moving_left = True

def move_right():
    global moving_right
    moving_right = True

def move_up():
    global moving_up
    moving_up = True

def move_down():
    global moving_down
    moving_down = True

def stop_left():
    global moving_left
    moving_left = False

def stop_right():
    global moving_right
    moving_right = False

def stop_up():
    global moving_up
    moving_up = False

def stop_down():
    global moving_down
    moving_down = False

# Tuşları bağlayın
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")

wn.onkeyrelease(stop_left, "Left")
wn.onkeyrelease(stop_right, "Right")
wn.onkeyrelease(stop_up, "Up")
wn.onkeyrelease(stop_down, "Down")

# Hızı ayarla
turtle.delay(0)

# Oyun süresi (saniye cinsinden)
game_duration = 11

# Oyun başlangıç zamanı
start_time = time.time()


# Oyun döngüsü
while time.time() - start_time < game_duration:
    # Geriye kaç saniye kaldığını hesaplayın
    remaining_time = int(game_duration - (time.time() - start_time))
    # Yemek ve oyuncu arasındaki mesafeyi kontrol et
    if player.distance(food) < 20:
        food.goto(random.randint(left_boundary, right_boundary), random.randint(bottom_boundary, top_boundary))
        score += 1
    score_display.clear()
    score_display.write(f"{score}  {remaining_time}", align="center",font=("Courier", 25, "normal"))

    player.speed(0)

    if (moving_left or moving_right) and (moving_up or moving_down):
        if (moving_left and player.xcor() > left_boundary) and (moving_up and player.ycor() < top_boundary):
            player.setheading(135)
            player.goto(player.xcor() - movement_speed, player.ycor() + movement_speed)
        elif (moving_left and player.xcor() > left_boundary) and (moving_down and player.ycor() > bottom_boundary):
            player.setheading(225)
            player.goto(player.xcor() - movement_speed, player.ycor() - movement_speed)
        if (moving_right and player.xcor() < right_boundary) and (moving_up and player.ycor() < top_boundary):
            player.setheading(45)
            player.goto(player.xcor() + movement_speed, player.ycor() + movement_speed)
        elif (moving_right and player.xcor() < right_boundary) and (moving_down and player.ycor() > bottom_boundary):
            player.setheading(315)
            player.goto(player.xcor() + movement_speed, player.ycor() - movement_speed)
    else:
        if moving_left and player.xcor() > left_boundary:
            player.setheading(180)
            player.goto(player.xcor() - movement_speed, player.ycor())
        elif moving_right and player.xcor() < right_boundary:
            player.setheading(0)
            player.goto(player.xcor() + movement_speed, player.ycor())
        if moving_up and player.ycor() < top_boundary:
            player.setheading(90)
            player.goto(player.xcor(), player.ycor() + movement_speed)
        elif moving_down and player.ycor() > bottom_boundary:
            player.setheading(270)
            player.goto(player.xcor(), player.ycor() - movement_speed)


    wn.update()
    # 0.025 saniye bekleme ekleyin
    time.sleep(0.025)



# Oyun süresi dolduğunda ekranda bir mesaj göstermek için:
game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("red")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 60)


game_over_text2 = turtle.Turtle()
game_over_text2.speed(0)
game_over_text2.color("blue")
game_over_text2.penup()
game_over_text2.hideturtle()
game_over_text2.goto(0, 20)

if score < 10:
    game_over_text.write(f"Where are my {10 - score} bananas?", align="center", font=("Courier", 36, "normal"))
    game_over_text2.write(f"Your Bananas: {score}", align="center", font=("Courier", 36, "normal"))
    gif_turtle = turtle.Turtle()
    gif_turtle.shape(monkey_gif_path)
    gif_turtle.penup()
    gif_turtle.goto(0, -140)  # Adjust the position as needed
else:
    game_over_text.write("Let's make banana cake!", align="center", font=("Courier", 36, "normal"))
    game_over_text2.write(f"Your Bananas: {score}", align="center", font=("Courier", 36, "normal"))
    gif_turtle = turtle.Turtle()
    gif_turtle.shape(cake_gif_path)
    gif_turtle.penup()
    gif_turtle.goto(0, -140)  # Adjust the position as needed
    wn.bgcolor("yellow")  # Change background color to yellow
#oyunu kapatın
turtle.done()
