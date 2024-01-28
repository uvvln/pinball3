from game import Game
import shape_setups

g = Game(shape_setups.standard)

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

