def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
            break


def move_forward():
    while front_is_clear():
        move()


while not at_goal():
    move_forward()
    jump()



