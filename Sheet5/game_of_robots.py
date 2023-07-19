from gasp import *
from random import randint


def place_player():
    global player_x, player_y, player_shape

    print("I'm right here!")
    player_x  = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5, 10 * player_y +5 ), 5, filled=True, color=color.BLUE)


def move_player():
    global finished, player_shape, player_x, player_y

    print("I'm moving to...")
    key = update_when('key_pressed')
    if key == 'q':
        finished = True
    if key == 'd':
        player_x += 1

    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))


begin_graphics()
finished = False
place_player()

while not finished:
    move_player()

end_graphics()
