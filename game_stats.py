class GameStats():

    def _init_(self, ai_settings):

        self.ai_settings = ai_settings
        self.reset_stats()
        # Start ALiens Invasion in an active state.
        self.game_active = True

    def reset_stats(self):

        self.ships_left = self.ai_settings.ship_limit
