import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GameAPIManager:
    def __init__(self):
        self.steam_api_key = os.getenv('STEAM_API_KEY')
        self.xbox_api_key = os.getenv('XBOX_API_KEY')
        self.ps_api_key = os.getenv('PS_API_KEY')

    def fetch_steam_game(self, appid):
        base_url = f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={self.steam_api_key}&appid={appid}"
        response = requests.get(base_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def fetch_xbox_game(self, game_id):
        headers = {'X-Authorization': self.xbox_api_key}
        base_url = f"https://xboxapi.com/v2/game-details/{game_id}"
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def fetch_ps_game(self, game_id):
        headers = {'Authorization': f'Bearer {self.ps_api_key}'}
        base_url = f"https://psnapi.com/v1/games/{game_id}"
        response = requests.get(base_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None

if __name__ == "__main__":
    game_manager = GameAPIManager()
    steam_game = game_manager.fetch_steam_game("440")
    xbox_game = game_manager.fetch_xbox_game("game_id_here")
    ps_game = game_manager.fetch_ps_game("game_id_here")

    print(steam_game)
    print(xbox_game)
    print(ps_game)