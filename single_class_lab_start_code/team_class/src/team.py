class Team:
    def __init__(self, name, players, coach):

        # initialise instance variables
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        if player not in self.players:
            return False
        else: 
            return True

    
    def play_game(self, result):
        if result:
            self.points += 3
