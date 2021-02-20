import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. states quiz")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
hit=[]
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

state_list=data.state.to_list()
length= len(data.state.to_list())
while length > len(hit) :
    answer_state = screen.textinput(title=f"{len(hit)}/50 States Correct",
                                    prompt="Enter  state name").title()

    if answer_state == "Exit":
        missing_states = [states for states in state_list if states not in hit]
        pandas.DataFrame(missing_states).to_csv("States_to_learn.csv")

        break

    if answer_state in state_list:
        hit.append(answer_state)
        state_data = data[data.state == answer_state]
        x_cor=int(state_data.x)
        y_cor=int(state_data.y)
        state= turtle.Turtle()
        state.hideturtle()
        state.pu()

        state.goto(x_cor,y_cor)
        state.write(state_data.state.item(), "center", font=("Courier", 8, "normal"))
        #state.write(answer_state,"center",font=("Courier", 8, "normal"))



#turtle.mainloop()
#screen.exitonclick()