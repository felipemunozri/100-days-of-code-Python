from racquet import Racquet


class Player:
    def __init__(self, color, position):
        self.color = color
        self.score = 0
        self.racquet = Racquet(color, position)

    def reset_racquet(self, position):
        """Resets player racquet to position."""
        self.racquet.goto(position)
