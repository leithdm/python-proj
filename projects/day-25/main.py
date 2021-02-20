import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# convert csv to dataframe
data = pandas.read_csv("50_states.csv")
# covert dataframe to list
all_states = data['state'].to_list()
# list to store all of the users guesses. Prevents entering the same state twice
guessed_states = []
correct_answers = 0
while len(guessed_states) < 50:
    # .title() makes the first letter a Capital letter, to reflect the data
    answer_state = screen.textinput(title=f"Score is: {correct_answers}/50",
                                    prompt="What's another state's name?").title()

    # code-word to exit game
    if answer_state == "Exit":
        # generate a csv file of all the states that have not been guessed by the user
        # missed_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)

        # using List Comprehension, instead of code above to generate a csv for all states not guessed
        missed_states = [state for state in all_states if state not in guessed_states ]
        data_for_csv = pandas.DataFrame(missed_states)
        data_for_csv.to_csv("states_to_learn.csv")
        break
    # check if answer is in the list
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        correct_answers += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # get the row of data in dataframe where the 'state' is the correct answer
        state_data = data[data['state'] == answer_state]
        # use the coordinates of x and y to move pen to that location
        t.goto(int(state_data['x']), int(state_data['y']))
        # write the name of the state
        t.write(answer_state)


# function to get the mouse click coordinates
def get_mouse_click_coord(x, y):
    print(x, y)

# event listener for when the mouse is clicked. Used to find the state coordinates for initial csv setup
# turtle.onscreenclick(get_mouse_click_coord)
