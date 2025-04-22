from karel.stanfordkarel import *
# Here is a place to program your Section problem
def main():
    while(front_is_clear()):
        move()
        if(beepers_present()):
            build_hospital()
def build_hospital():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right()
    move()
    turn_right()
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()
    turn_left()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
if _name_ == '_main_':
    main()

    # Add your 2nd approch here