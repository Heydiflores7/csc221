from gasp import *
from random import randint

def draw_grid():
    for x in range(0, 640, 10):
        Line((x,0), (x, 640), thickness= 0.02, color=color.BLUE)

    for y in range(0, 480, 10):
        Line((0,y), (640, y), thickness=0.02, color=color.BLUE)

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
        player_x += 2
    if key == 'a':
        player_x += -2
    if key == 'w':
        player_y += 2
    if key == 's':
        player_y += -2
        
    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))


begin_graphics()
finished = False
place_player()
draw_grid()

while not finished:
    move_player()

end_graphics()
