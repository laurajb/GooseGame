from game import Game

game = Game(player1="Tana", player2="Ikal")

def test_game_has_two_players():
    assert game.get_player1_name() and  game.get_player2_name()

def test_player_space_None():
    assert game.get_player1_space() == None and game.get_player2_space() == None

def test_values_in_range():
    for i in range(1000):
        game.roll_dice()
        assert 1 <= game.d1 <=6 and 1 <= game.d2 <=6

def test_isNot9():
    for i in range(100):
        game.roll_dice()
        assert game.get_player1_space() != 9 and game.get_player2_space() != 9

