class GameStats():

    def _init_(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()

        # Start ALiens Invasion in an inactive state.
        self.game_active = False

        # Highscore should never be reset.
        self.high_score = 0

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
