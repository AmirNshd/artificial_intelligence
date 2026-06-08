from game import Game


game = Game(
    clean_terminal=True,
    wait_for=0.5,
    up_depth=7,
    down_depth=6,
    first_player=None
)

game.start_game()
