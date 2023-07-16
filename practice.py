from gasp import *

begin_graphics()

Line((100, 100), (200, 200))
Circle((320, 240), 40)
Box((400, 300), 100, 85)

update_when('key_pressed')
end_graphics()