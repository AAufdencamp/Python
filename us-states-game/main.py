import pandas
import turtle


screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list() #converting series to list allows us to use keyword "in" below to check for a match

guessed_states = [ ]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    #print(answer_state) #prints user input

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pulls out the row we need
        t.goto(state_data.x.item(), state_data.y.item()) #state_data is a row of data, and we can access the info using the
        #t.write(state_data.state)                        #column names to subset. But because state_data is a
        t.write(state_data.state.item())                 #Pandas series subsetting returns both index AND item values
                                                     # use .item() to get JUST the item value

print(new_data)

#screen.exitonclick()

#convert the guess to Title case
#check if the guess is among the 50 states
#Write correct guesses onto the map
#Use a loop to allow the user to keep guessing
#Record the correct guesses in a list
#Keep track of the score

#####unused code but keep. All coordinates are already provided in 50_states.csv#####
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#####unused code but keep. All coordinates are already provided in 50_states.csv#####


turtle.mainloop() #alternative way of keeping screen open when code is done running


