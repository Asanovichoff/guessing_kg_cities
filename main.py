import turtle
import pandas

screen = turtle.Screen()
screen.title("Kyrgyzstan map game")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)
all_cities = []

while len(all_cities) < 7:
    guess = screen.textinput(title="Kyrgyzstan map game", prompt="Guess city")
    data = pandas.read_csv("cities")
    cities = data.city.tolist()

    if guess in cities:
        all_cities.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        cities_data = data[data.city == guess]
        t.goto(int(cities_data.x), int(cities_data.y))
        t.write(guess)


screen.exitonclick()
