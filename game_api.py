import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GameAPIManager:
    def __init__(self):
        self.api_keys = {
            'steam': os.getenv('STEAM_API_KEY'),
            'xbox': os.getenv('XBOX_API_KEY'),
            'ps': os.getenv('PS_API_KEY')
        }

    def _common_fetch(self, url, headers=None):
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else None

    def fetch_steam_game(self, appid):
        base_url = f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={self.api_keys['steam']}&appid={appid}"
        return self._common_fetch(base_url)

    def fetch_xbox_game(self, game_id):
        headers = {'X-Authorization': self.api_keys['xbox']}
        base_url = f"https://xboxapi.com/v2/game-details/{game_id}"
        return self._common_fetch(base_url, headers)

    def fetch_ps_game(self, game_id):
        headers = {'Authorization': f'Bearer {self.api_keys['ps']}'}
        base_url = f"https://psnapi.com/v1/games/{game_id}"
        return self._common_fetch(base_url, headers)

if __name__ == "__main__":
    game_manager = GameAPIManager()
    steam_game = game_manager.fetch_steam_game("440")
    xbox_game = game_manager.fetch_xbox_game("game_id_here")
    ps_game = game_manager.fetch_ps_game("game_id_here")

    print(steam_game)
    print(xbox_game)
    print(ps_game)