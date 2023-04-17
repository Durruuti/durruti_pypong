import turtle
import time

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Pong by @Durruti")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Raquetas
raquetas = []

for posicion in ((-350, 0), (350, 0)):
    raqueta = turtle.Turtle()
    raqueta.speed(0)
    raqueta.shape("square")
    raqueta.color("white")
    raqueta.shapesize(stretch_wid=5, stretch_len=1)
    raqueta.penup()
    raqueta.goto(posicion)
    raquetas.append(raqueta)

puntuacion = {"A": 0, "B": 0}

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 1
pelota.dy = 1
escala_velocidad = 0.5  # ajustar la velocidad de la pelota (1 = fácil, 2 = medio, 3 = difícil)

# Marcadores
marcador_a = turtle.Turtle()
marcador_a.speed(0)
marcador_a.color("white")
marcador_a.penup()
marcador_a.hideturtle()
marcador_a.goto(-100, 260)

marcador_b = turtle.Turtle()
marcador_b.speed(0)
marcador_b.color("white")
marcador_b.penup()
marcador_b.hideturtle()
marcador_b.goto(100, 260)

# Funciones de movimiento de raquetas
def mover_raqueta(raqueta, y):
    nueva_posicion = raqueta.ycor() + y
    if nueva_posicion < -250:
        nueva_posicion = -250
    elif nueva_posicion > 250:
        nueva_posicion = 250
    raqueta.sety(nueva_posicion)

# Función de colisión
def colision(raqueta, pelota):
    if pelota.dx > 0: # si la pelota se mueve hacia la derecha
        x_dist = pelota.xcor() + 10 - raqueta.xcor() # distancia entre la pelota y el borde derecho de la raqueta
        if abs(x_dist) < 10 and pelota.ycor() < raqueta.ycor() + 50 and pelota.ycor() > raqueta.ycor() - 50:
            pelota.dx *= -1 # cambia la dirección de la pelota en el eje x si hay colisión
    elif pelota.dx < 0: # si la pelota se mueve hacia la izquierda
        x_dist = pelota.xcor() - 10 - raqueta.xcor() - 20 # distancia entre la pelota y el borde izquierdo de la raqueta
        if abs(x_dist) < 10 and pelota.ycor() < raqueta.ycor() + 50 and pelota.ycor() > raqueta.ycor() - 50:
            pelota.dx *= -1 # cambia la dirección de la pelota en el eje x si hay colisión



def actualizar_marcador(jugador, marcador):
    marcador.clear()
    marcador.write("Jugador {}: {}".format(jugador, puntuacion[jugador]), align="center", font=("Courier", 24))


while True:
    wn.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Colisiones con las paredes superior e inferior
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    # Colisiones con las raquetas
    for raqueta in raquetas:
        colision(raqueta, pelota)

    # Movimiento de las raquetas
    wn.listen()
    wn.onkeypress(lambda: mover_raqueta(raquetas[0], 20), "w")
    wn.onkeypress(lambda: mover_raqueta(raquetas[0], -20), "s")
    wn.onkeypress(lambda: mover_raqueta(raquetas[1], 20), "Up")
    wn.onkeypress(lambda: mover_raqueta(raquetas[1], -20), "Down")

    # Actualización de marcador y reinicio de la pelota en caso de gol
    if pelota.xcor() > 390:
        puntuacion["A"] += 1
        actualizar_marcador("A", marcador_a)
        pelota.goto(0, 0)
        pelota.dx *= -1
    elif pelota.xcor() < -390:
        puntuacion["B"] += 1
        actualizar_marcador("B", marcador_b)
        pelota.goto(0, 0)
        pelota.dx *= -1
