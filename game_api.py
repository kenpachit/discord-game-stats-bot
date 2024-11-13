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
        # Check if any of the required API keys are missing
        for key, value in self.api_keys.items():
            if value is None:
                raise ValueError(f"API key for {key} is missing. Please check your .env file.")

    def _common_fetch(self, url, headers=None):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raises a HTTPError for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Python 3.6+
        except requests.exceptions.RequestException as err:
            print(f"Request exception occurred: {err}")
        return None

    def fetch_steam_game(self, appid):
        try:
            base_url = f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={self.api_keys['steam']}&appid={appid}"
            return self._common_fetch(base_url)
        except Exception as e:
            print(f"Failed to fetch Steam game with app ID {appid}: {e}")
            return None

    def fetch_xbox_game(self, game_id):
        try:
            headers = {'X-Authorization': self.api_keys['xbox']}
            base_url = f"https://xboxapi.com/v2/game-details/{game_id}"
            return self._common_fetch(base_url, headers)
        except Exception as e:
            print(f"Failed to fetch Xbox game with game ID {game_id}: {e}")
            return None

    def fetch_ps_game(self, game_id):
        try:
            headers = {'Authorization': f"Bearer {self.api_keys['ps']}"}
            base_url = f"https://psnapi.com/v1/games/{game_id}"
            return self._common_fetch(base_url, headers)
        except Exception as e:
            print(f"Failed to fetch PlayStation game with game ID {game_id}: {e}")
            return None

if __name__ == "__main__":
    game_manager = GameAPIManager()
    steam_game = game_manager.fetch_steam_game("440")
    xbox_game = game_manager.fetch_xbox_game("game_id_here")
    ps_game = game_manager.fetch_ps_game("game_id_here")

    print(steam_game)
    print(xbox_game)
    print(ps_game)