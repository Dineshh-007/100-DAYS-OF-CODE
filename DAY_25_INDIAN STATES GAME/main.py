import turtle
import pandas

screen = turtle.Screen()
screen.title("THE INDIAN STATES GAME")
# screen.setup(width=725, height=491)

image = "indian_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian_state.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 30:
    guess_state = screen.textinput(title=f"{len(guessed_states)} / 30 ",prompt="What's the another state?").title()

    if guess_state == "Exit":
        #use list comprehension which is used in US STATES GAME
        need_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                need_to_learn.append(state)
        states_learned = pandas.DataFrame(need_to_learn)
        states_learned.to_csv("states_to_learn.csv")   # here a new csv file will get created for the missing states
        break

    if guess_state in all_states and guess_state not in guessed_states:
        guessed_states.append(guess_state)
        row = data[data.state == guess_state]
        x = row.x.item()
        y = row.y.item()
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x,y)
        writer.write(guess_state, align="center", font=("Arial", 12, "bold"))

