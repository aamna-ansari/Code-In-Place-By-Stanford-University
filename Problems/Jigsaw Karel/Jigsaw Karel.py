from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    for i in range(2):
        turn_left()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
    for i in range(2):
        turn_right()



def turn_right():
  for i in range(3):
    turn_left()
if __name__ == '__main__':
    main()